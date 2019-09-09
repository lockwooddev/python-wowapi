# wowapi

# wowapi.api

## WowApi
```python
WowApi(self, client_id, client_secret, retry_conn_failures=False)
```


```python
import os

from wowapi import WowApi

api = WowApi('client_id', 'client_secret')

# Token price
api.get_token('eu', namespace='dynamic-eu', locale='de_DE')

# Auctions
api.get_auctions('eu', 'silvermoon', locale='de_DE')
```

### get_data_resource
```python
WowApi.get_data_resource(self, url, region)
```

Some endpoints return a url pointing to another resource.
These urls do not include OAuth tokens.
`api.get_data_resource` takes care of this.

```python
auctions_ref = api.get_auctions('eu', 'silvermoon', locale='de_DE')
api.get_data_resource(auctions_ref['files'][0]['url'], 'eu')
```

# wowapi.mixins.community

## CommunityMixin
```python
CommunityMixin(self, /, *args, **kwargs)
```
All Community API methods
### get_oauth_profile
```python
CommunityMixin.get_oauth_profile(self, region)
```

World of Warcraft Profile API - data about wow profile for oauth token

```python
api.get_oauth_profile('us')
```

### get_achievement
```python
CommunityMixin.get_achievement(self, region, id, **filters)
```

Achievement API

```python
api.get_achievement('us', 2144, locale='pt_BR')
```

### get_auctions
```python
CommunityMixin.get_auctions(self, region, realm_slug, **filters)
```

Auction API data status

### get_bosses
```python
CommunityMixin.get_bosses(self, region, **filters)
```

Boss API - Master list of bosses

### get_boss
```python
CommunityMixin.get_boss(self, region, id, **filters)
```

Boss API - Boss details

### get_realm_leaderboard
```python
CommunityMixin.get_realm_leaderboard(self, region, realm, **filters)
```

Challenge Mode API - realm leaderboard

### get_region_leaderboard
```python
CommunityMixin.get_region_leaderboard(self, region, **filters)
```

Challenge Mode API - region leaderboard

### get_character_profile
```python
CommunityMixin.get_character_profile(self, region, realm, character_name, **filters)
```

Character Profile API - base info or specific comma separated fields as filters

```python
api = WowApi('client-id', 'client-secret')
api.get_character_profile('eu', 'khadgar', 'patchwerk')
api.get_character_profile('eu', 'khadgar', 'patchwerk', locale='en_GB', fields='guild,mounts')
```

### get_guild_profile
```python
CommunityMixin.get_guild_profile(self, region, realm, guild_name, **filters)
```

Guild Profile API - base info or specific comma separated fields as filters

```python
api = WowApi('client-id', 'client-secret')
api.get_guild_profile('eu', 'khadgar')
api.get_guild_profile('eu', 'khadgar', locale='en_GB', fields='achievements,challenge')
```

### get_item
```python
CommunityMixin.get_item(self, region, id, **filters)
```

Item API - detail item

### get_item_set
```python
CommunityMixin.get_item_set(self, region, id, **filters)
```

Item API - detail item set

### get_mounts
```python
CommunityMixin.get_mounts(self, region, **filters)
```

Mounts API - all supported mounts

### get_pets
```python
CommunityMixin.get_pets(self, region, **filters)
```

Pets API - all supported pets

### get_pet_ability
```python
CommunityMixin.get_pet_ability(self, region, id, **filters)
```

Pets API - pet ability details

### get_pet_species
```python
CommunityMixin.get_pet_species(self, region, id, **filters)
```

Pets API - pet species details

### get_pet_stats
```python
CommunityMixin.get_pet_stats(self, region, id, **filters)
```

Pets API - pet stats details

### get_leaderboards
```python
CommunityMixin.get_leaderboards(self, region, bracket, **filters)
```

Pvp API - pvp bracket leaderboard and rbg

### get_quest
```python
CommunityMixin.get_quest(self, region, id, **filters)
```

Quest API - metadata for quests

