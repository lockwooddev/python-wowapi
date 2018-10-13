import logging
from datetime import datetime, timedelta

import requests
from requests.exceptions import RequestException

from .exceptions import WowApiException, WowApiOauthException


logger = logging.getLogger('wowapi')
logger.addHandler(logging.NullHandler())


class WowApi(object):

    __base_url = '{0}.api.blizzard.com'

    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret

        self._session = requests.Session()

        self._access_token = None
        self._access_token_expiration = None

    def _utcnow(self):
        return datetime.utcnow()

    def _get_client_credentials(self):
        path = '/oauth/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(
            self._client_id, self._client_secret
        )
        url = 'https://us.battle.net{0}'.format(path)

        logger.info('Fetching new token from: {0}'.format(url))

        now = self._utcnow()
        try:
            response = self._session.get(url)
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
            msg = 'Invalid Json in OAuth request: {0} for {1}'.format(response.content, url)
            logger.exception(msg)
            raise WowApiOauthException(msg)

        token = json['access_token']
        expiration = now + timedelta(seconds=json['expires_in'])
        logger.info('New token {0} expires at {1} UTC'.format(token, expiration))

        self._access_token = token
        self._access_token_expiration = expiration

    def _handle_request(self, url, **kwargs):
        try:
            response = self._session.get(url, **kwargs)
        except RequestException as exc:
            logger.exception(str(exc))
            raise WowApiException(str(exc))

        if not response.ok:
            # get a new token and try request again
            if response.status_code == 401:
                logger.info('Access token invalid. Fetching new token..')
                self._get_client_credentials()
                return self._handle_request(url, **kwargs)

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

        base_url = self.__base_url.format(region)
        if region == 'cn':
            base_url = 'api.blizzard.com.cn'

        url = 'https://{0}/wow/{1}'.format(base_url, resource)

        # fetch access token on first run
        if not self._access_token:
            logger.info('Fetching access token..')
            self._get_client_credentials()
        else:
            now = datetime.utcnow()
            # refresh access token if expired
            if now >= self._access_token_expiration:
                logger.info('Access token expired. Fetching new token..')
                self._get_client_credentials()

        filters['access_token'] = self._access_token
        logger.info('Requesting resource: {0} with parameters: {1}'.format(url, filters))
        return self._handle_request(url, params=filters)

    def get_achievement(self, region, id, **filters):
        """
        Achievement api

        >>> WowApi.get_achievement('us', 2144, locale='pt_BR')
        """
        return self.get_resource('achievement/{0}', region, *[id], **filters)

    def get_auctions(self, region, realm_slug, **filters):
        """
        Auctions data status
        """
        return self.get_resource('auction/data/{0}', region, *[realm_slug], **filters)

    def get_bosses(self, region, **filters):
        """
        Boss api - Master list of bosses
        """
        return self.get_resource('boss/', region, **filters)

    def get_boss(self, region, id, **filters):
        """
        Boss api - Boss details
        """
        return self.get_resource('boss/{0}', region, *[id], **filters)

    def get_realm_leaderboard(self, region, realm, **filters):
        """
        Challenge mode api - realm leaderboard
        """
        return self.get_resource('challenge/{0}', region, *[realm], **filters)

    def get_region_leaderboard(self, region, **filters):
        """
        Challenge mode api - region leaderboard
        """
        return self.get_resource('challenge/region', region, **filters)

    def get_character_profile(self, region, realm, character_name, **filters):
        """
        Character profile api - base info or specific comma separated fields as filters

        >>> api = WowApi('client-id', 'client-secret')
        >>> api.get_character_profile('eu', 'khadgar', 'patchwerk')
        >>> api.get_character_profile('eu', 'khadgar', 'patchwerk', locale='en_GB', fields='guild,mounts')
        """  # noqa
        return self.get_resource(
            'character/{0}/{1}', region, *[realm, character_name], **filters
        )

    def get_guild_profile(self, region, realm, guild_name, **filters):
        """
        Guild profile api - base info or specific comma separated fields as filters

        >>> api = WowApi('client-id', 'client-secret')
        >>> api.get_guild_profile('eu', 'khadgar')
        >>> api.get_guild_profile('eu', 'khadgar', locale='en_GB', fields='achievements,challenge')
        """
        return self.get_resource(
            'guild/{0}/{1}', region, *[realm, guild_name], **filters
        )

    def get_item(self, region, id, **filters):
        """
        Item api - detail iten
        """
        return self.get_resource('item/{0}', region, *[id], **filters)

    def get_item_set(self, region, id, **filters):
        """
        Item api - detail iten set
        """
        return self.get_resource('item/set/{0}', region, *[id], **filters)

    def get_mounts(self, region, **filters):
        """
        Mounts api - all supported mounts
        """
        return self.get_resource('mount/', region, **filters)

    def get_pets(self, region, **filters):
        """
        Pets api - all supported pets
        """
        return self.get_resource('pet/', region, **filters)

    def get_pet_ability(self, region, id, **filters):
        """
        Pets api - pet ability details
        """
        return self.get_resource('pet/ability/{0}', region, *[id], **filters)

    def get_pet_species(self, region, id, **filters):
        """
        Pets api - pet species details
        """
        return self.get_resource('pet/species/{0}', region, *[id], **filters)

    def get_pet_stats(self, region, id, **filters):
        """
        Pets api - pet stats details
        """
        return self.get_resource('pet/stats/{0}', region, *[id], **filters)

    def get_leaderboards(self, region, bracket, **filters):
        """
        Pvp api - pvp bracket leaderboard and rbg
        """
        return self.get_resource('leaderboard/{0}', region, *[bracket], **filters)

    def get_quest(self, region, id, **filters):
        """
        Quest api - metadata for quests
        """
        return self.get_resource('quest/{0}', region, *[id], **filters)

    def get_realm_status(self, region, **filters):
        """
        Realm status api - realm status for region
        """
        return self.get_resource('realm/status', region, **filters)

    def get_recipe(self, region, id, **filters):
        """
        Recipe api - recipe details
        """
        return self.get_resource('recipe/{0}', region, *[id], **filters)

    def get_spell(self, region, id, **filters):
        """
        Spell api - spell details
        """
        return self.get_resource('spell/{0}', region, *[id], **filters)

    def get_zones(self, region, **filters):
        """
        Zone api - master list
        """
        return self.get_resource('zone/', region, **filters)

    def get_zone(self, region, id, **filters):
        """
        Zone api - detail zone
        """
        return self.get_resource('zone/{0}', region, *[id], **filters)

    def get_battlegroups(self, region, **filters):
        """
        Data resources api - all battlegroups
        """
        return self.get_resource('data/battlegroups/', region, **filters)

    def get_character_races(self, region, **filters):
        """
        Data resources api - all character races
        """
        return self.get_resource('data/character/races', region, **filters)

    def get_character_classes(self, region, **filters):
        """
        Data resources api - all character classes
        """
        return self.get_resource('data/character/classes', region, **filters)

    def get_character_achievements(self, region, **filters):
        """
        Data resources api - all character achievements
        """
        return self.get_resource('data/character/achievements', region, **filters)

    def get_guild_rewards(self, region, **filters):
        """
        Data resources api - all guild rewards
        """
        return self.get_resource('data/guild/rewards', region, **filters)

    def get_guild_perks(self, region, **filters):
        """
        Data resources api - all guild perks
        """
        return self.get_resource('data/guild/perks', region, **filters)

    def get_guild_achievements(self, region, **filters):
        """
        Data resources api - all guild achievements
        """
        return self.get_resource('data/guild/achievements', region, **filters)

    def get_item_classes(self, region, **filters):
        """
        Data resources api - all item classes
        """
        return self.get_resource('data/item/classes', region, **filters)

    def get_talents(self, region, **filters):
        """
        Data resources api - all talents, specs and glyphs for each class
        """
        return self.get_resource('data/talents', region, **filters)

    def get_pet_types(self, region, **filters):
        """
        Data resources api - all pet types
        """
        return self.get_resource('data/pet/types', region, **filters)
