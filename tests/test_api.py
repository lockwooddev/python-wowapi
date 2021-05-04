from datetime import datetime, timedelta

import pytest
from requests.exceptions import RequestException

from wowapi import WowApi, WowApiException, WowApiOauthException

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
        data = self.api._handle_request(self.test_url)
        assert data == {}
        session_get_mock.assert_called_with(self.test_url)

    def test_handle_request_request_exception(self, session_get_mock):
        session_get_mock.side_effect = RequestException('Error')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert 'Error' in str(exc.value)

    def test_handle_request_invalid_json(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{"foo": "bar"},')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert 'Invalid Json' in str(exc.value)

    def test_handle_request_404(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(404, b'{}')
        with pytest.raises(WowApiException) as exc:
            self.api._handle_request(self.test_url)

        assert '404' in str(exc.value)

    def test_get_data_resource_authorized(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{}')
        self.authorized_api.get_data_resource('https://us.api.blizzard.com/profile/wow/test', 'us')
        session_get_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/test',
            params={'access_token': 'secret'}
        )

    def test_get_data_resource_unauthorized(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{}')
        self.api.get_data_resource('https://us.api.blizzard.com/profile/wow/test', 'us')
        session_get_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/test',
            params={}
        )

    def test_get_data_resource_filters(self, session_get_mock):
        session_get_mock.return_value = ResponseMock()(200, b'{}')
        self.authorized_api.get_data_resource(
            'https://us.api.blizzard.com/profile/wow/test',
            'us',
            locale='de_DE',
        )

        session_get_mock.assert_called_with(
            'https://us.api.blizzard.com/profile/wow/test',
            params={
                'access_token': 'secret',
                'locale': 'de_DE',
            }
        )

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
        with pytest.raises(WowApiOauthException):
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
        with pytest.raises(WowApiOauthException):
            data = self.api.get_resource('foo', 'eu')

            assert data == {'response': 'ok'}
            assert self.api._access_tokens == {
                'eu': {
                    'token': '333',
                    'expiration': now + timedelta(seconds=60)
                }
            }

    def test_format_base_url(self):
        assert self.api._format_base_url('test', 'us') == 'https://us.api.blizzard.com/test'
        assert self.api._format_base_url('test', 'cn') == (
            'https://www.gateway.battlenet.com.cn/test'
        )
