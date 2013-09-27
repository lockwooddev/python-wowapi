from wowapi.resources import APIResource, AuctionResource, CharacterResource

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
                {"b": 2}
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
                     "lastModified":1000
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
        self.assertEqual([], resource.alliance)
        self.assertEqual([], resource.horde)
        self.assertEqual([], resource.neutral)
        self.assertEqual('', resource.realm_name)
        self.assertEqual('', resource.realm_slug)

    def test_is_new_1(self):
        """
        Tests no last_timestamp given and fetch False

        Should return True and not fetch the resource
        """
        resource = AuctionResource(self.response_dict)
        self.assertTrue(resource.is_new(fetch=False))
        self.assertFalse(resource.auction_data)

    @patch("wowapi.connectors.APIConnector.handle_request")
    def test_is_new_2(self, mock):
        """
        Tests no last_timestamp given and fetch True

        Should return True and fetch the resource
        """
        mock.return_value = self.auction_response
        resource = AuctionResource(self.response_dict)
        self.assertTrue(resource.is_new(fetch=True))
        self.assertTrue(resource.auction_data)

    def test_is_new_3(self):
        """
        Tests old last_timestamp given and fetch False

        Should return True and not fetch the resource
        """
        resource = AuctionResource(self.response_dict)
        has_new = resource.is_new(last_timestamp=800, fetch=False)
        self.assertTrue(has_new)
        self.assertFalse(resource.auction_data)

    @patch("wowapi.connectors.APIConnector.handle_request")
    def test_is_new_4(self, mock):
        """
        Tests new last_timestamp given and fetch True

        Should return False and not fetch the resource
        """
        mock.return_value = self.auction_response
        resource = AuctionResource(self.response_dict)
        has_new = resource.is_new(last_timestamp=1100, fetch=True)
        self.assertFalse(has_new)
        self.assertFalse(resource.auction_data)

    def test_properties(self):
        resource = AuctionResource(self.response_dict)
        resource.auction_data = json.loads(self.auction_response)

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


class ItemResourceTest(unittest.TestCase):

    def setUp(self):
        pass


class CharacterResourceTest(unittest.TestCase):

    def setUp(self):
        self.character = {
            "lastModified": 1000000000000,
            "name": "Test Player 1",
            "realm": "test-realm",
            "battlegroup": "Test Battlegroup",
            "class": 1,
            "race": 1,
            "gender": 0,
            "level": 60,
            "achievementPoints": 0,
            "thumbnail": "test-avatar.jpg",
            "calcClass": "U"
        }

    def test_instantiation(self):
        resource = CharacterResource(self.character, all_keywords=True)
        self.assertEqual(self.character["lastModified"], resource.lastModified)
        self.assertEqual(self.character["name"], resource.name)
        self.assertEqual(self.character["realm"], resource.realm)
        self.assertEqual(self.character["battlegroup"], resource.battlegroup)
        self.assertEqual(self.character["class"], resource.class_)
        self.assertEqual(self.character["race"], resource.race)
        self.assertEqual(self.character["gender"], resource.gender)
        self.assertEqual(self.character["level"], resource.level)
        self.assertEqual(
            self.character["achievementPoints"], resource.achievementPoints)
        self.assertEqual(self.character["thumbnail"], resource.thumbnail)
        self.assertEqual(self.character["calcClass"], resource.calcClass)
