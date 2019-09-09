import copy
from datetime import datetime, timedelta

from wowapi import WowApi


class TestGameDataMixin:

    def setup(self):
        self.params = {'access_token': 'secret'}

        self.api = WowApi('client-id', 'client-secret')
        self.api._access_tokens = {
            'us': {
                'token': 'secret',
                'expiration': datetime.utcnow() + timedelta(hours=1)
            }
        }

    # Achievement API

    def test_get_achievement_category_index(self, response_mock):
        self.api.get_achievement_category_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/achievement-category/index', params=params)

    def test_get_achievement_category(self, response_mock):
        self.api.get_achievement_category('us', 'dynamic-us', 81)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/achievement-category/81', params=params)

    def test_get_achievement_index(self, response_mock):
        self.api.get_achievement_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/achievement/index', params=params)

    def test_get_achievement_data(self, response_mock):
        self.api.get_achievement_data('us', 'dynamic-us', 6)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/achievement/6', params=params)

    def test_get_achievement_media(self, response_mock):
        self.api.get_achievement_media('us', 'dynamic-us', 6)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/achievement/6', params=params)

    # Azerite Essence API

    def test_get_azerite_essence_index(self, response_mock):
        self.api.get_azerite_essence_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/azerite-essence/index', params=params)

    def test_get_azerite_essence(self, response_mock):
        self.api.get_azerite_essence('us', 'dynamic-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/azerite-essence/2', params=params)

    def test_get_azerite_essence_media(self, response_mock):
        self.api.get_azerite_essence_media('us', 'dynamic-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/azerite-essence/2', params=params)

    # Connected Realm API

    def test_get_connected_realm_index(self, response_mock):
        self.api.get_connected_realm_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/index', params=params)

    def test_get_connected_realm(self, response_mock):
        self.api.get_connected_realm('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1', params=params)

    # Creature API

    def test_get_creature_family_index(self, response_mock):
        self.api.get_creature_family_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/creature-family/index', params=params)

    def test_get_creature_family(self, response_mock):
        self.api.get_creature_family('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/creature-family/1', params=params)

    def test_get_creature_type_index(self, response_mock):
        self.api.get_creature_type_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/creature-type/index', params=params)

    def test_get_creature_type(self, response_mock):
        self.api.get_creature_type('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/creature-type/1', params=params)

    def test_get_creature(self, response_mock):
        self.api.get_creature('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/creature/1', params=params)

    def test_get_creature_display_media(self, response_mock):
        self.api.get_creature_display_media('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/creature-display/1', params=params)

    def test_get_creature_family_media(self, response_mock):
        self.api.get_creature_family_media('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/creature-family/1', params=params)

    # Guild API

    def test_get_guild_data(self, response_mock):
        self.api.get_guild_data('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild', params=params)

    def test_get_guild_achievements_data(self, response_mock):
        self.api.get_guild_achievements_data('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/achievements',
            params=params
        )

    def test_get_guild_roster_data(self, response_mock):
        self.api.get_guild_roster_data('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/roster', params=params)

    # Guild Crest API

    def test_get_guild_crest_index(self, response_mock):
        self.api.get_guild_crest_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild-crest/index', params=params)

    def test_get_guild_crest_border_media(self, response_mock):
        self.api.get_guild_crest_border_media('us', 'dynamic-us', 0)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/guild-crest/border/0', params=params)

    def test_get_guild_crest_emblem_media(self, response_mock):
        self.api.get_guild_crest_emblem_media('us', 'dynamic-us', 0)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/guild-crest/emblem/0', params=params)

    # Item API

    def test_get_item_class_index(self, response_mock):
        self.api.get_item_class_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/item-class/index', params=params)

    def test_get_item_class(self, response_mock):
        self.api.get_item_class('us', 'dynamic-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/item-class/2', params=params)

    def test_get_item_subclass(self, response_mock):
        self.api.get_item_subclass('us', 'dynamic-us', 2, 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/item-class/2/item-subclass/1', params=params)

    def test_get_item_data(self, response_mock):
        self.api.get_item_data('us', 'dynamic-us', 9999)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/item/9999', params=params)

    def test_get_item_media(self, response_mock):
        self.api.get_item_media('us', 'dynamic-us', 9999)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/item/9999', params=params)

    # Mythic Keystone Affix API

    def test_get_mythic_keystone_affixes(self, response_mock):
        self.api.get_mythic_keystone_affixes('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/keystone-affix/index', params=params)

    def test_get_mythic_keystone_affix(self, response_mock):
        self.api.get_mythic_keystone_affix('us', 'dynamic-us', 3)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/keystone-affix/3', params=params)

    # Mythic Raid Leaderboard API

    def test_get_mythic_raid_leaderboard(self, response_mock):
        self.api.get_mythic_raid_leaderboard('us', 'dynamic-us', 'uldir', 'horde')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/leaderboard/hall-of-fame/uldir/horde',
            params=params
        )

    # Mount API

    def test_get_mount_index(self, response_mock):
        self.api.get_mount_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mount/index',
            params=params
        )

    def test_get_mount_data(self, response_mock):
        self.api.get_mount_data('us', 'dynamic-us', 6)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mount/6',
            params=params
        )

    # Mythic Keystone Dungeon API

    def test_get_mythic_keystone_dungeon_index(self, response_mock):
        self.api.get_mythic_keystone_dungeon_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index', params=params)

    def test_get_mythic_keystone_dungeon(self, response_mock):
        self.api.get_mythic_keystone_dungeon('us', 'dynamic-us', 5)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/5', params=params)

    def test_get_mythic_keystone_index(self, response_mock):
        self.api.get_mythic_keystone_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/index', params=params)

    def test_get_mythic_keystone_period_index(self, response_mock):
        self.api.get_mythic_keystone_period_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/period/index', params=params)

    def test_get_mythic_keystone_period(self, response_mock):
        self.api.get_mythic_keystone_period('us', 'dynamic-us', 641)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/period/641', params=params)

    def test_get_mythic_keystone_season_index(self, response_mock):
        self.api.get_mythic_keystone_season_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/season/index', params=params)

    def test_get_mythic_keystone_season(self, response_mock):
        self.api.get_mythic_keystone_season('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/season/1', params=params)

    # Mythic Keystone Leaderboard API

    def test_get_mythic_keystone_leaderboard_index(self, response_mock):
        self.api.get_mythic_keystone_leaderboard_index('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/index',
            params=params
        )

    def test_get_mythic_keystone_leaderboard(self, response_mock):
        self.api.get_mythic_keystone_leaderboard('us', 'dynamic-us', 1, 2, 3)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/2/period/3',
            params=params
        )

    # Pet API

    def test_get_pet_index(self, response_mock):
        self.api.get_pet_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pet/index',
            params=params
        )

    def test_get_pet_data(self, response_mock):
        self.api.get_pet_data('us', 'dynamic-us', 39)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pet/39',
            params=params
        )

    # Playable Class API

    def test_get_playable_classes(self, response_mock):
        self.api.get_playable_classes('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-class/index',
            params=params
        )

    def test_get_playable_class(self, response_mock):
        self.api.get_playable_class('us', 'static-us', 7)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-class/7',
            params=params
        )

    def test_get_playable_class_pvp_talent_slots(self, response_mock):
        self.api.get_playable_class_pvp_talent_slots('us', 'static-us', 7)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-class/7/pvp-talent-slots',
            params=params
        )

    # Playable Race API

    def test_get_playable_race_index(self, response_mock):
        self.api.get_playable_race_index('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-race/index',
            params=params
        )

    def test_get_playable_race(self, response_mock):
        self.api.get_playable_race('us', 'static-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-race/2',
            params=params
        )

    # Playable Specialization API

    def test_get_playable_specialization_index(self, response_mock):
        self.api.get_playable_specialization_index('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-specialization/index',
            params=params
        )

    def test_get_playable_specialization(self, response_mock):
        self.api.get_playable_specialization('us', 'static-us', 262)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-specialization/262',
            params=params
        )

    # Power Type API

    def test_get_power_type_index(self, response_mock):
        self.api.get_power_type_index('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/power-type/index',
            params=params
        )

    def test_get_power_type(self, response_mock):
        self.api.get_power_type('us', 'static-us', 0)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/power-type/0',
            params=params
        )

    # PvP Season API

    def test_get_pvp_season_index(self, response_mock):
        self.api.get_pvp_season_index('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-season/index',
            params=params
        )

    def test_get_pvp_season(self, response_mock):
        self.api.get_pvp_season('us', 'static-us', 27)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-season/27',
            params=params
        )

    def test_get_pvp_leaderboard_index(self, response_mock):
        self.api.get_pvp_leaderboard_index('us', 'static-us', 27)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-leaderboard/index',
            params=params
        )

    def test_get_pvp_leaderboard(self, response_mock):
        self.api.get_pvp_leaderboard('us', 'static-us', 27, '3v3')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-leaderboard/3v3',
            params=params
        )

    def test_get_pvp_rewards_index(self, response_mock):
        self.api.get_pvp_rewards_index('us', 'static-us', 27)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-reward/index',
            params=params
        )

    # PvP Tier API

    def test_get_pvp_tier_media(self, response_mock):
        self.api.get_pvp_tier_media('us', 'static-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/pvp-tier/1',
            params=params
        )

    def test_get_pvp_tier_index(self, response_mock):
        self.api.get_pvp_tier_index('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-tier/index',
            params=params
        )

    def test_get_pvp_tier(self, response_mock):
        self.api.get_pvp_tier('us', 'static-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-tier/1',
            params=params
        )

    # Realm API

    def test_get_realm_index(self, response_mock):
        self.api.get_realm_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/realm/index',
            params=params
        )

    def test_get_realm(self, response_mock):
        self.api.get_realm('us', 'dynamic-us', 'tichondrius')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/realm/tichondrius',
            params=params
        )

    # Region API

    def test_get_region_index(self, response_mock):
        self.api.get_region_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/region/index',
            params=params
        )

    def test_get_region(self, response_mock):
        self.api.get_region('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/region/1',
            params=params
        )

    # Title API

    def test_get_title_index(self, response_mock):
        self.api.get_title_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/title/index',
            params=params
        )

    def test_get_title(self, response_mock):
        self.api.get_title('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/title/1',
            params=params
        )

    # WoW Token API

    def test_get_token_index(self, response_mock):
        self.api.get_token_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/token/index', params=params)
