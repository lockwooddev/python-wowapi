from .connectors import (
    AuctionConnector, ItemConnector, ItemSetConnector, CharacterConnector,
    PetAbilitiesConnector, PetSpeciesConnector, PetStatsConnector,
    RealmLeaderboardConnector, RegionLeaderboardConnector,
    GuildProfileConnector,
    ArenaTeamConnector, ArenaLadderConnector, BattleGroundLadderConnector,
    QuestConnector, RealmStatusConnector, RecipeConnector, SpellConnector,
    BattlegroupConnector, CharacterRaceConnector, CharacterClassConnector,
    CharacterAchievementConnector, GuildRewardConnector, GuildPerkConnector,
    GuildAchievementConnector, ItemClassConnector, TalentConnector,
    PetTypeConnector
)
from .resources import (
    AuctionResource, ItemResource, ItemSetResource, CharacterResource,
    PetAbilitiesResource, PetSpeciesResource, PetStatsResource,
    RealmLeaderboardResource, RegionLeaderboardResource, GuildProfileResource,
    ArenaTeamResource, ArenaLadderResource, BattleGroundLadderResource,
    QuestResource, RealmStatusResource, RecipeResource, SpellResource,
    DataResource
)


def get_auctions(host, realm_slug, **kwargs):
    connector = AuctionConnector(host, *[realm_slug], **kwargs)
    return AuctionResource(connector.get_resource())


def get_item(host, item_id, **kwargs):
    connector = ItemConnector(host, *[item_id], **kwargs)
    return ItemResource(connector.get_resource(), all_keywords=True)


def get_item_set(host, set_id, **kwargs):
    connector = ItemSetConnector(host, *[set_id], **kwargs)
    return ItemSetResource(connector.get_resource(), all_keywords=True)


def get_character(host, realm_slug, character_name, **kwargs):
    connector = CharacterConnector(host, *[realm_slug, character_name], **kwargs)
    return CharacterResource(connector.get_resource(), all_keywords=True)


def get_pet_abilities(host, ability_id, **kwargs):
    connector = PetAbilitiesConnector(host, *[ability_id], **kwargs)
    return PetAbilitiesResource(connector.get_resource(), all_keywords=True)


def get_pet_species(host, species_id, **kwargs):
    connector = PetSpeciesConnector(host, *[species_id], **kwargs)
    return PetSpeciesResource(connector.get_resource(), all_keywords=True)


def get_pet_stats(host, species_id, **kwargs):
    connector = PetStatsConnector(host, *[species_id], **kwargs)
    return PetStatsResource(connector.get_resource(), all_keywords=True)


def get_realm_leaderboard(host, realm_slug, **kwargs):
    connector = RealmLeaderboardConnector(host, *[realm_slug], **kwargs)
    return RealmLeaderboardResource(connector.get_resource(), all_keywords=True)


def get_region_leaderboard(host, **kwargs):
    connector = RegionLeaderboardConnector(host, **kwargs)
    return RegionLeaderboardResource(connector.get_resource(), all_keywords=True)


def get_guild_profile(host, realm_slug, guild_name, **kwargs):
    connector = GuildProfileConnector(host, *[realm_slug, guild_name], **kwargs)
    return GuildProfileResource(connector.get_resource(), all_keywords=True)


def get_arena_team(host, realm_slug, team_size, team_name, **kwargs):
    connector = ArenaTeamConnector(host, *[realm_slug, team_size, team_name], **kwargs)
    return ArenaTeamResource(connector.get_resource(), all_keywords=True)


def get_arena_ladder(host, battlegroup, team_size, **kwargs):
    connector = ArenaLadderConnector(host, *[battlegroup, team_size], **kwargs)
    return ArenaLadderResource(connector.get_resource(), all_keywords=True)


def get_rated_battleground_ladder(host, **kwargs):
    connector = BattleGroundLadderConnector(host, **kwargs)
    return BattleGroundLadderResource(connector.get_resource(), all_keywords=True)


def get_quest(host, quest_id, **kwargs):
    connector = QuestConnector(host, *[quest_id], **kwargs)
    return QuestResource(connector.get_resource(), all_keywords=True)


def get_realm_status(host, **kwargs):
    connector = RealmStatusConnector(host, **kwargs)
    return RealmStatusResource(connector.get_resource(), all_keywords=True)


def get_recipe(host, recipe_id, **kwargs):
    connector = RecipeConnector(host, *[recipe_id], **kwargs)
    return RecipeResource(connector.get_resource(), all_keywords=True)


def get_spell(host, spell_id, **kwargs):
    connector = SpellConnector(host, *[spell_id], **kwargs)
    return SpellResource(connector.get_resource(), all_keywords=True)


# data resources

def get_battlegroups(host, **kwargs):
    connector = BattlegroupConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_character_races(host, **kwargs):
    connector = CharacterRaceConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_character_classes(host, **kwargs):
    connector = CharacterClassConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_character_achievements(host, **kwargs):
    connector = CharacterAchievementConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_guild_rewards(host, **kwargs):
    connector = GuildRewardConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_guild_perks(host, **kwargs):
    connector = GuildPerkConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_guild_achievements(host, **kwargs):
    connector = GuildAchievementConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_item_classes(host, **kwargs):
    connector = ItemClassConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_talents(host, **kwargs):
    connector = TalentConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)


def get_pet_types(host, **kwargs):
    connector = PetTypeConnector(host, **kwargs)
    return DataResource(connector.get_resource(), all_keywords=True)
