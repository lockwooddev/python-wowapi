import connectors
import resources


def get_auctions(host, realm_slug, **kwargs):
    connector = connectors.AuctionConnector(host, *[realm_slug], **kwargs)
    return resources.AuctionResource(connector.get_resource())


def get_item(host, item_id, **kwargs):
    connector = connectors.ItemConnector(host, *[item_id], **kwargs)
    return resources.ItemResource(connector.get_resource(), all_keywords=True)


def get_item_set(host, set_id, **kwargs):
    connector = connectors.ItemSetConnector(host, *[set_id], **kwargs)
    return resources.ItemSetResource(connector.get_resource(), all_keywords=True)


def get_character(host, realm_slug, character_name, **kwargs):
    connector = connectors.CharacterConnector(host, *[realm_slug, character_name], **kwargs)
    return resources.CharacterResource(connector.get_resource(), all_keywords=True)


def get_pet_abilities(host, ability_id, **kwargs):
    connector = connectors.PetAbilitiesConnector(host, *[ability_id], **kwargs)
    return resources.PetAbilitiesResource(connector.get_resource(), all_keywords=True)


def get_pet_species(host, species_id, **kwargs):
    connector = connectors.PetSpeciesConnector(host, *[species_id], **kwargs)
    return resources.PetSpeciesResource(connector.get_resource(), all_keywords=True)


def get_pet_stats(host, species_id, **kwargs):
    connector = connectors.PetStatsConnector(host, *[species_id], **kwargs)
    return resources.PetStatsResource(connector.get_resource(), all_keywords=True)


def get_realm_leaderboard(host, realm_slug, **kwargs):
    connector = connectors.RealmLeaderboardConnector(host, *[realm_slug], **kwargs)
    return resources.RealmLeaderboardResource(connector.get_resource(), all_keywords=True)


def get_region_leaderboard(host, **kwargs):
    connector = connectors.RegionLeaderboardConnector(host, **kwargs)
    return resources.RegionLeaderboardResource(connector.get_resource(), all_keywords=True)


def get_guild_profile(host, realm_slug, guild_name, **kwargs):
    connector = connectors.GuildProfileConnector(host, *[realm_slug, guild_name], **kwargs)
    return resources.GuildProfileResource(connector.get_resource(), all_keywords=True)


def get_arena_team(host, realm_slug, team_size, team_name, **kwargs):
    connector = connectors.ArenaTeamConnector(host, *[realm_slug, team_size, team_name], **kwargs)
    return resources.ArenaTeamResource(connector.get_resource(), all_keywords=True)


def get_arena_ladder(host, battlegroup, team_size, **kwargs):
    connector = connectors.ArenaLadderConnector(host, *[battlegroup, team_size], **kwargs)
    return resources.ArenaLadderResource(connector.get_resource(), all_keywords=True)


def get_rated_battleground_ladder(host, **kwargs):
    connector = connectors.BattleGroundLadderConnector(host, **kwargs)
    return resources.BattleGroundLadderResource(connector.get_resource(), all_keywords=True)


def get_quest(host, quest_id, **kwargs):
    connector = connectors.QuestConnector(host, *[quest_id], **kwargs)
    return resources.QuestResource(connector.get_resource(), all_keywords=True)


def get_realm_status(host, **kwargs):
    connector = connectors.RealmStatusConnector(host, **kwargs)
    return resources.RealmStatusResource(connector.get_resource(), all_keywords=True)


def get_recipe(host, recipe_id, **kwargs):
    connector = connectors.RecipeConnector(host, *[recipe_id], **kwargs)
    return resources.RecipeResource(connector.get_resource(), all_keywords=True)


def get_spell(host, spell_id, **kwargs):
    connector = connectors.SpellConnector(host, *[spell_id], **kwargs)
    return resources.SpellResource(connector.get_resource(), all_keywords=True)


def get_battlegroups(host, **kwargs):
    connector = connectors.BattlegroupConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_character_races(host, **kwargs):
    connector = connectors.CharacterRaceConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_character_classes(host, **kwargs):
    connector = connectors.CharacterClassConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_character_achievements(host, **kwargs):
    connector = connectors.CharacterAchievementConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_guild_rewards(host, **kwargs):
    connector = connectors.GuildRewardConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_guild_perks(host, **kwargs):
    connector = connectors.GuildPerkConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_guild_achievements(host, **kwargs):
    connector = connectors.GuildAchievementConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_item_classes(host, **kwargs):
    connector = connectors.ItemClassConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_talents(host, **kwargs):
    connector = connectors.TalentConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)


def get_pet_types(host, **kwargs):
    connector = connectors.PetTypeConnector(host, **kwargs)
    return resources.DataResource(connector.get_resource(), all_keywords=True)
