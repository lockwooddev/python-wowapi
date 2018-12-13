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

logger.info('Community API Example')

api = WowApi(os.environ['WOW_CLIENT_ID'], os.environ['WOW_CLIENT_SECRET'])
data = api.get_auctions('eu', 'silvermoon', locale='de_DE')
pprint(data)

data = api.get_realm_status('us')
pprint(data)
