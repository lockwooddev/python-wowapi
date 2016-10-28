import os

import requests
from requests.exceptions import RequestException

from .exceptions import WowApiException, WowApiConfigException


class WowApi(object):

    base_urls = {
        'us': 'us.api.battle.net',
        'eu': 'eu.api.battle.net',
        'kr': 'kr.api.battle.net',
        'tw': 'tw.api.battle.net',
        'cn': 'api.battlenet.com.cn',
        'sea': 'sea.api.battle.net',
    }

    @classmethod
    def get_resource(cls, resource, region, *args, **filters):
        resource = resource.format(*args)

        region_url = cls.base_urls.get(region, None)
        if not region_url:
            raise WowApiConfigException("Region '{0}' not a valid region".format(region))

        url = 'https://{0}/wow/{1}'.format(cls.base_urls[region], resource)

        api_key = os.environ.get('WOWAPI_APIKEY', None)
        if not api_key:
            raise WowApiConfigException('WOWAPI_APIKEY is missing from your env variables')

        filters['apikey'] = api_key

        try:
            response = requests.get(url, params=filters)
        except RequestException as exc:
            raise

        if response.ok:
            try:
                json = response.json()
            except Exception as exc:
                raise WowApiException('Invalid Json: {0}'.format(response.content))

        else:
            error_msg = '{0} - {1}'.format(url, response.status_code)
            raise WowApiException(error_msg)

        return json

    @classmethod
    def get_achievement(cls, region, id, **filters):
        """
        Achievement api

        >>> WowApi.get_achievement('us', 2144, locale='pt_BR')
        """
        return cls.get_resource('achievement/{0}', region, *[id], **filters)

    @classmethod
    def get_auctions(cls, region, realm_slug):
        """
        Auctions api
        """
        return cls.get_resource('auction/data/{0}', region, *[realm_slug])

    @classmethod
    def get_bosses(cls, region, **filters):
        """
        Boss api - list of all supported bosses
        """
        return cls.get_resource('boss/', region, **filters)

    @classmethod
    def get_boss(cls, region, id, **filters):
        """
        Boss api - details of bosses
        """
        return cls.get_resource('boss/{0}', region, *[id], **filters)

    @classmethod
    def get_realm_leaderboard(cls, region, realm, **filters):
        """
        Challenge mode api - realm leaderboard
        """
        return cls.get_resource('challenge/{0}', region, *[realm], **filters)

    @classmethod
    def get_region_leaderboard(cls, region, **filters):
        """
        Challenge mode api - region leaderboard
        """
        return cls.get_resource('challenge/region', region, **filters)

    @classmethod
    def get_character_profile(cls, region, realm, character_name, **filters):
        """
        Character profile api - base info or specific comma separated fields as filters

        >>> WowApi.get_character_profile('eu', 'khadgar', 'patchwerk')

        >>> WowApi.get_character_profile('eu', 'khadgar', 'patchwerk', locale='en_GB', fields='guild,mounts')
        """  # noqa
        return cls.get_resource(
            'character/{0}/{1}', region, *[realm, character_name], **filters
        )

    @classmethod
    def get_guild_profile(cls, region, realm, guild_name, **filters):
        """
        Guild profile api - base info or specific comma separated fields as filters
        """
        return cls.get_resource(
            'guild/{0}/{1}', region, *[realm, guild_name], **filters
        )

    @classmethod
    def get_item(cls, region, id, **filters):
        """
        Item api - detail iten
        """
        return cls.get_resource('item/{0}', region, *[id], **filters)

    @classmethod
    def get_item_set(cls, region, id, **filters):
        """
        Item api - detail iten set
        """
        return cls.get_resource('item/set/{0}', region, *[id], **filters)

    @classmethod
    def get_mounts(cls, region, **filters):
        """
        Mounts api - all supported mounts
        """
        return cls.get_resource('mount/', region, **filters)

    @classmethod
    def get_pets(cls, region, **filters):
        """
        Pets api - all supported pets
        """
        return cls.get_resource('pet/', region, **filters)

    @classmethod
    def get_pet_ability(cls, region, id, **filters):
        """
        Pets api - pet ability details
        """
        return cls.get_resource('pet/ability/{0}', region, *[id], **filters)

    @classmethod
    def get_pet_species(cls, region, id, **filters):
        """
        Pets api - pet species details
        """
        return cls.get_resource('pet/species/{0}', region, *[id], **filters)

    @classmethod
    def get_pet_stats(cls, region, id, **filters):
        """
        Pets api - pet stats details
        """
        return cls.get_resource('pet/stats/{0}', region, *[id], **filters)

    @classmethod
    def get_leaderboards(cls, region, bracket, **filters):
        """
        Pvp api - pvp bracket leaderboard and rbg
        """
        return cls.get_resource('leaderboard/{0}', region, *[bracket], **filters)

    @classmethod
    def get_quest(cls, region, id, **filters):
        """
        Quest api - metadata for quests
        """
        return cls.get_resource('quest/{0}', region, *[id], **filters)

    @classmethod
    def get_realm_status(cls, region, **filters):
        """
        Realm status api - realm status for region
        """
        return cls.get_resource('realm/status', region, **filters)

    @classmethod
    def get_recipe(cls, region, id, **filters):
        """
        Recipe api - recipe details
        """
        return cls.get_resource('recipe/{0}', region, *[id], **filters)

    @classmethod
    def get_spell(cls, region, id, **filters):
        """
        Spell api - spell details
        """
        return cls.get_resource('spell/{0}', region, *[id], **filters)

    @classmethod
    def get_zones(cls, region, **filters):
        """
        Zone api - all supported zones and bosses
        """
        return cls.get_resource('zone/', region, **filters)

    @classmethod
    def get_zone(cls, region, id, **filters):
        """
        Zone api - zone details
        """
        return cls.get_resource('zone/{0}', region, *[id], **filters)

    @classmethod
    def get_battlegroups(cls, region, **filters):
        """
        Data resources api - all battlegroups
        """
        return cls.get_resource('data/battlegroups/', region, **filters)

    @classmethod
    def get_character_races(cls, region, **filters):
        """
        Data resources api - all character races
        """
        return cls.get_resource('data/character/races', region, **filters)

    @classmethod
    def get_character_classes(cls, region, **filters):
        """
        Data resources api - all character classes
        """
        return cls.get_resource('data/character/classes', region, **filters)

    @classmethod
    def get_character_achievements(cls, region, **filters):
        """
        Data resources api - all character achievements
        """
        return cls.get_resource('data/character/achievements', region, **filters)

    @classmethod
    def get_guild_rewards(cls, region, **filters):
        """
        Data resources api - all guild rewards
        """
        return cls.get_resource('data/guild/rewards', region, **filters)

    @classmethod
    def get_guild_perks(cls, region, **filters):
        """
        Data resources api - all guild perks
        """
        return cls.get_resource('data/guild/perks', region, **filters)

    @classmethod
    def get_guild_achievements(cls, region, **filters):
        """
        Data resources api - all guild achievements
        """
        return cls.get_resource('data/guild/achievements', region, **filters)

    @classmethod
    def get_item_classes(cls, region, **filters):
        """
        Data resources api - all item classes
        """
        return cls.get_resource('data/item/classes', region, **filters)

    @classmethod
    def get_talents(cls, region, **filters):
        """
        Data resources api - all talents, specs and glyphs for each class
        """
        return cls.get_resource('data/talents', region, **filters)

    @classmethod
    def get_pet_types(cls, region, **filters):
        """
        Data resources api - all pet types
        """
        return cls.get_resource('data/pet/types', region, **filters)
