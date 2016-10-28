import os

import pytest
import requests
from requests.exceptions import RequestException

from wowapi import WowApi, WowApiException, WowApiConfigException


class TestWowApi(object):

    def setup(self):
        os.environ['WOWAPI_APIKEY'] = 'foo'

        self.response_mock = requests.models.Response()
        self.response_mock.status_code = 200
        self.response_mock._content = b'{}'

        self.params = {'apikey': 'foo'}

    def test_get_resource_wrong_region_arg(self):
        with pytest.raises(WowApiConfigException) as exc:
            WowApi.get_resource('foo/', 'za')

        assert "Region 'za' not a valid region" in str(exc)

    def test_get_resource_no_api_key(self):
        del os.environ['WOWAPI_APIKEY']

        with pytest.raises(WowApiConfigException) as exc:
            WowApi.get_resource('foo/', 'us')

        assert "WOWAPI_APIKEY is missing from your env variables" in str(exc)

    def test_get_resource_requests_exception(self, request_exception_mock):
        with pytest.raises(RequestException) as exc:
            WowApi.get_resource('foo/', 'us')

        assert 'Problem' in str(exc)

    def test_get_resource_json_invalid(self, invalid_json_mock):
        with pytest.raises(WowApiException) as exc:
            WowApi.get_resource('foo/', 'us')

        assert 'Invalid Json' in str(exc)

    def test_get_resource_response_404(self, get_404_mock):
        with pytest.raises(WowApiException) as exc:
            WowApi.get_resource('foo/', 'us')

        assert 'https://us.api.battle.net/wow/foo/ - 404' in str(exc)

    def get_resource_with_filters(self, get_mock):
        WowApi.get_resource('foo/{0}', 'us', 1, locale='en_US', fields='pets,stats', breedId=9999)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/foo/1/',
            params={
                'apikey': 'foo',
                'locale': 'en_US',
                'fields': 'pets,stats',
                'breedId': 9999
            }
        )

    # tests for endpoints

    def test_get_achievement(self, get_mock):
        WowApi.get_achievement('us', 1234)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/achievement/1234', params=self.params)

    def test_get_auctions(self, get_mock):
        WowApi.get_auctions('us', 'khadgar')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/auction/data/khadgar', params=self.params)

    def test_get_bosses(self, get_mock):
        WowApi.get_bosses('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/boss/', params=self.params)

    def test_get_boss(self, get_mock):
        WowApi.get_boss('us', 24723)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/boss/24723', params=self.params)

    def test_get_realm_leaderboard(self, get_mock):
        WowApi.get_realm_leaderboard('us', 'silvermoon')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/challenge/silvermoon', params=self.params)

    def test_get_region_leaderboard(self, get_mock):
        WowApi.get_region_leaderboard('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/challenge/region', params=self.params)

    def test_get_character_profile(self, get_mock):
        WowApi.get_character_profile('eu', 'khadgar', 'patchwerk')
        get_mock.assert_called_with(
            'https://eu.api.battle.net/wow/character/khadgar/patchwerk', params=self.params)

    def test_get_guild_profile(self, get_mock):
        WowApi.get_guild_profile('eu', 'draenor', 'topguild')
        get_mock.assert_called_with(
            'https://eu.api.battle.net/wow/guild/draenor/topguild', params=self.params)

    def test_get_item(self, get_mock):
        WowApi.get_item('us', 9999)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/item/9999', params=self.params)

    def test_get_item_set(self, get_mock):
        WowApi.get_item_set('us', 1060)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/item/set/1060', params=self.params)

    def test_get_mounts(self, get_mock):
        WowApi.get_mounts('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/mount/', params=self.params)

    def test_get_pets(self, get_mock):
        WowApi.get_pets('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/pet/', params=self.params)

    def test_get_pet_ability(self, get_mock):
        WowApi.get_pet_ability('us', 640)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/pet/ability/640', params=self.params)

    def test_get_pet_species(self, get_mock):
        WowApi.get_pet_species('us', 258)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/pet/species/258', params=self.params)

    def test_get_pet_stats(self, get_mock):
        WowApi.get_pet_stats('eu', 258)
        get_mock.assert_called_with(
            'https://eu.api.battle.net/wow/pet/stats/258', params=self.params)

    def test_get_leaderboards(self, get_mock):
        WowApi.get_leaderboards('us', '5v5')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/leaderboard/5v5', params=self.params)

    def test_get_quest(self, get_mock):
        WowApi.get_quest('us', 13146)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/quest/13146', params=self.params)

    def test_get_realm_status(self, get_mock):
        WowApi.get_realm_status('kr')
        get_mock.assert_called_with(
            'https://kr.api.battle.net/wow/realm/status', params=self.params)

    def test_get_recipe(self, get_mock):
        WowApi.get_recipe('us', 33994)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/recipe/33994', params=self.params)

    def test_get_spell(self, get_mock):
        WowApi.get_spell('us', 8056)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/spell/8056', params=self.params)

    def test_get_zones(self, get_mock):
        WowApi.get_zones('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/zone/', params=self.params)

    def test_get_zone(self, get_mock):
        WowApi.get_zone('us', 4131)
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/zone/4131', params=self.params)

    def test_get_battlegroups(self, get_mock):
        WowApi.get_battlegroups('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/battlegroups/', params=self.params)

    def test_get_character_races(self, get_mock):
        WowApi.get_character_races('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/character/races', params=self.params)

    def test_get_character_classes(self, get_mock):
        WowApi.get_character_classes('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/character/classes', params=self.params)

    def test_get_character_achievements(self, get_mock):
        WowApi.get_character_achievements('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/character/achievements', params=self.params)

    def test_get_guild_rewards(self, get_mock):
        WowApi.get_guild_rewards('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/guild/rewards', params=self.params)

    def test_get_guild_perks(self, get_mock):
        WowApi.get_guild_perks('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/guild/perks', params=self.params)

    def test_get_guild_achievements(self, get_mock):
        WowApi.get_guild_achievements('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/guild/achievements', params=self.params)

    def test_get_item_classes(self, get_mock):
        WowApi.get_item_classes('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/item/classes', params=self.params)

    def test_get_talents(self, get_mock):
        WowApi.get_talents('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/talents', params=self.params)

    def test_get_pet_types(self, get_mock):
        WowApi.get_pet_types('us')
        get_mock.assert_called_with(
            'https://us.api.battle.net/wow/data/pet/types', params=self.params)
