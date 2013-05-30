from .connectors import (
    AuctionConnector, ItemConnector, ItemSetConnector, CharacterConnector,
    PetAbilitiesConnector, PetSpeciesConnector, PetStatsConnector,
    RealmLeaderboardConnector, RegionLeaderboardConnector,
    GuildProfileConnector,
    ArenaTeamConnector, ArenaLadderConnector, BattleGroundLadderConnector,
    QuestConnector, RealmStatusConnector, RecipeConnector, SpellConnector
)
from .resources import (
    AuctionResource, ItemResource, ItemSetResource, CharacterResource,
    PetAbilitiesResource, PetSpeciesResource, PetStatsResource,
    RealmLeaderboardResource, RegionLeaderboardResource, GuildProfileResource,
    ArenaTeamResource, ArenaLadderResource, BattleGroundLadderResource,
    QuestResource, RealmStatusResource, RecipeResource, SpellResource
)


def get_auctions(host, realm_slug, **kwargs):
    connector = AuctionConnector(host, *[realm_slug], **kwargs)
    response_dict = connector.get_resource()
    return AuctionResource(response_dict)


def get_item(host, item_id, **kwargs):
    connector = ItemConnector(host, *[item_id], **kwargs)
    response_dict = connector.get_resource()
    return ItemResource(response_dict, all_keywords=True)


def get_item_set(host, set_id, **kwargs):
    connector = ItemSetConnector(host, *[set_id], **kwargs)
    response_dict = connector.get_resource()
    return ItemSetResource(response_dict, all_keywords=True)


def get_character(host, realm_slug, character_name, **kwargs):
    connector = CharacterConnector(
        host, *[realm_slug, character_name], **kwargs)
    response_dict = connector.get_resource()
    return CharacterResource(response_dict, all_keywords=True)


def get_pet_abilities(host, ability_id, **kwargs):
    connector = PetAbilitiesConnector(host, *[ability_id], **kwargs)
    response_dict = connector.get_resource()
    return PetAbilitiesResource(response_dict, all_keywords=True)


def get_pet_species(host, species_id, **kwargs):
    connector = PetSpeciesConnector(host, *[species_id], **kwargs)
    response_dict = connector.get_resource()
    return PetSpeciesResource(response_dict, all_keywords=True)


def get_pet_stats(host, species_id, **kwargs):
    connector = PetStatsConnector(host, *[species_id], **kwargs)
    response_dict = connector.get_resource()
    return PetStatsResource(response_dict, all_keywords=True)


def get_realm_leaderboard(host, realm_slug, **kwargs):
    connector = RealmLeaderboardConnector(host, *[realm_slug], **kwargs)
    response_dict = connector.get_resource()
    return RealmLeaderboardResource(response_dict, all_keywords=True)


def get_region_leaderboard(host, **kwargs):
    connector = RegionLeaderboardConnector(host, **kwargs)
    response_dict = connector.get_resource()
    return RegionLeaderboardResource(response_dict, all_keywords=True)


def get_guild_profile(host, realm_slug, guild_name, **kwargs):
    connector = GuildProfileConnector(host, *[realm_slug, guild_name], **kwargs)
    response_dict = connector.get_resource()
    return GuildProfileResource(response_dict, all_keywords=True)


def get_arena_team(host, realm_slug, team_size, team_name, **kwargs):
    connector = ArenaTeamConnector(
        host, *[realm_slug, team_size, team_name], **kwargs)
    response_dict = connector.get_resource()
    return ArenaTeamResource(response_dict, all_keywords=True)


def get_arena_ladder(host, battlegroup, team_size, **kwargs):
    connector = ArenaLadderConnector(host, *[battlegroup, team_size], **kwargs)
    response_dict = connector.get_resource()
    return ArenaLadderResource(response_dict, all_keywords=True)


def get_rated_battleground_ladder(host, **kwargs):
    connector = BattleGroundLadderConnector(host, **kwargs)
    response_dict = connector.get_resource()
    return BattleGroundLadderResource(response_dict, all_keywords=True)


def get_quest(host, quest_id, **kwargs):
    connector = QuestConnector(host, *[quest_id], **kwargs)
    response_dict = connector.get_resource()
    return QuestResource(response_dict, all_keywords=True)


def get_realm_status(host, **kwargs):
    connector = RealmStatusConnector(host, **kwargs)
    response_dict = connector.get_resource()
    return RealmStatusResource(response_dict, all_keywords=True)


def get_recipe(host, recipe_id, **kwargs):
    connector = RecipeConnector(host, *[recipe_id], **kwargs)
    response_dict = connector.get_resource()
    return RecipeResource(response_dict, all_keywords=True)


def get_spell(host, spell_id, **kwargs):
    connector = SpellConnector(host, *[spell_id], **kwargs)
    response_dict = connector.get_resource()
    return SpellResource(response_dict, all_keywords=True)