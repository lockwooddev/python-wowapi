import pytest
import requests
from requests.exceptions import RequestException


def response_mock():
    mock = requests.models.Response()
    mock.status_code = 200
    mock._content = b'{}'
    return mock


@pytest.fixture
def get_mock(mocker):
    return mocker.patch('requests.get', return_value=response_mock())


@pytest.fixture
def get_404_mock(mocker):
    mock = response_mock()
    mock.status_code = 404
    mock._content = 'Not Found'

    return mocker.patch('requests.get', return_value=mock)


@pytest.fixture
def invalid_json_mock(mocker):
    mock = response_mock()
    mock._content = b'{"foo": "bar"},'

    return mocker.patch('requests.get', return_value=mock)


@pytest.fixture
def request_exception_mock(mocker):

    return mocker.patch('requests.get', side_effect=RequestException('Problem'))
