import logging
from datetime import datetime, timedelta

import requests
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from requests.packages.urllib3.util.retry import Retry

from .exceptions import WowApiException, WowApiOauthException
from .mixins import GameDataMixin, ProfileMixin


logger = logging.getLogger('wowapi')
logger.addHandler(logging.NullHandler())


class WowApi(GameDataMixin, ProfileMixin):
    """
    ```python
    import os

    from wowapi import WowApi

    api = WowApi('client_id', 'client_secret')

    # Token price
    api.get_token('eu', namespace='dynamic-eu', locale='de_DE')

    # Auctions
    api.get_auctions('eu', 'silvermoon', locale='de_DE')
    ```
    """

    __base_url = '{0}.api.blizzard.com'

    def __init__(self, client_id, client_secret, retry_conn_failures=False):
        self._client_id = client_id
        self._client_secret = client_secret

        self._session = requests.Session()

        # Use default retry setup
        if retry_conn_failures:
            self.retry_conn_failures()

        self._access_tokens = {}

    def _utcnow(self):
        return datetime.utcnow()

    def retry_conn_failures(self, total=5, backoff_factor=1,
                            status_forcelist=[443, 500, 502, 503, 504]):
        # Allows a user to control how retries function
        retries = Retry(total=total, backoff_factor=backoff_factor,
                        status_forcelist=status_forcelist)
        self._session.mount('http://', HTTPAdapter(max_retries=retries))
        self._session.mount('https://', HTTPAdapter(max_retries=retries))

    def _get_client_credentials(self, region):
        path = '/oauth/token'
        data = {'grant_type': 'client_credentials'}
        auth = HTTPBasicAuth(self._client_id, self._client_secret)

        url = 'https://{0}.battle.net{1}'.format(region, path)
        if region == 'cn':
            url = 'https://www.battlenet.com.cn{0}'.format(path)

        logger.info('Fetching new token from: {0}'.format(url))

        now = self._utcnow()
        try:
            response = self._session.post(url, data=data, auth=auth)
        except RequestException as exc:
            logger.exception(str(exc))
            raise WowApiOauthException(str(exc))

        if not response.ok:
            msg = 'Invalid response - {0} for {1}'.format(response.status_code, url)
            logger.warning(msg)
            raise WowApiOauthException(msg)

        try:
            json = response.json()
        except Exception:
            msg = 'Invalid Json in OAuth response: {0} for {1}'.format(response.content, url)
            logger.exception(msg)
            raise WowApiOauthException(msg)

        token = json['access_token']
        expiration = now + timedelta(seconds=json['expires_in'])
        logger.info('New token {0} expires at {1} UTC'.format(token, expiration))

        self._access_tokens[region] = {
            'token': token,
            'expiration': expiration
        }

    def get_data_resource(self, url, region, **filters):
        """
        Some endpoints return a url pointing to another resource.
        These urls do not include OAuth tokens.
        `api.get_data_resource` takes care of this.

        ```python
        auctions_ref = api.get_auctions('eu', 'silvermoon', locale='de_DE')
        api.get_data_resource(auctions_ref['files'][0]['url'], 'eu')
        ```
        """
        access_token = self._access_tokens.get(region, {}).get('token', '')
        if access_token:
            filters['access_token'] = access_token

        return self._handle_request(url, params=filters)

    def _handle_request(self, url, **kwargs):
        try:
            response = self._session.get(url, **kwargs)
        except RequestException as exc:
            logger.exception(str(exc))
            raise WowApiException(str(exc))

        if not response.ok:
            msg = 'Invalid response - {0} - {1}'.format(url, response.status_code)
            logger.warning(msg)
            raise WowApiException(msg)

        try:
            return response.json()
        except Exception:
            msg = 'Invalid Json: {0} for {1}'.format(response.content, url)
            logger.exception(msg)
            raise WowApiException(msg)

    def get_resource(self, resource, region, *args, **filters):
        resource = resource.format(*args)

        # fetch access token on first run for region
        if region not in self._access_tokens:
            logger.info('Fetching access token..')
            self._get_client_credentials(region)
        else:
            now = self._utcnow()
            # refresh access token if expiring in the next 30 seconds.
            # this protects against the rare occurrence of hitting
            # the API right as your token expires, causing errors.
            if now >= self._access_tokens[region]['expiration'] - timedelta(seconds=30):
                logger.info('Access token expired. Fetching new token..')
                self._get_client_credentials(region)

        filters['access_token'] = self._access_tokens[region]['token']
        url = self._format_base_url(resource, region)
        logger.info('Requesting resource: {0} with parameters: {1}'.format(url, filters))
        return self._handle_request(url, params=filters)

    def get_oauth_resource(self, resource, region, token, *args, **filters):
        filters['access_token'] = token

        resource = resource.format(*args)

        url = self._format_base_url(resource, region)
        logger.info('Requesting resource: {0} with parameters: {1}'.format(url, filters))
        return self._handle_request(url, params=filters)

    def _format_base_url(self, resource, region):
        base_url = self.__base_url.format(region)
        if region == 'cn':
            base_url = 'www.gateway.battlenet.com.cn'

        return 'https://{0}/{1}'.format(base_url, resource)
