import copy
from datetime import datetime, timedelta

from wowapi import WowApi


class TestProfileMixin(object):

    def setup(self):
        self.params = {'access_token': 'secret'}

        self.api = WowApi('client-id', 'client-secret')
        self.api._access_tokens = {
            'us': {
                'token': 'secret',
                'expiration': datetime.utcnow() + timedelta(hours=1)
            }
        }

    # Account Profile API

    def test_get_account_profile_summary(self, response_mock):
        self.api.get_account_profile_summary(
            'us', 'dynamic-us', 'profile-token'
        )

        params = {
            'namespace': 'dynamic-us',
            'access_token': 'profile-token'
        }

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/user/wow',
            params=params
        )

    def test_get_protected_character_profile_summary(self, response_mock):
        self.api.get_protected_character_profile_summary(
            'us', 'dynamic-us', 'profile-token', 1, 9000
        )

        params = {
            'namespace': 'dynamic-us',
            'access_token': 'profile-token'
        }

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/user/wow/protected-character/1-9000',
            params=params
        )

    def test_get_account_collection_index(self, response_mock):
        self.api.get_account_collection_index('us', 'dynamic-us', 'profile-token')

        params = {
            'namespace': 'dynamic-us',
            'access_token': 'profile-token'
        }

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/user/wow/collections',
            params=params
        )

    def test_get_mount_collection_summary(self, response_mock):
        self.api.get_mount_collection_summary('us', 'dynamic-us', 'profile-token')

        params = {
            'namespace': 'dynamic-us',
            'access_token': 'profile-token'
        }

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/user/wow/collections/mounts',
            params=params
        )

    def test_get_pet_collection_summary(self, response_mock):
        self.api.get_pet_collection_summary('us', 'dynamic-us', 'profile-token')

        params = {
            'namespace': 'dynamic-us',
            'access_token': 'profile-token'
        }

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/user/wow/collections/pets',
            params=params
        )

    # Character Achievements API

    def test_get_character_achievements_summary(self, response_mock):
        self.api.get_character_achievements_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/achievements',
            params=params
        )

    def test_get_character_achievements_statistics(self, response_mock):
        self.api.get_character_achievements_statistics(
            'us', 'dynamic-us', 'moon', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/moon/asmon/achievements/statistics',
            params=params
        )

    # Character Appearance API

    def test_get_character_appearance_summary(self, response_mock):
        self.api.get_character_appearance_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/appearance',
            params=params
        )

    # Character Collections API

    def test_get_character_collection_index(self, response_mock):
        self.api.get_character_collection_index('us', 'dynamic-us', 'khadgar', 'asmon')

        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/collections',
            params=params
        )

    def test_get_character_mount_collection_index(self, response_mock):
        self.api.get_character_mount_collection_index('us', 'dynamic-us', 'khadgar', 'asmon')

        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/collections/mounts',
            params=params
        )

    def test_get_character_pet_collection_index(self, response_mock):
        self.api.get_character_pet_collection_index('us', 'dynamic-us', 'khadgar', 'asmon')

        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/collections/pets',
            params=params
        )

    # Character Encounters API

    def test_get_character_encounters_summary(self, response_mock):
        self.api.get_character_encounters_summary('us', 'dynamic-us', 'khadgar', 'asmon')

        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/encounters',
            params=params
        )

    def test_get_character_dungeons(self, response_mock):
        self.api.get_character_dungeons('us', 'dynamic-us', 'khadgar', 'asmon')

        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/encounters/dungeons',
            params=params
        )

    def test_get_character_raids(self, response_mock):
        self.api.get_character_raids('us', 'dynamic-us', 'khadgar', 'asmon')

        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/encounters/raids',
            params=params
        )

    # Character Equipment API

    def test_get_character_equipment_summary(self, response_mock):
        self.api.get_character_equipment_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/equipment',
            params=params
        )

    # Character Hunter Pets API

    def test_get_character_hunter_pets_summary(self, response_mock):
        self.api.get_character_hunter_pets_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/hunter-pets',
            params=params
        )

    # Character Media API

    def test_get_character_media_summary(self, response_mock):
        self.api.get_character_media_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/character-media',
            params=params
        )

    # WoW Mythic Keystone Character Profile API

    def test_get_character_mythic_keystone_profile(self, response_mock):
        self.api.get_character_mythic_keystone_profile(
            'us', 'profile-us', 'blackmoore', 'ayanda'
        )

        params = copy.deepcopy(self.params)
        params['namespace'] = 'profile-us'

        response_mock.assert_called_with(
            '{0}/profile/wow/character/blackmoore/ayanda/mythic-keystone-profile'.format(
                'https://us.api.blizzard.com'
            ),
            params=params)

    def test_get_character_mythic_keystone_profile_season(self, response_mock):
        self.api.get_character_mythic_keystone_profile_season(
            'us', 'profile-us', 'blackmoore', 'ayanda',  '1'
        )

        params = copy.deepcopy(self.params)
        params['namespace'] = 'profile-us'

        response_mock.assert_called_with(
            '{0}/profile/wow/character/blackmoore/ayanda/mythic-keystone-profile/season/1'.format(
                'https://us.api.blizzard.com'
            ),
            params=params
        )

    # Character Professions API

    def test_get_character_professions_summary(self, response_mock):
        self.api.get_character_professions_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/professions',
            params=params
        )

    # Character Profile API

    def test_get_character_profile_summary(self, response_mock):
        self.api.get_character_profile_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon',
            params=params
        )

    def test_get_character_profile_status(self, response_mock):
        self.api.get_character_profile_status(
            'us', 'dynamic-us', 'khadgar', 'asmon'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/status',
            params=params
        )

    # Character PvP API

    def test_get_character_pvp_bracket_stats(self, response_mock):
        self.api.get_character_pvp_bracket_stats(
            'us', 'dynamic-us', 'khadgar', 'asmon', '3v3'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/pvp-bracket/3v3',
            params=params
        )

    def test_get_character_pvp_summary(self, response_mock):
        self.api.get_character_pvp_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/pvp-summary',
            params=params
        )

    # Character Quests API

    def test_get_character_quests(self, response_mock):
        self.api.get_character_quests(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/quests',
            params=params
        )

    def test_get_character_completed_quests(self, response_mock):
        self.api.get_character_completed_quests(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/quests/completed',
            params=params
        )

    # Character Reputations API

    def test_get_character_reputations_summary(self, response_mock):
        self.api.get_character_reputations_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/reputations',
            params=params
        )

    # Character Specializations API

    def test_get_character_specializations_summary(self, response_mock):
        self.api.get_character_specializations_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/specializations',
            params=params
        )

    # Character Statistics API

    def test_get_character_stats_summary(self, response_mock):
        self.api.get_character_stats_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/statistics',
            params=params
        )

    # Character Titles API

    def test_get_character_titles_summary(self, response_mock):
        self.api.get_character_titles_summary(
            'us', 'dynamic-us', 'khadgar', 'asmon',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/titles',
            params=params
        )

    # Guild API

    def test_get_guild(self, response_mock):
        self.api.get_guild('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild', params=params)

    def test_get_guild_activity(self, response_mock):
        self.api.get_guild_activity('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/activity',
            params=params
        )

    def test_get_guild_achievements(self, response_mock):
        self.api.get_guild_achievements('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/achievements',
            params=params
        )

    def test_get_guild_roster(self, response_mock):
        self.api.get_guild_roster('us', 'dynamic-us', 'khadgar', 'bestguild')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/roster', params=params)
