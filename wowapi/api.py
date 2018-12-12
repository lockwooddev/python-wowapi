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

        self._access_tokens = {}

    def _utcnow(self):
        return datetime.utcnow()

    def _get_client_credentials(self, region):
        path = '/oauth/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(
            self._client_id, self._client_secret
        )

        url = 'https://{0}.battle.net{1}'.format(region, path)
        if region == 'cn':
            url = 'https://www.battlenet.com.cn{0}'.format(path)

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

        self._access_tokens[region] = {
            'token': token,
            'expiration': expiration
        }

    def get_data_resource(self, url, region):
        params = {'access_token': self._access_tokens.get(region, {}).get('token', '')}
        return self._handle_request(url, region, params=params)

    def _handle_request(self, url, region, **kwargs):
        try:
            response = self._session.get(url, **kwargs)
        except RequestException as exc:
            logger.exception(str(exc))
            raise WowApiException(str(exc))

        if not response.ok:
            # get a new token and try request again
            if response.status_code == 401:
                logger.info('Access token invalid. Fetching new token..')
                self._get_client_credentials(region)
                return self._handle_request(url, region, **kwargs)

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
            base_url = 'www.gateway.battlenet.com.cn'

        url = 'https://{0}/{1}'.format(base_url, resource)

        # fetch access token on first run for region
        if region not in self._access_tokens:
            logger.info('Fetching access token..')
            self._get_client_credentials(region)
        else:
            now = datetime.utcnow()
            # refresh access token if expired
            if now >= self._access_tokens[region]['expiration']:
                logger.info('Access token expired. Fetching new token..')
                self._get_client_credentials(region)

        filters['access_token'] = self._access_tokens[region]['token']
        logger.info('Requesting resource: {0} with parameters: {1}'.format(url, filters))
        return self._handle_request(url, region, params=filters)

    def get_achievement(self, region, id, **filters):
        """
        Achievement api

        >>> WowApi.get_achievement('us', 2144, locale='pt_BR')
        """
        return self.get_resource('wow/achievement/{0}', region, *[id], **filters)

    def get_auctions(self, region, realm_slug, **filters):
        """
        Auctions data status
        """
        return self.get_resource('wow/auction/data/{0}', region, *[realm_slug], **filters)

    def get_bosses(self, region, **filters):
        """
        Boss api - Master list of bosses
        """
        return self.get_resource('wow/boss/', region, **filters)

    def get_boss(self, region, id, **filters):
        """
        Boss api - Boss details
        """
        return self.get_resource('wow/boss/{0}', region, *[id], **filters)

    def get_realm_leaderboard(self, region, realm, **filters):
        """
        Challenge mode api - realm leaderboard
        """
        return self.get_resource('wow/challenge/{0}', region, *[realm], **filters)

    def get_region_leaderboard(self, region, **filters):
        """
        Challenge mode api - region leaderboard
        """
        return self.get_resource('wow/challenge/region', region, **filters)

    def get_character_profile(self, region, realm, character_name, **filters):
        """
        Character profile api - base info or specific comma separated fields as filters

        >>> api = WowApi('client-id', 'client-secret')
        >>> api.get_character_profile('eu', 'khadgar', 'patchwerk')
        >>> api.get_character_profile('eu', 'khadgar', 'patchwerk', locale='en_GB', fields='guild,mounts')
        """  # noqa
        return self.get_resource(
            'wow/character/{0}/{1}', region, *[realm, character_name], **filters
        )

    def get_guild_profile(self, region, realm, guild_name, **filters):
        """
        Guild profile api - base info or specific comma separated fields as filters

        >>> api = WowApi('client-id', 'client-secret')
        >>> api.get_guild_profile('eu', 'khadgar')
        >>> api.get_guild_profile('eu', 'khadgar', locale='en_GB', fields='achievements,challenge')
        """
        return self.get_resource(
            'wow/guild/{0}/{1}', region, *[realm, guild_name], **filters
        )

    def get_item(self, region, id, **filters):
        """
        Item api - detail iten
        """
        return self.get_resource('wow/item/{0}', region, *[id], **filters)

    def get_item_set(self, region, id, **filters):
        """
        Item api - detail iten set
        """
        return self.get_resource('wow/item/set/{0}', region, *[id], **filters)

    def get_mounts(self, region, **filters):
        """
        Mounts api - all supported mounts
        """
        return self.get_resource('wow/mount/', region, **filters)

    def get_pets(self, region, **filters):
        """
        Pets api - all supported pets
        """
        return self.get_resource('wow/pet/', region, **filters)

    def get_pet_ability(self, region, id, **filters):
        """
        Pets api - pet ability details
        """
        return self.get_resource('wow/pet/ability/{0}', region, *[id], **filters)

    def get_pet_species(self, region, id, **filters):
        """
        Pets api - pet species details
        """
        return self.get_resource('wow/pet/species/{0}', region, *[id], **filters)

    def get_pet_stats(self, region, id, **filters):
        """
        Pets api - pet stats details
        """
        return self.get_resource('wow/pet/stats/{0}', region, *[id], **filters)

    def get_leaderboards(self, region, bracket, **filters):
        """
        Pvp api - pvp bracket leaderboard and rbg
        """
        return self.get_resource('wow/leaderboard/{0}', region, *[bracket], **filters)

    def get_quest(self, region, id, **filters):
        """
        Quest api - metadata for quests
        """
        return self.get_resource('wow/quest/{0}', region, *[id], **filters)

    def get_realm_status(self, region, **filters):
        """
        Realm status api - realm status for region
        """
        return self.get_resource('wow/realm/status', region, **filters)

    def get_recipe(self, region, id, **filters):
        """
        Recipe api - recipe details
        """
        return self.get_resource('wow/recipe/{0}', region, *[id], **filters)

    def get_spell(self, region, id, **filters):
        """
        Spell api - spell details
        """
        return self.get_resource('wow/spell/{0}', region, *[id], **filters)

    def get_zones(self, region, **filters):
        """
        Zone api - master list
        """
        return self.get_resource('wow/zone/', region, **filters)

    def get_zone(self, region, id, **filters):
        """
        Zone api - detail zone
        """
        return self.get_resource('wow/zone/{0}', region, *[id], **filters)

    def get_battlegroups(self, region, **filters):
        """
        Data resources api - all battlegroups
        """
        return self.get_resource('wow/data/battlegroups/', region, **filters)

    def get_character_races(self, region, **filters):
        """
        Data resources api - all character races
        """
        return self.get_resource('wow/data/character/races', region, **filters)

    def get_character_classes(self, region, **filters):
        """
        Data resources api - all character classes
        """
        return self.get_resource('wow/data/character/classes', region, **filters)

    def get_character_achievements(self, region, **filters):
        """
        Data resources api - all character achievements
        """
        return self.get_resource('wow/data/character/achievements', region, **filters)

    def get_guild_rewards(self, region, **filters):
        """
        Data resources api - all guild rewards
        """
        return self.get_resource('wow/data/guild/rewards', region, **filters)

    def get_guild_perks(self, region, **filters):
        """
        Data resources api - all guild perks
        """
        return self.get_resource('wow/data/guild/perks', region, **filters)

    def get_guild_achievements(self, region, **filters):
        """
        Data resources api - all guild achievements
        """
        return self.get_resource('wow/data/guild/achievements', region, **filters)

    def get_item_classes(self, region, **filters):
        """
        Data resources api - all item classes
        """
        return self.get_resource('wow/data/item/classes', region, **filters)

    def get_talents(self, region, **filters):
        """
        Data resources api - all talents, specs and glyphs for each class
        """
        return self.get_resource('wow/data/talents', region, **filters)

    def get_pet_types(self, region, **filters):
        """
        Data resources api - all pet types
        """
        return self.get_resource('wow/data/pet/types', region, **filters)

    # ---------------------------------------------------------------------------------------------
    # Game Data API wrappers
    # ---------------------------------------------------------------------------------------------

    def get_connected_realms(self, region, namespace, **filters):
        """
        Game data api - get connected realms
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/connected-realm/', region, **filters)

    def get_connected_realm(self, region, namespace, connected_realm_id, **filters):
        """
        Game data api - get connected realm by id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/connected-realm/{0}', region, *[connected_realm_id], **filters
        )

    def get_mythic_keystone_leaderboards(self, region, namespace, connected_realm_id, **filters):
        """
        Game data api - get mythic keystone leaderboards by connected realm id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/connected-realm/{0}/mythic-leaderboard/',
            region,
            *[connected_realm_id],
            **filters
        )

    def get_mythic_keystone_leaderboard(self,
                                        region, namespace, connected_realm_id, dungeon_id, period,
                                        **filters):
        """
        Game data api - get mythic keystone leaderboard of specific dungeon
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/connected-realm/{0}/mythic-leaderboard/{1}/period/{2}',
            region,
            *[connected_realm_id, dungeon_id, period],
            **filters
        )

    def get_mythic_raid_leaderboard(self, region, namespace, raid, faction, **filters):
        """
        Game data api - get mythic raid leaderboard of specific faction
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/leaderboard/hall-of-fame/{0}/{1}',
            region,
            *[raid, faction],
            **filters
        )

    def get_mythic_challenge_modes(self, region, namespace, **filters):
        """
        Game data api - get period information of mythic challenge modes
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mythic-challenge-mode/', region, **filters)

    def get_playable_classes(self, region, namespace, **filters):
        """
        Game data api - get all available playable classes
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-class/', region, **filters)

    def get_playable_class(self, region, namespace, class_id, **filters):
        """
        Game data api - get playable classes by class id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-class/{0}', region, *[class_id], **filters)

    def get_playable_specializations(self, region, namespace, **filters):
        """
        Game data api - get all playable specializations
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-specialization/', region, **filters)

    def get_playable_specialization(self, region, namespace, spec_id, **filters):
        """
        Game data api - get playable specialization by spec id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/playable-specialization/{0}',
            region,
            *[spec_id],
            **filters
        )

    def get_realms(self, region, namespace, **filters):
        """
        Game data api - get all realms
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/realm/', region, **filters)

    def get_realm(self, region, namespace, realm_slug, **filters):
        """
        Game data api - get realm by realm slug
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/realm/{0}', region, *[realm_slug], **filters)

    def get_regions(self, region, namespace, **filters):
        """
        Game data api - get all regions
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/region/', region, **filters)

    def get_region(self, region, namespace, region_id, **filters):
        """
        Game data api - get region by region id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/region/{0}', region, *[region_id], **filters)

    def get_token(self, regiom, namespace, **filters):
        """
        Game data api - get Wow token
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/token/', regiom, **filters)
