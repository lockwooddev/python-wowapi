from wowapi.resources import APIResource, AuctionResource

import json
from mock import patch
import unittest


class APIResourceTest(unittest.TestCase):

    def setUp(self):
        self.response_dict = {
            "id": 9999,
            "name": "test",
            "container": [
                {"a": 1},
                {"b", 2}
            ]
        }

    def test_all_keywords_true(self):
        resource = APIResource(self.response_dict, all_keywords=True)
        self.assertTrue(hasattr(resource, "id"))
        self.assertTrue(hasattr(resource, "name"))
        self.assertTrue(hasattr(resource, "container"))

    def test_all_keywords_false(self):
        resource = APIResource(self.response_dict, all_keywords=False)
        self.assertFalse(hasattr(resource, "id"))
        self.assertFalse(hasattr(resource, "name"))
        self.assertFalse(hasattr(resource, "container"))


class AuctionResourceTest(unittest.TestCase):

    def setUp(self):
        self.response_dict = {
            "files":[
                {
                     "url":"http://test/auctions.json",
                     "lastModified":1369578638000
                }
            ]
        }

        self.auction_response = json.dumps({
            "realm": {
                "name":"Test Realm",
                "slug":"test-realm"
            },
            "alliance": {
                "auctions":[
                    {"auc":1,"item":1,"owner":"p1","bid":1,"buyout":1,
                        "quantity":1,"timeLeft":"SHORT"},
                ]
            },
            "horde": {
                "auctions":[
                    {"auc":2,"item":1,"owner":"p2","bid":1,"buyout":1,
                        "quantity":1,"timeLeft":"SHORT"},
                ]
            },
            "neutral": {
                "auctions":[
                    {"auc":3,"item":1,"owner":"p3","bid":1,"buyout":1,
                        "quantity":1,"timeLeft":"SHORT"},
                ]
            }
        })

    def test_instantiation(self):
        resource = AuctionResource(self.response_dict)
        self.assertEqual([], resource.all)
        self.assertEqual([], resource.alliance)
        self.assertEqual([], resource.horde)
        self.assertEqual([], resource.neutral)
        self.assertEqual('', resource.realm_name)
        self.assertEqual('', resource.realm_slug)

    @patch("wowapi.connectors.APIConnector.handle_request")
    def test_is_updated_no_timestamp_given(self, mock):
        mock.return_value = self.auction_response
        resource = AuctionResource(self.response_dict)
        has_new = resource.is_updated()
        self.assertTrue(has_new)
        self.assertTrue(resource.auction_data)

    def test_is_updated_timestamp_old(self):
        resource = AuctionResource(self.response_dict)
        has_new = resource.is_updated(timestamp=1369578638001)
        self.assertFalse(has_new)
        self.assertFalse(resource.auction_data)

    @patch("wowapi.connectors.APIConnector.handle_request")
    def test_is_updated_timestamp_new(self, mock):
        mock.return_value = self.auction_response
        resource = AuctionResource(self.response_dict)
        has_new = resource.is_updated(timestamp=1369578637999)
        self.assertTrue(has_new)
        self.assertTrue(resource.auction_data)

    def test_properties(self):
        resource = AuctionResource(self.response_dict)
        resource.auction_data = json.loads(self.auction_response)
        self.assertTrue(resource.all)
        self.assertEqual("alliance", resource.all[0]["faction"])
        self.assertEqual("horde", resource.all[1]["faction"])
        self.assertEqual("neutral", resource.all[2]["faction"])

        self.assertEqual(1, len(resource.alliance))
        self.assertEqual(1, resource.alliance[0]["auc"])
        self.assertNotIn("faction", resource.alliance)

        self.assertEqual(1, len(resource.horde))
        self.assertEqual(2, resource.horde[0]["auc"])
        self.assertNotIn("faction", resource.horde)

        self.assertEqual(1, len(resource.neutral))
        self.assertEqual(3, resource.neutral[0]["auc"])
        self.assertNotIn("faction", resource.neutral)

        self.assertEqual('Test Realm', resource.realm_name)
        self.assertEqual('test-realm', resource.realm_slug)