### get_realm_status
```python
CommunityMixin.get_realm_status(self, region, **filters)
```

Realm Status API - realm status for region

### get_recipe
```python
CommunityMixin.get_recipe(self, region, id, **filters)
```

Recipe API - recipe details

### get_spell
```python
CommunityMixin.get_spell(self, region, id, **filters)
```

Spell API - spell details

### get_characters
```python
CommunityMixin.get_characters(self, region, **filters)
```

User API - List of characters of account

```python
WowApi.get_characters('us')
```

### get_zones
```python
CommunityMixin.get_zones(self, region, **filters)
```

Zone API - master list

### get_zone
```python
CommunityMixin.get_zone(self, region, id, **filters)
```

Zone API - detail zone

### get_battlegroups
```python
CommunityMixin.get_battlegroups(self, region, **filters)
```

Data Resources API - all battlegroups

### get_character_races
```python
CommunityMixin.get_character_races(self, region, **filters)
```

Data Resources API - all character races

### get_character_classes
```python
CommunityMixin.get_character_classes(self, region, **filters)
```

Data Resources API - all character classes

### get_character_achievements
```python
CommunityMixin.get_character_achievements(self, region, **filters)
```

Data Resources API - all character achievements

### get_guild_rewards
```python
CommunityMixin.get_guild_rewards(self, region, **filters)
```

Data Resources API - all guild rewards

### get_guild_perks
```python
CommunityMixin.get_guild_perks(self, region, **filters)
```

Data Resources API - all guild perks

### get_guild_achievements
```python
CommunityMixin.get_guild_achievements(self, region, **filters)
```

Data Resources API - all guild achievements

### get_item_classes
```python
CommunityMixin.get_item_classes(self, region, **filters)
```

Data Resources API - all item classes

### get_talents
```python
CommunityMixin.get_talents(self, region, **filters)
```

Data Resources API - all talents, specs and glyphs for each class

### get_pet_types
```python
CommunityMixin.get_pet_types(self, region, **filters)
```

Data Resources API - all pet types

# wowapi.mixins.game_data

## GameDataMixin
```python
GameDataMixin(self, /, *args, **kwargs)
```
All Game Data API methods
### get_achievement_category_index
```python
GameDataMixin.get_achievement_category_index(self, region, namespace, **filters)
```

Data Achievement API - Returns an index of achievement categories

### get_achievement_category
```python
GameDataMixin.get_achievement_category(self, region, namespace, id, **filters)
```

Data Achievement API - Returns an achievement category by id

### get_achievement_index
```python
GameDataMixin.get_achievement_index(self, region, namespace, **filters)
```

Data Achievement API - Returns an index of achievements

### get_achievement_data
```python
GameDataMixin.get_achievement_data(self, region, namespace, id, **filters)
```

Data Achievement API - Returns an achievement by id

### get_achievement_media
```python
GameDataMixin.get_achievement_media(self, region, namespace, id, **filters)
```

Data Achievement API - Returns media for an achievement by id

### get_azerite_essence_index
```python
GameDataMixin.get_azerite_essence_index(self, region, namespace, **filters)
```

Data Azerite Essence API - Returns an index of azerite essences

### get_azerite_essence
```python
GameDataMixin.get_azerite_essence(self, region, namespace, id, **filters)
```

Data Azerite Essence API - Returns an azerite essence by id

### get_azerite_essence_media
```python
GameDataMixin.get_azerite_essence_media(self, region, namespace, id, **filters)
```

Data Azerite Essence API - Returns media for an azerite essence by id

### get_connected_realm_index
```python
GameDataMixin.get_connected_realm_index(self, region, namespace, **filters)
```

Data Connected Realm API - Returns an index of connected realms

### get_connected_realm
```python
GameDataMixin.get_connected_realm(self, region, namespace, id, **filters)
```

Data Connected Realm API - Returns a connected realm by id

### get_creature_family_index
```python
GameDataMixin.get_creature_family_index(self, region, namespace, **filters)
```

Data Creature API - Returns an index of creature families

