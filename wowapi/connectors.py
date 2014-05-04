from .connector_base import APIConnector


class AuctionConnector(APIConnector):
    resource = "auction/data/"


class ItemConnector(APIConnector):
    filters = ['locale']
    resource = "item/"


class ItemSetConnector(APIConnector):
    filters = ['locale']
    resource = "item/set/"


class CharacterConnector(APIConnector):
    filters = ['locale', 'fields']
    resource = "character/"


class PetAbilitiesConnector(APIConnector):
    filters = ['locale']
    resource = "battlePet/ability/"


class PetSpeciesConnector(APIConnector):
    filters = ['locale']
    resource = "battlePet/species/"


class PetStatsConnector(APIConnector):
    filters = ['locale', 'level', 'breedId', 'qualityId']
    resource = "battlePet/stats/"


class RealmLeaderboardConnector(APIConnector):
    filters = ['locale']
    resource = "challenge/"


class RegionLeaderboardConnector(APIConnector):
    filters = ['locale']
    resource = "challenge/region"


class GuildProfileConnector(APIConnector):
    filters = ['locale', 'fields']
    resource = "guild/"


class ArenaTeamConnector(APIConnector):
    filters = ['locale']
    resource = "arena/"


class ArenaLadderConnector(APIConnector):
    filters = ['locale', 'page', 'size', 'asc']
    resource = "pvp/arena/"


class BattleGroundLadderConnector(APIConnector):
    filters = ['locale', 'page', 'size', 'asc']
    resource = "pvp/ratedbg/ladder"


class QuestConnector(APIConnector):
    filters = ['locale']
    resource = "quest/"


class RealmStatusConnector(APIConnector):
    filters = ['locale']
    resource = "realm/status"


class RecipeConnector(APIConnector):
    filters = ['locale']
    resource = "recipe/"


class SpellConnector(APIConnector):
    filters = ['locale']
    resource = "spell/"


class BattlegroupConnector(APIConnector):
    resource = "data/battlegroups/"


class CharacterRaceConnector(APIConnector):
    filters = ['locale']
    resource = "data/character/races"


class CharacterClassConnector(APIConnector):
    filters = ['locale']
    resource = "data/character/classes"


class CharacterAchievementConnector(APIConnector):
    filters = ['locale']
    resource = "data/character/achievements"


class GuildRewardConnector(APIConnector):
    filters = ['locale']
    resource = "data/guild/rewards"


class GuildPerkConnector(APIConnector):
    filters = ['locale']
    resource = "data/guild/perks"


class GuildAchievementConnector(APIConnector):
    filters = ['locale']
    resource = "data/guild/achievements"


class ItemClassConnector(APIConnector):
    filters = ['locale']
    resource = "data/item/classes"


class TalentConnector(APIConnector):
    filters = ['locale']
    resource = "data/talents"


class PetTypeConnector(APIConnector):
    filters = ['locale']
    resource = "data/pet/types"
