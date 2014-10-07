from .exceptions import WowApiError
from .connectors import APIConnector
from .resource_base import APIResource


class AuctionResource(APIResource):

    def __init__(self, response_dict):
        super(AuctionResource, self).__init__(response_dict)
        self.url = self.data["files"][0]["url"]
        self.last_modified = self.data["files"][0]["lastModified"]
        self.auction_data = {}
        self._connector = APIConnector("")

    def __repr__(self):
        return '<{0} ({1})>'.format(self.__class__.__name__, self.url)

    def is_new(self, timestamp):
        # only fetch if the timestamp arg is older than the last_modified of the realm.
        if timestamp < self.last_modified:
            self.auction_data = self.download_auctions()
            return True, self.auction_data
        else:
            return False, None

    def download_auctions(self):
        try:
            return self._connector.handle_request(self.url)
        except WowApiError, e:
            raise WowApiError(e)


class ItemResource(APIResource):

    def __repr__(self):
        return '<%s (%i): %s>' % (
            self.__class__.__name__, self.data['id'], self.data['name'].encode('utf-8'))


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
