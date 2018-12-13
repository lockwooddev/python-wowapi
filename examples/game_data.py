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
data = api.get_token('eu', namespace='dynamic-eu', locale='de_DE')
pprint(data)

# get realm list and request detail href with the get_data_resource method
data = api.get_realms('us', namespace='dynamic-us')
detail_url = data['realms'][0]['key']['href']
detail_data = api.get_data_resource(detail_url, region='us')
pprint(detail_data)

# get playable specializations list and fetch a single specialization with the api
data = api.get_playable_specializations('us', namespace='static-us')
spec_id = data['character_specializations'][0]['id']
specialization = api.get_playable_specialization('us', namespace='static-us', spec_id=spec_id)
pprint(specialization)
