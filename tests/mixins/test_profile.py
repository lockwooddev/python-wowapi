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

    # Character Achievements API

    def test_get_character_achievements_summary(self, response_mock):
        self.api.get_character_achievements_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/achievements',
            params=params
        )

    # Character Appearance API

    def test_get_character_appearance_summary(self, response_mock):
        self.api.get_character_appearance_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/appearance',
            params=params
        )

    # Character Equipment API

    def test_get_character_equipment_summary(self, response_mock):
        self.api.get_character_equipment_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/equipment',
            params=params
        )

    # Character Media API

    def test_get_character_media_summary(self, response_mock):
        self.api.get_character_media_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/character-media',
            params=params
        )

    # Character Profile API

    def test_get_character_profile_summary(self, response_mock):
        self.api.get_character_profile_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower',
            params=params
        )

    # Character PvP API

    def test_get_character_pvp_bracket_stats(self, response_mock):
        self.api.get_character_pvp_bracket_stats(
            'us', 'dynamic-us', 'khadgar', 'blizzpower', '3v3'
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/pvp-bracket/3v3',
            params=params
        )

    def test_get_character_pvp_summary(self, response_mock):
        self.api.get_character_pvp_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/pvp-summary',
            params=params
        )

    # Character Specializations API

    def test_get_character_specializations_summary(self, response_mock):
        self.api.get_character_specializations_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/specializations',
            params=params
        )

    # Character Statistics API

    def test_get_character_stats_summary(self, response_mock):
        self.api.get_character_stats_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/statistics',
            params=params
        )

    # Character Titles API

    def test_get_character_titles_summary(self, response_mock):
        self.api.get_character_titles_summary(
            'us', 'dynamic-us', 'khadgar', 'blizzpower',
        )
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/character/khadgar/blizzpower/titles',
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
