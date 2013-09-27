from .exceptions import APIError
from .connectors import APIConnector

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

    def is_new(self, last_timestamp=None, fetch=False):
        new = False

        # If last_timestamp as arg, compare if given ts is smaller
        # of course the arg ts should be the ts of your last fetched last_modified key.
        if last_timestamp:
            if last_timestamp < self.last_modified:
                new = True
        # new auctions also true if last_timestamp not an arg. This is useful if you request this
        # endpoint for the first time.
        else:
            new = True

        # If fetch and new are true, it downloads the auctions and sets the auction_data attribute.
        if fetch and new:
            self.auction_data = self.download_auctions()

        return new

    def download_auctions(self):
        try:
            return self._connector.handle_request(self.url)
        except APIError, e:
            logger.error(e)
            raise APIError(e)

    def get_property(self, key1, key2, false_return=[]):
        if self.auction_data:
            property_ = self.auction_data.get(key1)
            return property_[key2]
        return false_return

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
