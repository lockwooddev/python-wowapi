import copy
from datetime import datetime, timedelta

from wowapi import WowApi


class TestCommunityMixin:

    def setup(self):
        self.params = {'access_token': 'secret'}

        self.api = WowApi('client-id', 'client-secret')
        self.api._access_tokens = {
            'us': {
                'token': 'secret',
                'expiration': datetime.utcnow() + timedelta(hours=1)
            }
        }

    def test_get_oauth_profile(self, response_mock):
        self.api.get_oauth_profile('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/user/characters', params=self.params)

    def test_get_achievement(self, response_mock):
        self.api.get_achievement('us', 1234)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/achievement/1234', params=self.params)

    def test_get_auctions(self, response_mock):
        self.api.get_auctions('us', 'khadgar')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/auction/data/khadgar', params=self.params)

    def test_get_bosses(self, response_mock):
        self.api.get_bosses('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/boss/', params=self.params)

    def test_get_boss(self, response_mock):
        self.api.get_boss('us', 24723)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/boss/24723', params=self.params)

    def test_get_realm_leaderboard(self, response_mock):
        self.api.get_realm_leaderboard('us', 'silvermoon')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/challenge/silvermoon', params=self.params)

    def test_get_region_leaderboard(self, response_mock):
        self.api.get_region_leaderboard('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/challenge/region', params=self.params)

    def test_get_character_profile(self, response_mock):
        self.api.get_character_profile('us', 'khadgar', 'patchwerk')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/character/khadgar/patchwerk', params=self.params)

    def test_get_guild_profile(self, response_mock):
        self.api.get_guild_profile('us', 'draenor', 'topguild')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/guild/draenor/topguild', params=self.params)

    def test_get_item(self, response_mock):
        self.api.get_item('us', 9999)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/item/9999', params=self.params)

    def test_get_item_set(self, response_mock):
        self.api.get_item_set('us', 1060)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/item/set/1060', params=self.params)

    def test_get_mounts(self, response_mock):
        self.api.get_mounts('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/mount/', params=self.params)

    def test_get_pets(self, response_mock):
        self.api.get_pets('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/', params=self.params)

    def test_get_pet_ability(self, response_mock):
        self.api.get_pet_ability('us', 640)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/ability/640', params=self.params)

    def test_get_pet_species(self, response_mock):
        self.api.get_pet_species('us', 258)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/species/258', params=self.params)

    def test_get_pet_stats(self, response_mock):
        self.api.get_pet_stats('us', 258)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/stats/258', params=self.params)

    def test_get_leaderboards(self, response_mock):
        self.api.get_leaderboards('us', '5v5')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/leaderboard/5v5', params=self.params)

    def test_get_quest(self, response_mock):
        self.api.get_quest('us', 13146)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/quest/13146', params=self.params)

    def test_get_realm_status(self, response_mock):
        self.api.get_realm_status('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/realm/status', params=self.params)

    def test_get_recipe(self, response_mock):
        self.api.get_recipe('us', 33994)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/recipe/33994', params=self.params)

    def test_get_spell(self, response_mock):
        self.api.get_spell('us', 8056)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/spell/8056', params=self.params)

    def test_get_characters(self, response_mock):
        params = copy.deepcopy(self.params)
        params['locale'] = 'de_DE'
        self.api.get_characters('us', locale='de_DE')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/user/characters', params=params)

    def test_get_zones(self, response_mock):
        self.api.get_zones('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/zone/', params=self.params)

    def test_get_zone(self, response_mock):
        self.api.get_zone('us', 4131)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/zone/4131', params=self.params)

    def test_get_battlegroups(self, response_mock):
        self.api.get_battlegroups('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/battlegroups/', params=self.params)

    def test_get_character_races(self, response_mock):
        self.api.get_character_races('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/character/races', params=self.params)

    def test_get_character_classes(self, response_mock):
        self.api.get_character_classes('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/character/classes', params=self.params)

    def test_get_character_achievements(self, response_mock):
        self.api.get_character_achievements('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/character/achievements', params=self.params)

    def test_get_guild_rewards(self, response_mock):
        self.api.get_guild_rewards('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/guild/rewards', params=self.params)

    def test_get_guild_perks(self, response_mock):
        self.api.get_guild_perks('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/guild/perks', params=self.params)

    def test_get_guild_achievements(self, response_mock):
        self.api.get_guild_achievements('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/guild/achievements', params=self.params)

    def test_get_item_classes(self, response_mock):
        self.api.get_item_classes('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/item/classes', params=self.params)

    def test_get_talents(self, response_mock):
        self.api.get_talents('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/talents', params=self.params)

    def test_get_pet_types(self, response_mock):
        self.api.get_pet_types('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/pet/types', params=self.params)
