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

        assert 'Error' in str(exc.value)

    def test_handle_request_invalid_json(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{"foo": "bar"},')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

        assert 'Invalid Json' in str(exc.value)

    def test_handle_request_404(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(404, b'{}')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

        assert '404' in str(exc.value)

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

    def test_handle_request_401_china(self, session_get_mock, utc_mock):
        """ Tests no client token present """
        now = datetime.utcnow()
        utc_mock.return_value = now

        session_get_mock.side_effect = [
            ResponseMock()(401, b'{}'),
            ResponseMock()(200, b'{"access_token": "123", "expires_in": 120}'),
            ResponseMock()(200, b'{"response": "ok"}'),
        ]
        data = self.api._handle_request(self.test_url, 'cn')

        assert data == {'response': 'ok'}
        assert self.api._access_tokens == {
            'cn': {
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

        assert '401 for https://us.battle.net/oauth/token' in str(exc.value)

    def test_handle_invalid_authorize_json(self, session_get_mock):
        session_get_mock.side_effect = [
            ResponseMock()(401, b'{}'),
            ResponseMock()(200, b'{fdfdfdf}}'),
        ]

        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url, self.default_region)

        assert 'Invalid Json in OAuth response' in str(exc.value)

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