### get_creature_family
```python
GameDataMixin.get_creature_family(self, region, namespace, id, **filters)
```

Data Creature API - Returns a creature family by id

### get_creature_type_index
```python
GameDataMixin.get_creature_type_index(self, region, namespace, **filters)
```

Data Creature API - Returns an index of creature types

### get_creature_type
```python
GameDataMixin.get_creature_type(self, region, namespace, id, **filters)
```

Data Creature API - Returns a creature type by id

### get_creature
```python
GameDataMixin.get_creature(self, region, namespace, id, **filters)
```

Data Creature API - Returns a creature by id

### get_creature_display_media
```python
GameDataMixin.get_creature_display_media(self, region, namespace, id, **filters)
```

Data Creature API - Returns media for a creature display by id

### get_creature_family_media
```python
GameDataMixin.get_creature_family_media(self, region, namespace, id, **filters)
```

Data Creature API - Returns media for a creature family by id

### get_guild_data
```python
GameDataMixin.get_guild_data(self, region, namespace, realm_slug, guild_slug, **filters)
```

Data Guild API - Returns a single guild by its name and realm

### get_guild_achievements_data
```python
GameDataMixin.get_guild_achievements_data(self, region, namespace, realm_slug, guild_slug, **filters)
```

Data Guild API - Returns a single guild's achievements by name and realm

### get_guild_roster_data
```python
GameDataMixin.get_guild_roster_data(self, region, namespace, realm_slug, guild_slug, **filters)
```

Data Guild API - Returns a single guild's roster by its name and realm

### get_guild_crest_index
```python
GameDataMixin.get_guild_crest_index(self, region, namespace, **filters)
```

Guild Crest API - Returns an index of guild crest media

### get_guild_crest_border_media
```python
GameDataMixin.get_guild_crest_border_media(self, region, namespace, id, **filters)
```

Guild Crest API - Returns media for a guild crest border by id

### get_guild_crest_emblem_media
```python
GameDataMixin.get_guild_crest_emblem_media(self, region, namespace, id, **filters)
```

Guild Crest API - Returns media for a guild crest emblem by id

### get_item_class_index
```python
GameDataMixin.get_item_class_index(self, region, namespace, **filters)
```

Item API - Returns an index of item classes

### get_item_class
```python
GameDataMixin.get_item_class(self, region, namespace, id, **filters)
```

Item API - Returns an item class by id

### get_item_subclass
```python
GameDataMixin.get_item_subclass(self, region, namespace, class_id, subclass_id, **filters)
```

Item API - Returns an item subclass by id

### get_item_data
```python
GameDataMixin.get_item_data(self, region, namespace, id, **filters)
```

Item API - Returns an item by id

### get_item_media
```python
GameDataMixin.get_item_media(self, region, namespace, id, **filters)
```

Item API - Returns media for an item by id

### get_mythic_keystone_affixes
```python
GameDataMixin.get_mythic_keystone_affixes(self, region, namespace, **filters)
```

Mythic Keystone Affix API - get mythic keystone affixes

### get_mythic_keystone_affix
```python
GameDataMixin.get_mythic_keystone_affix(self, region, namespace, affix_id, **filters)
```

Mythic Keystone Affix API - get mythic keystone affix by id

### get_mythic_raid_leaderboard
```python
GameDataMixin.get_mythic_raid_leaderboard(self, region, namespace, raid, faction, **filters)
```

Mythic Raid Leaderboard API - get mythic raid leaderboard of specific faction

### get_mount_index
```python
GameDataMixin.get_mount_index(self, region, namespace, **filters)
```

Mount API - Returns an index of mounts

### get_mount_data
```python
GameDataMixin.get_mount_data(self, region, namespace, id, **filters)
```

Mount API - Returns a mount by id

### get_mythic_keystone_dungeon_index
```python
GameDataMixin.get_mythic_keystone_dungeon_index(self, region, namespace, **filters)
```

Mythic Keystone Dungeon API - get all mythic keystone dungeons

