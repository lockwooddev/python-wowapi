from datetime import datetime, timedelta

import pytest
from requests.exceptions import RequestException

from wowapi import WowApi, WowApiException
from .fixtures import ResponseMock


class TestWowApi(object):

    def setup(self):
        self.params = {'access_token': '987'}

        self.api = WowApi('client-id', 'client-secret')

        self.authorized_api = WowApi('client-id', 'client-secret')
        self.authorized_api._access_token = self.params['access_token']
        self.authorized_api._access_token_expiration = datetime.utcnow() + timedelta(hours=1)

        self.test_url = 'http://example.com'

    def test_instance(self):
        assert not self.api._access_token
        assert not self.api._access_token_expiration

    def test_handle_request_success(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{}')
        data = self.api._handle_request(self.test_url)
        assert data == {}
        session_get_mock.assert_called_with(self.test_url)

    def test_handle_request_request_exception(self, session_get_mock):
        session_get_mock.side_effect = RequestException('Error')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert 'Error' in str(exc)

    def test_handle_request_invalid_json(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{"foo": "bar"},')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert 'Invalid Json' in str(exc)

    def test_handle_request_404(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(404, b'{}')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert '404' in str(exc)

    def test_handle_request_401(self, session_get_mock, utc_mock):
        """ Tests no client token present """
        now = datetime.utcnow()
        utc_mock.return_value = now

        session_get_mock.side_effect = [
            ResponseMock()(401, b'{}'),
            ResponseMock()(200, b'{"access_token": "123", "expires_in": 120}'),
            ResponseMock()(200, b'{"response": "ok"}'),
        ]
        data = self.api._handle_request(self.test_url)

        assert data == {'response': 'ok'}
        assert self.api._access_token == '123'
        assert self.api._access_token_expiration == now + timedelta(seconds=120)

    def test_handle_request_cannot_authorize(self, session_get_mock):
        session_get_mock.side_effect = [
            ResponseMock()(401, b'{}'),
            ResponseMock()(401, b'{}'),
        ]

        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert '401 for https://us.battle.net/oauth/token' in str(exc)

    def test_get_resource_call(self, response_mock):
        self.authorized_api.get_resource(
            'foo/{0}', 'us', 1, locale='en_US', fields='pets,stats', breedId=9999)

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/foo/1',
            params={
                'access_token': '987',
                'locale': 'en_US',
                'fields': 'pets,stats',
                'breedId': 9999
            }
        )

    def test_get_resource_call_china(self, response_mock):
        self.authorized_api.get_resource(
            'foo/{0}', 'cn', 1)

        response_mock.assert_called_with(
            'https://api.blizzard.com.cn/wow/foo/1',
            params={
                'access_token': '987',
            }
        )

    def test_get_resource_no_access_token(self, session_get_mock, utc_mock):
        now = datetime.utcnow()
        utc_mock.return_value = now

        session_get_mock.side_effect = [
            ResponseMock()(200, b'{"access_token": "111", "expires_in": 60}'),
            ResponseMock()(200, b'{"response": "ok"}'),
        ]
        data = self.api.get_resource('foo', 'eu')

        assert data == {'response': 'ok'}
        assert self.api._access_token == '111'
        assert self.api._access_token_expiration == now + timedelta(seconds=60)

    def test_get_resource_no_access_expired(self, session_get_mock, utc_mock):
        now = datetime.utcnow()
        utc_mock.return_value = now

        self.api._access_token = '222'
        self.api._access_token_expiration = now

        session_get_mock.side_effect = [
            ResponseMock()(200, b'{"access_token": "999", "expires_in": 60}'),
            ResponseMock()(200, b'{"response": "ok"}'),
        ]
        data = self.api.get_resource('foo', 'eu')

        assert data == {'response': 'ok'}
        assert self.api._access_token == '999'
        assert self.api._access_token_expiration == now + timedelta(seconds=60)

    def test_get_achievement(self, response_mock):
        self.authorized_api.get_achievement('us', 1234)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/achievement/1234', params=self.params)

    def test_get_auctions(self, response_mock):
        self.authorized_api.get_auctions('us', 'khadgar')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/auction/data/khadgar', params=self.params)

    def test_get_bosses(self, response_mock):
        self.authorized_api.get_bosses('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/boss/', params=self.params)

    def test_get_boss(self, response_mock):
        self.authorized_api.get_boss('us', 24723)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/boss/24723', params=self.params)

    def test_get_realm_leaderboard(self, response_mock):
        self.authorized_api.get_realm_leaderboard('us', 'silvermoon')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/challenge/silvermoon', params=self.params)

    def test_get_region_leaderboard(self, response_mock):
        self.authorized_api.get_region_leaderboard('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/challenge/region', params=self.params)

    def test_get_character_profile(self, response_mock):
        self.authorized_api.get_character_profile('eu', 'khadgar', 'patchwerk')
        response_mock.assert_called_with(
            'https://eu.api.blizzard.com/wow/character/khadgar/patchwerk', params=self.params)

    def test_get_guild_profile(self, response_mock):
        self.authorized_api.get_guild_profile('eu', 'draenor', 'topguild')
        response_mock.assert_called_with(
            'https://eu.api.blizzard.com/wow/guild/draenor/topguild', params=self.params)

    def test_get_item(self, response_mock):
        self.authorized_api.get_item('us', 9999)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/item/9999', params=self.params)

    def test_get_item_set(self, response_mock):
        self.authorized_api.get_item_set('us', 1060)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/item/set/1060', params=self.params)

    def test_get_mounts(self, response_mock):
        self.authorized_api.get_mounts('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/mount/', params=self.params)

    def test_get_pets(self, response_mock):
        self.authorized_api.get_pets('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/', params=self.params)

    def test_get_pet_ability(self, response_mock):
        self.authorized_api.get_pet_ability('us', 640)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/ability/640', params=self.params)

    def test_get_pet_species(self, response_mock):
        self.authorized_api.get_pet_species('us', 258)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/species/258', params=self.params)

    def test_get_pet_stats(self, response_mock):
        self.authorized_api.get_pet_stats('eu', 258)
        response_mock.assert_called_with(
            'https://eu.api.blizzard.com/wow/pet/stats/258', params=self.params)

    def test_get_leaderboards(self, response_mock):
        self.authorized_api.get_leaderboards('us', '5v5')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/leaderboard/5v5', params=self.params)

    def test_get_quest(self, response_mock):
        self.authorized_api.get_quest('us', 13146)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/quest/13146', params=self.params)

    def test_get_realm_status(self, response_mock):
        self.authorized_api.get_realm_status('kr')
        response_mock.assert_called_with(
            'https://kr.api.blizzard.com/wow/realm/status', params=self.params)

    def test_get_recipe(self, response_mock):
        self.authorized_api.get_recipe('us', 33994)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/recipe/33994', params=self.params)

    def test_get_spell(self, response_mock):
        self.authorized_api.get_spell('us', 8056)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/spell/8056', params=self.params)

    def test_get_zones(self, response_mock):
        self.authorized_api.get_zones('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/zone/', params=self.params)

    def test_get_zone(self, response_mock):
        self.authorized_api.get_zone('us', 4131)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/zone/4131', params=self.params)

    def test_get_battlegroups(self, response_mock):
        self.authorized_api.get_battlegroups('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/battlegroups/', params=self.params)

    def test_get_character_races(self, response_mock):
        self.authorized_api.get_character_races('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/character/races', params=self.params)

    def test_get_character_classes(self, response_mock):
        self.authorized_api.get_character_classes('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/character/classes', params=self.params)

    def test_get_character_achievements(self, response_mock):
        self.authorized_api.get_character_achievements('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/character/achievements', params=self.params)

    def test_get_guild_rewards(self, response_mock):
        self.authorized_api.get_guild_rewards('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/guild/rewards', params=self.params)

    def test_get_guild_perks(self, response_mock):
        self.authorized_api.get_guild_perks('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/guild/perks', params=self.params)

    def test_get_guild_achievements(self, response_mock):
        self.authorized_api.get_guild_achievements('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/guild/achievements', params=self.params)

    def test_get_item_classes(self, response_mock):
        self.authorized_api.get_item_classes('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/item/classes', params=self.params)

    def test_get_talents(self, response_mock):
        self.authorized_api.get_talents('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/talents', params=self.params)

    def test_get_pet_types(self, response_mock):
        self.authorized_api.get_pet_types('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/data/pet/types', params=self.params)
