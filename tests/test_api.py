import copy
from datetime import datetime, timedelta

import pytest
from requests.exceptions import RequestException

from wowapi import WowApi, WowApiException
from .fixtures import ResponseMock


class TestWowApi(object):

    def setup(self):
        self.params = {'access_token': 'secret'}

        self.api = WowApi('client-id', 'client-secret')

        self.authorized_api = WowApi('client-id', 'client-secret')
        self.authorized_api._access_tokens = {
            'us': {
                'token': 'secret',
                'expiration': datetime.utcnow() + timedelta(hours=1)
            },
            'cn': {
                'token': 'secret',
                'expiration': datetime.utcnow() + timedelta(hours=1)
            }
        }

        self.test_url = 'http://example.com'

        self.default_region = 'us'

    def test_instance(self):
        assert not self.api._access_tokens

    def test_handle_request_success(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{}')
        data = self.api._handle_request(self.test_url, self.default_region)
        assert data == {}
        session_get_mock.assert_called_with(self.test_url)

    def test_handle_request_request_exception(self, session_get_mock):
        session_get_mock.side_effect = RequestException('Error')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

        assert 'Error' in str(exc)

    def test_handle_request_invalid_json(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{"foo": "bar"},')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

        assert 'Invalid Json' in str(exc)

    def test_handle_request_404(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(404, b'{}')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

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
        data = self.api._handle_request(self.test_url, self.default_region)

        assert data == {'response': 'ok'}
        assert self.api._access_tokens == {
            'us': {
                'token': '123',
                'expiration': now + timedelta(seconds=120)
            }
        }

    def test_handle_request_cannot_authorize(self, session_get_mock):
        session_get_mock.side_effect = [
            ResponseMock()(401, b'{}'),
            ResponseMock()(401, b'{}'),
        ]

        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

        assert '401 for https://us.battle.net/oauth/token' in str(exc)

    def test_get_resource_call(self, response_mock):
        self.authorized_api.get_resource(
            'resource/{0}', 'us', 1, locale='en_US', fields='pets,stats', breedId=9999)

        response_mock.assert_called_with(
            'https://us.api.blizzard.com/resource/1',
            params={
                'access_token': 'secret',
                'locale': 'en_US',
                'fields': 'pets,stats',
                'breedId': 9999
            }
        )

    def test_get_resource_call_china(self, response_mock):
        self.authorized_api.get_resource('resource/{0}', 'cn', 1)

        response_mock.assert_called_with(
            'https://www.gateway.battlenet.com.cn/resource/1',
            params={
                'access_token': 'secret',
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
        assert self.api._access_tokens == {
            'eu': {
                'token': '111',
                'expiration': now + timedelta(seconds=60)
            }
        }

    def test_get_resource_no_access_expired(self, session_get_mock, utc_mock):
        now = datetime.utcnow()
        utc_mock.return_value = now

        self.api._access_tokens = {
            'eu': {
                'token': '222',
                'expiration': now
            }
        }

        session_get_mock.side_effect = [
            ResponseMock()(200, b'{"access_token": "333", "expires_in": 60}'),
            ResponseMock()(200, b'{"response": "ok"}'),
        ]
        data = self.api.get_resource('foo', 'eu')

        assert data == {'response': 'ok'}
        assert self.api._access_tokens == {
            'eu': {
                'token': '333',
                'expiration': now + timedelta(seconds=60)
            }
        }

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
        self.authorized_api.get_character_profile('us', 'khadgar', 'patchwerk')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/character/khadgar/patchwerk', params=self.params)

    def test_get_guild_profile(self, response_mock):
        self.authorized_api.get_guild_profile('us', 'draenor', 'topguild')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/guild/draenor/topguild', params=self.params)

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
        self.authorized_api.get_pet_stats('us', 258)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/pet/stats/258', params=self.params)

    def test_get_leaderboards(self, response_mock):
        self.authorized_api.get_leaderboards('us', '5v5')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/leaderboard/5v5', params=self.params)

    def test_get_quest(self, response_mock):
        self.authorized_api.get_quest('us', 13146)
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/quest/13146', params=self.params)

    def test_get_realm_status(self, response_mock):
        self.authorized_api.get_realm_status('us')
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/wow/realm/status', params=self.params)

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

    # ---------------------------------------------------------------------------------------------
    # Game Data API tests
    # ---------------------------------------------------------------------------------------------

    # Connected Realm API

    def test_get_connected_realms(self, response_mock):
        self.authorized_api.get_connected_realms('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/index', params=params)

    def test_get_connected_realm(self, response_mock):
        self.authorized_api.get_connected_realm('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1', params=params)

    # Mythic Keystone Affix API

    def test_get_mythic_keystone_affixes(self, response_mock):
        self.authorized_api.get_mythic_keystone_affixes('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/keystone-affix/index', params=params)

    def test_get_mythic_keystone_affix(self, response_mock):
        self.authorized_api.get_mythic_keystone_affix('us', 'dynamic-us', 3)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/keystone-affix/3', params=params)

    # Mythic Raid Leaderboard API

    def test_get_mythic_raid_leaderboard(self, response_mock):
        self.authorized_api.get_mythic_raid_leaderboard('us', 'dynamic-us', 'uldir', 'horde')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/leaderboard/hall-of-fame/uldir/horde',
            params=params
        )

    # Mythic Keystone Dungeon API

    def test_get_mythic_keystone_dungeons(self, response_mock):
        self.authorized_api.get_mythic_keystone_dungeons('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index', params=params)

    def test_get_mythic_keystone_dungeon(self, response_mock):
        self.authorized_api.get_mythic_keystone_dungeon('us', 'dynamic-us', 5)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/5', params=params)

    def test_get_mythic_keystones(self, response_mock):
        self.authorized_api.get_mythic_keystones('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/index', params=params)

    def test_get_mythic_keystone_periods(self, response_mock):
        self.authorized_api.get_mythic_keystone_periods('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/period/index', params=params)

    def test_get_mythic_keystone_period(self, response_mock):
        self.authorized_api.get_mythic_keystone_period('us', 'dynamic-us', 641)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/period/641', params=params)

    def test_get_mythic_keystone_seasons(self, response_mock):
        self.authorized_api.get_mythic_keystone_seasons('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/season/index', params=params)

    def test_get_mythic_keystone_season(self, response_mock):
        self.authorized_api.get_mythic_keystone_season('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/mythic-keystone/season/1', params=params)

    # Mythic Keystone Leaderboard API

    def test_get_mythic_keystone_leaderboards(self, response_mock):
        self.authorized_api.get_mythic_keystone_leaderboards('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/index',
            params=params
        )

    def test_get_mythic_keystone_leaderboard(self, response_mock):
        self.authorized_api.get_mythic_keystone_leaderboard('us', 'dynamic-us', 1, 2, 3)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/2/period/3',
            params=params
        )

    # Playable Class API

    def test_get_playable_classes(self, response_mock):
        self.authorized_api.get_playable_classes('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-class/index',
            params=params
        )

    def test_get_playable_class(self, response_mock):
        self.authorized_api.get_playable_class('us', 'static-us', 7)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-class/7',
            params=params
        )

    def test_get_playable_class_pvp_talent_slots(self, response_mock):
        self.authorized_api.get_playable_class_pvp_talent_slots('us', 'static-us', 7)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-class/7/pvp-talent-slots',
            params=params
        )

    # Playable Specialization API

    def test_get_playable_specializations(self, response_mock):
        self.authorized_api.get_playable_specializations('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-specialization/index',
            params=params
        )

    def test_get_playable_specialization(self, response_mock):
        self.authorized_api.get_playable_specialization('us', 'static-us', 262)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/playable-specialization/262',
            params=params
        )

    # Power Type API

    def test_get_power_types(self, response_mock):
        self.authorized_api.get_power_types('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/power-type/index',
            params=params
        )

    def test_get_power_type(self, response_mock):
        self.authorized_api.get_power_type('us', 'static-us', 0)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/power-type/0',
            params=params
        )

    # Playable Race API

    def test_get_races(self, response_mock):
        self.authorized_api.get_races('us', 'static-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/race/index',
            params=params
        )

    def test_get_race(self, response_mock):
        self.authorized_api.get_race('us', 'static-us', 2)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'static-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/race/2',
            params=params
        )

    # Realm API

    def test_get_realms(self, response_mock):
        self.authorized_api.get_realms('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/realm/index',
            params=params
        )

    def test_get_realm(self, response_mock):
        self.authorized_api.get_realm('us', 'dynamic-us', 'tichondrius')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/realm/tichondrius',
            params=params
        )

    # Region API

    def test_get_regions(self, response_mock):
        self.authorized_api.get_regions('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/region/index',
            params=params
        )

    def test_get_region(self, response_mock):
        self.authorized_api.get_region('us', 'dynamic-us', 1)
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/region/1',
            params=params
        )

    # WoW Token API

    def test_get_token(self, response_mock):
        self.authorized_api.get_token('us', 'dynamic-us')
        params = copy.deepcopy(self.params)
        params['namespace'] = 'dynamic-us'
        response_mock.assert_called_with(
            'https://us.api.blizzard.com/data/wow/token/index', params=params)
