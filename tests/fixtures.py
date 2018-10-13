import pytest
import requests


@pytest.fixture
def session_get_mock(mocker):
    return mocker.patch('requests.Session.get')


@pytest.fixture
def utc_mock(mocker):
    return mocker.patch('wowapi.api.WowApi._utcnow')


def get_success_response():
    mock = requests.models.Response()
    mock.status_code = 200
    mock._content = b'{}'
    return mock


class ResponseMock(object):

    def __call__(self, status_code, content):
        mock = requests.models.Response()
        mock.status_code = status_code
        mock._content = content
        return mock


@pytest.fixture
def response_mock(mocker):
    return mocker.patch('requests.Session.get', return_value=get_success_response())
