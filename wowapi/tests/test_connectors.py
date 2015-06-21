from wowapi.connectors import APIConnector
from wowapi.exceptions import WowApiError, WowApiClientError

from mock import patch
import pytest
import requests


class TestAPIConnector:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.host = 'eu.battle.net'

    def test_get_query_parameters(self):
        instance = APIConnector(self.host, locale='en_GB', custom='test')
        instance.filters = ['locale', ]
        url_parameters = instance.get_query_parameters()
        assert 1, len(url_parameters)
        assert 'custom' not in url_parameters

    def test_get_url(self):
        instance = APIConnector(self.host, 'guild', 'player')
        url = instance.get_url()
        assert 'http://eu.battle.net/api/wow/guild/player' == url

    def test_https(self):
        instance = APIConnector(self.host, 'guild', 'player', secure=True)
        assert 'https://' == instance.protocol

    def test_requests_error(self):
        instance = APIConnector(self.host)
        with patch.object(requests, 'get') as mock_method:
            with pytest.raises(WowApiClientError):
                mock_method.side_effect = requests.RequestException
                instance.handle_request('http://test')

    @patch('requests.get')
    @patch('requests.models.Response.json')
    def test_status_not_ok(self, json_mock, get_mock):
        res = requests.models.Response()
        res.status_code = 404
        res.encoding = 'UTF-8'
        res._content = ''

        json_mock.return_value = {
            'status': 'nok',
            'reason': 'something unexpected happened'}
        get_mock.return_value = res
        instance = APIConnector(self.host)

        with pytest.raises(WowApiError):
            instance.handle_request('http://test')

    @patch('requests.get')
    @patch('requests.models.Response.json')
    def test_json_decode_error(self, json_mock, get_mock):
        res = requests.models.Response()
        res.status_code = 404
        res._content = ''

        json_mock.side_effect = WowApiClientError('')
        get_mock.return_value = res
        instance = APIConnector(self.host)

        with pytest.raises(WowApiClientError):
            instance.handle_request('http://test')
