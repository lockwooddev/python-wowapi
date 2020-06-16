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

    # Auction House API

    def test_get_auctions(self, response_mock):
        self.api.get_auctions('us', 'dynamic-us', 1146)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1146/auctions', params=params)

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

    def test_get_item_set_index(self, response_mock):
        self.api.get_item_set_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/item-set/index', params=params)

    def test_get_item_set(self, response_mock):
        self.api.get_item_set('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/item-set/1', params=params)

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

    # Journal API

    def test_get_journal_index(self, response_mock):
        self.api.get_journal_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/journal-expansion/index', params=params)

    def test_get_journal_expansion(self, response_mock):
        self.api.get_journal_expansion('us', 'dynamic-us', 68)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/journal-expansion/68', params=params)

    def test_get_journal_encounter_index(self, response_mock):
        self.api.get_journal_encounter_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/journal-encounter/index', params=params)

    def test_get_journal_encounter(self, response_mock):
        self.api.get_journal_encounter('us', 'dynamic-us', 89)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/journal-encounter/89', params=params)

    def test_get_journal_instance_index(self, response_mock):
        self.api.get_journal_instance_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/journal-instance/index', params=params)

    def test_get_journal_instance(self, response_mock):
        self.api.get_journal_instance('us', 'dynamic-us', 63)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/journal-instance/63', params=params)

    def test_get_journal_instance_media(self, response_mock):
        self.api.get_journal_instance_media('us', 'dynamic-us', 63)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/journal-instance/63', params=params)

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

    def test_get_mythic_keystone_affix_media(self, response_mock):
        self.api.get_mythic_keystone_affix_media('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/keystone-affix/1', params=params)

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

    # Mythic Raid Leaderboard API

    def test_get_mythic_raid_leaderboard(self, response_mock):
        self.api.get_mythic_raid_leaderboard('us', 'dynamic-us', 'uldir', 'horde')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/leaderboard/hall-of-fame/uldir/horde',
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

    def test_get_playable_class_index(self, response_mock):
        self.api.get_playable_class_index('us', 'static-us')
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

    def test_get_playable_class_media(self, response_mock):
        self.api.get_playable_class_media('us', 'static-us', 7)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/playable-class/7',
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

    def test_get_playable_specialization_media(self, response_mock):
        self.api.get_playable_specialization_media('us', 'static-us', 262)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/playable-specialization/262',
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

    # Profession API

    def test_get_profession_index(self, response_mock):
        self.api.get_profession_index('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/profession/index',
            params=params
        )

    def test_get_profession(self, response_mock):
        self.api.get_profession('us', 'static-us', 164)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/profession/164',
            params=params
        )

    def test_get_profession_media(self, response_mock):
        self.api.get_profession_media('us', 'static-us', 164)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/profession/164',
            params=params
        )

    def test_get_profession_skill_tier(self, response_mock):
        self.api.get_profession_skill_tier('us', 'static-us', 164, 2477)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/profession/164/skill-tier/2477',
            params=params
        )

    def test_get_recipe(self, response_mock):
        self.api.get_recipe('us', 'static-us', 1631)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/recipe/1631',
            params=params
        )

    def test_get_recipe_media(self, response_mock):
        self.api.get_recipe_media('us', 'static-us', 1631)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/recipe/1631',
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

    # Quest API

    def test_get_quest_index(self, response_mock):
        self.api.get_quest_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/index',
            params=params
        )

    def test_get_quest(self, response_mock):
        self.api.get_quest('us', 'dynamic-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/2',
            params=params
        )

    def test_get_quest_categories_index(self, response_mock):
        self.api.get_quest_categories_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/category/index',
            params=params
        )

    def test_get_quest_catagory(self, response_mock):
        self.api.get_quest_catagory('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/category/1',
            params=params
        )

    def test_get_quest_area_index(self, response_mock):
        self.api.get_quest_area_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/area/index',
            params=params
        )

    def test_get_quest_area(self, response_mock):
        self.api.get_quest_area('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/area/1',
            params=params
        )

    def test_get_quest_types_index(self, response_mock):
        self.api.get_quest_types_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/type/index',
            params=params
        )

    def test_get_quest_type(self, response_mock):
        self.api.get_quest_type('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/quest/type/1',
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

    # Reputations API

    def test_get_reputation_faction_index(self, response_mock):
        self.api.get_reputation_faction_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/reputation-faction/index',
            params=params
        )

    def test_get_reputation_faction(self, response_mock):
        self.api.get_reputation_faction('us', 'dynamic-us', 21)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/reputation-faction/21',
            params=params
        )

    def test_get_reputation_tier_index(self, response_mock):
        self.api.get_reputation_tier_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/reputation-tiers/index',
            params=params
        )

    def test_get_reputation_tier(self, response_mock):
        self.api.get_reputation_tier('us', 'dynamic-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/reputation-tiers/2',
            params=params
        )

    # Spell API

    def test_get_spell(self, response_mock):
        self.api.get_spell('us', 'dynamic-us', 196607)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/spell/196607', params=params
        )

    def test_get_spell_media(self, response_mock):
        self.api.get_spell_media('us', 'dynamic-us', 196607)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/media/spell/196607', params=params
        )

    # Talent API

    def test_get_talent_index(self, response_mock):
        self.api.get_talent_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/talent/index', params=params
        )

    def test_get_talent(self, response_mock):
        self.api.get_talent('us', 'dynamic-us', 23106)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/talent/23106', params=params
        )

    def test_get_pvp_talent_index(self, response_mock):
        self.api.get_pvp_talent_index('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-talent/index', params=params
        )

    def test_get_pvp_talent(self, response_mock):
        self.api.get_pvp_talent('us', 'dynamic-us', 3)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/pvp-talent/3', params=params
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