### get_mythic_keystone_dungeon
```python
GameDataMixin.get_mythic_keystone_dungeon(self, region, namespace, dungeon_id, **filters)
```

Mythic Keystone Dungeon API - get mythic keystone dungeon by id

### get_mythic_keystone_index
```python
GameDataMixin.get_mythic_keystone_index(self, region, namespace, **filters)
```

Mythic Keystone Dungeon API - get links to documents related to mythic keystone dungeons

### get_mythic_keystone_period_index
```python
GameDataMixin.get_mythic_keystone_period_index(self, region, namespace, **filters)
```

Mythic Keystone Dungeon API - get all mythic keystone periods

### get_mythic_keystone_period
```python
GameDataMixin.get_mythic_keystone_period(self, region, namespace, period_id, **filters)
```

Mythic Keystone Dungeon API - get mythic keystone period by id

### get_mythic_keystone_season_index
```python
GameDataMixin.get_mythic_keystone_season_index(self, region, namespace, **filters)
```

Mythic Keystone Dungeon API - get all mythic keystone seasons

### get_mythic_keystone_season
```python
GameDataMixin.get_mythic_keystone_season(self, region, namespace, season_id, **filters)
```

Mythic Keystone Dungeon API - get mythic keystone season by id

### get_mythic_keystone_leaderboard_index
```python
GameDataMixin.get_mythic_keystone_leaderboard_index(self, region, namespace, connected_realm_id, **filters)
```

Mythic Keystone Leaderboard API
Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm

### get_mythic_keystone_leaderboard
```python
GameDataMixin.get_mythic_keystone_leaderboard(self, region, namespace, connected_realm_id, dungeon_id, period, **filters)
```

Mythic Keystone Leaderboard API - get a weekly mythic keystone leaderboard by period

### get_pet_index
```python
GameDataMixin.get_pet_index(self, region, namespace, **filters)
```

Pet API - Returns an index of pets

### get_pet_data
```python
GameDataMixin.get_pet_data(self, region, namespace, id, **filters)
```

Pet API - Returns a pet by id

### get_playable_classes
```python
GameDataMixin.get_playable_classes(self, region, namespace, **filters)
```

Playable Class API - get available playable classes

### get_playable_class
```python
GameDataMixin.get_playable_class(self, region, namespace, class_id, **filters)
```

Playable Class API - get playable classes by class id

### get_playable_class_pvp_talent_slots
```python
GameDataMixin.get_playable_class_pvp_talent_slots(self, region, namespace, class_id, **filters)
```

Playable Class API - get pvp talent slots for a playable class by id

### get_playable_race_index
```python
GameDataMixin.get_playable_race_index(self, region, namespace, **filters)
```

Playable Race API - Returns an index of playable races

### get_playable_race
```python
GameDataMixin.get_playable_race(self, region, namespace, race_id, **filters)
```

Playable Race API - Returns a playable race by ID

### get_playable_specialization_index
```python
GameDataMixin.get_playable_specialization_index(self, region, namespace, **filters)
```

Playable Specialization API - get playable specializations

### get_playable_specialization
```python
GameDataMixin.get_playable_specialization(self, region, namespace, spec_id, **filters)
```

Playable Specialization API - get playable specialization by spec id

### get_power_type_index
```python
GameDataMixin.get_power_type_index(self, region, namespace, **filters)
```

Power Type API - get power types

### get_power_type
```python
GameDataMixin.get_power_type(self, region, namespace, power_type_id, **filters)
```

Power Type API - get power type by id

### get_pvp_season_index
```python
GameDataMixin.get_pvp_season_index(self, region, namespace, **filters)
```

PvP Season API - Returns an index of PvP seasons

### get_pvp_season
```python
GameDataMixin.get_pvp_season(self, region, namespace, season_id, **filters)
```

PvP Season API - Returns a PvP season by ID

### get_pvp_leaderboard_index
```python
GameDataMixin.get_pvp_leaderboard_index(self, region, namespace, season_id, **filters)
```

PvP Season API - Returns an index of PvP leaderboards for a PvP season

