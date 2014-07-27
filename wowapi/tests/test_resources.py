from wowapi.resources import APIResource, AuctionResource, CharacterResource

import json
from mock import patch
import pytest


class TestAPIResource:

    @pytest.fixture(autouse=True)
    def setup(self):
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
        assert hasattr(resource, "id")
        assert hasattr(resource, "name")
        assert hasattr(resource, "container")

    def test_all_keywords_false(self):
        resource = APIResource(self.response_dict, all_keywords=False)
        assert not hasattr(resource, "id")
        assert not hasattr(resource, "name")
        assert not hasattr(resource, "container")


class TestAuctionResource:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.response_dict = {
            "files": [
                {
                    "url": "http://test/auctions.json",
                    "lastModified": 1000
                }
            ]
        }

        self.auction_response = json.dumps({
            "realm": {
                "name": "Test Realm",
                "slug": "test-realm"
            },
            "alliance": {
                "auctions": [{
                    "auc": 1,
                    "item": 1,
                    "owner": "p1",
                    "bid": 1,
                    "buyout": 1,
                    "quantity": 1,
                    "timeLeft": "SHORT"
                }]
            },
            "horde": {
                "auctions": [{
                    "auc": 2,
                    "item": 1,
                    "owner": "p2",
                    "bid": 1,
                    "buyout": 1,
                    "quantity": 1,
                    "timeLeft": "SHORT"
                }]
            },
            "neutral": {
                "auctions": [{
                    "auc": 3,
                    "item": 1,
                    "owner": "p3",
                    "bid": 1,
                    "buyout": 1,
                    "quantity": 1,
                    "timeLeft": "SHORT"
                }]
            }
        })

    def test_properties(self):
        resource = AuctionResource(self.response_dict)
        assert resource.data == self.response_dict
        assert resource.url == self.response_dict['files'][0]['url']
        assert resource.last_modified == self.response_dict['files'][0]['lastModified']
        assert not resource.auction_data

    def test_is_new_no_auctions(self):
        """
        Tests timestamp is not older than the realm last_modified

        Should return True and not fetch the resource
        """
        resource = AuctionResource(self.response_dict)
        result = resource.is_new(1000)
        assert not result[0]
        assert not result[1]
        assert not resource.auction_data

    @patch("wowapi.connectors.APIConnector.handle_request")
    def test_is_new_auctions(self, mock):
        """
        Tests timestamp

        Should return True and fetch the resource
        """
        mock.return_value = self.auction_response
        resource = AuctionResource(self.response_dict)
        result = resource.is_new(800)
        assert result[0]
        assert result[1]
        assert resource.auction_data


class TestCharacterResource:

    @pytest.fixture(autouse=True)
    def setup(self):
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
        assert self.character["lastModified"] == resource.lastModified
        assert self.character["name"] == resource.name
        assert self.character["realm"] == resource.realm
        assert self.character["battlegroup"] == resource.battlegroup
        assert self.character["class"] == resource.class_
        assert self.character["race"] == resource.race
        assert self.character["gender"] == resource.gender
        assert self.character["level"] == resource.level
        assert self.character["achievementPoints"] == resource.achievementPoints
        assert self.character["thumbnail"] == resource.thumbnail
        assert self.character["calcClass"] == resource.calcClass
