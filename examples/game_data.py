import logging
import os
from pprint import pprint

from wowapi import WowApi


logger = logging.getLogger('wowapi')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Game Data API Example')

# fetch token price for region
api = WowApi(os.environ['WOW_CLIENT_ID'], os.environ['WOW_CLIENT_SECRET'])
data = api.get_token_index('eu', namespace='dynamic-eu', locale='de_DE')
pprint(data)

# get realm list and request detail href with the get_data_resource method
data = api.get_realm_index('eu', namespace='dynamic-eu', locale='de_DE')
detail_url = data['realms'][0]['key']['href']
detail_data = api.get_data_resource(detail_url, region='eu')
pprint(detail_data)

# get playable specializations list and fetch a single specialization with the api
data = api.get_playable_specialization_index('eu', namespace='static-eu')
spec_id = data['character_specializations'][0]['id']
specialization = api.get_playable_specialization('eu', namespace='static-eu', spec_id=spec_id)
pprint(specialization)