### get_pvp_leaderboard
```python
GameDataMixin.get_pvp_leaderboard(self, region, namespace, season_id, bracket, **filters)
```

PvP Season API - Returns the PvP leaderboard of a specific PvP bracket for a PvP season

### get_pvp_rewards_index
```python
GameDataMixin.get_pvp_rewards_index(self, region, namespace, season_id, **filters)
```

PvP Season API - Returns an index of PvP rewards for a PvP season

### get_pvp_tier_media
```python
GameDataMixin.get_pvp_tier_media(self, region, namespace, tier_id, **filters)
```

PvP Tier API - Returns media for a PvP tier by ID

### get_pvp_tier_index
```python
GameDataMixin.get_pvp_tier_index(self, region, namespace, **filters)
```

PvP Tier API - Returns an index of PvP tiers

### get_pvp_tier
```python
GameDataMixin.get_pvp_tier(self, region, namespace, tier_id, **filters)
```

PvP Tier API - Returns a PvP tier by ID

### get_realm_index
```python
GameDataMixin.get_realm_index(self, region, namespace, **filters)
```

Realm API - get realms

### get_realm
```python
GameDataMixin.get_realm(self, region, namespace, realm_slug, **filters)
```

Realm API - get realm by realm slug

### get_region_index
```python
GameDataMixin.get_region_index(self, region, namespace, **filters)
```

Region API - get regions

### get_region
```python
GameDataMixin.get_region(self, region, namespace, region_id, **filters)
```

Region API - get region by region id

### get_title_index
```python
GameDataMixin.get_title_index(self, region, namespace, **filters)
```

Title API - Returns an index of titles

### get_title
```python
GameDataMixin.get_title(self, region, namespace, id, **filters)
```

Title API - Returns a title by id

### get_token_index
```python
GameDataMixin.get_token_index(self, region, namespace, **filters)
```

WoW Token API - Returns the WoW Token index

# wowapi.mixins.profile

## ProfileMixin
```python
ProfileMixin(self, /, *args, **kwargs)
```
All Profile API methods
### get_character_achievements_summary
```python
ProfileMixin.get_character_achievements_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Achievements API
Returns a summary of the achievements a character has completed

### get_character_appearance_summary
```python
ProfileMixin.get_character_appearance_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Appearance API - Returns a summary of a character's appearance settings

### get_character_equipment_summary
```python
ProfileMixin.get_character_equipment_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Equipment API - Returns a summary of the items equipped by a character

### get_character_media_summary
```python
ProfileMixin.get_character_media_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Media API - Returns a summary of the media assets available for a character

### get_character_profile_summary
```python
ProfileMixin.get_character_profile_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Profile API - Returns a profile summary for a character

### get_character_pvp_bracket_stats
```python
ProfileMixin.get_character_pvp_bracket_stats(self, region, namespace, realm_slug, character_name, bracket, **filters)
```

Character PvP API - Returns the PvP bracket statistics for a character

### get_character_pvp_summary
```python
ProfileMixin.get_character_pvp_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character PvP API - Returns a PvP summary for a character

### get_character_specializations_summary
```python
ProfileMixin.get_character_specializations_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Specializations API - Returns a summary of a character's specializations

### get_character_stats_summary
```python
ProfileMixin.get_character_stats_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Statistics API - Returns a statistics summary for a character

### get_character_titles_summary
```python
ProfileMixin.get_character_titles_summary(self, region, namespace, realm_slug, character_name, **filters)
```

Character Titles API - Returns a summary of titles a character has obtained

### get_character_mythic_keystone_profile
```python
ProfileMixin.get_character_mythic_keystone_profile(self, region, namespace, realm_slug, character_name, **filters)
```

Profile API - Mythic Keystone Character Profile Index

### get_character_mythic_keystone_profile_season
```python
ProfileMixin.get_character_mythic_keystone_profile_season(self, region, namespace, realm_slug, character_name, season_id, **filters)
```

Profile API - Returns the Mythic Keystone season details for a character

