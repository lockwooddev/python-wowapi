from .exceptions import APIError
from .connectors import APIConnector, CharacterConnector

import copy
import keyword
import logging


logger = logging.getLogger("wowapi")


class APIResource(object):

    def __init__(self, response_dict, all_keywords=False):
        self.data = response_dict

        # set all first row keys as attribute
        if all_keywords:
            for key in self.data:
                if key in keyword.kwlist:
                    setattr(self, key+"_", self.data[key])
                else:
                    setattr(self, key, self.data[key])


class AuctionResource(APIResource):

    def __init__(self, response_dict):
        super(AuctionResource, self).__init__(response_dict)
        self.url = self.data["files"][0]["url"]
        self.last_modified = self.data["files"][0]["lastModified"]
        self.auction_data = {}
        self._connector = APIConnector("")

    def is_new(self, timestamp=None):
        new = False

        if timestamp:
            if timestamp < self.last_modified:
                new = True
        else:
            # if no timestamp argument. Download auctions.
            new = True

        if new:
            try:
                self.auction_data = self._connector.handle_request(self.url)
            except APIError, e:
                logger.error(e)
                raise APIError(e)

        return new

    def get_property(self, key1, key2, false_return=[]):
        if self.auction_data:
            property_ = self.auction_data.get(key1)
            return property_[key2]
        return false_return

    @property
    def all(self):
        keywords = ["alliance", "horde", "neutral"]
        all_ = []
        if self.auction_data:
            dict_copy = copy.deepcopy(self.auction_data)
            for k in keywords:
                auctions = dict_copy.get(k)
                auctions = auctions["auctions"]

                for auction in auctions:
                    auction["faction"] = k
                    all_.append(auction)
        return all_

    @property
    def alliance(self):
        return self.get_property("alliance", "auctions")

    @property
    def horde(self):
        return self.get_property("horde", "auctions")

    @property
    def neutral(self):
        return self.get_property("neutral", "auctions")

    @property
    def realm_name(self):
        return self.get_property("realm", "name", '')

    @property
    def realm_slug(self):
        return self.get_property("realm", "slug", '')


class ItemResource(APIResource):
    pass


class ItemSetResource(APIResource):
    pass


class CharacterResource(APIResource):
    pass


class PetAbilitiesResource(APIResource):
    pass


class PetSpeciesResource(APIResource):
    pass


class PetStatsResource(APIResource):
    pass


class RealmLeaderboardResource(APIResource):
    pass


class RegionLeaderboardResource(APIResource):
    pass


class GuildProfileResource(APIResource):
    pass


class ArenaTeamResource(APIResource):
    pass


class ArenaLadderResource(APIResource):
    pass


class BattleGroundLadderResource(APIResource):
    pass


class QuestResource(APIResource):
    pass


class RealmStatusResource(APIResource):
    pass


class RecipeResource(APIResource):
    pass


class SpellResource(APIResource):
    pass


class DataResource(APIResource):
    pass