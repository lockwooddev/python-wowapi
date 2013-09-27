from .exceptions import APIError

import logging
import requests
from requests import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError
)


logger = logging.getLogger("wowapi")


class APIConnector(object):

    allowed_filters = []
    resource = ""

    def __init__(self, host, *args, **kwargs):
        self.host = host
        self.kwargs = kwargs
        self.args = args
        self.protocol = "https://" if self.kwargs.get("secure") else "http://"

    def get_query_parameters(self):
        params = {}
        for f in self.kwargs:
            if f in self.allowed_filters:
                params[f] = self.kwargs[f]
        return params

    def get_url(self):
        base = self.protocol + self.host + "/api/wow/" + self.resource
        url = base + "/".join(self.args)
        return url

    def handle_request(self, url, params=None):
        try:
            response = requests.get(url, params=params)
        except (RequestException, Timeout, URLRequired,
                TooManyRedirects, HTTPError, ConnectionError), e:
            logger.error("%s for %s" % (e, url))
            raise APIError(e)

        if not response.ok:
            logger.error("API response (%i) not okay for %s" % (response.status_code, url))
            raise APIError(response.status_code, response.json()["reason"])

        try:
            json_response = response.json()
        except ValueError, e:
            logger.error("No JSON object could be decoded for %s" % url)
            raise APIError(e)

        return json_response

    def get_resource(self):
        url = self.get_url()
        params = self.get_query_parameters()
        result = self.handle_request(url, params=params)
        return result


class AuctionConnector(APIConnector):
    resource = "auction/data/"


class ItemConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "item/"


class ItemSetConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "item/set/"


class CharacterConnector(APIConnector):
    allowed_filters = ['locale', 'fields']
    resource = "character/"


class PetAbilitiesConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "battlePet/ability/"


class PetSpeciesConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "battlePet/species/"


class PetStatsConnector(APIConnector):
    allowed_filters = ['locale', 'level', 'breedId', 'qualityId']
    resource = "battlePet/stats/"


class RealmLeaderboardConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "challenge/"


class RegionLeaderboardConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "challenge/region"


class GuildProfileConnector(APIConnector):
    allowed_filters = ['locale', 'fields']
    resource = "guild/"


class ArenaTeamConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "arena/"


class ArenaLadderConnector(APIConnector):
    allowed_filters = ['locale', 'page', 'size', 'asc']
    resource = "pvp/arena/"


class BattleGroundLadderConnector(APIConnector):
    allowed_filters = ['locale', 'page', 'size', 'asc']
    resource = "pvp/ratedbg/ladder"


class QuestConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "quest/"


class RealmStatusConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "realm/status"


class RecipeConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "recipe/"


class SpellConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "spell/"


# For Data Resources

class BattlegroupConnector(APIConnector):
    resource = "data/battlegroups/"


class CharacterRaceConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/character/races"


class CharacterClassConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/character/classes"


class CharacterAchievementConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/character/achievements"


class GuildRewardConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/guild/rewards"


class GuildPerkConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/guild/perks"


class GuildAchievementConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/guild/achievements"


class ItemClassConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/item/classes"


class TalentConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/talents"


class PetTypeConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "data/pet/types"
