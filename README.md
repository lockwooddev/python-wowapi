# python-wowapi


[![](https://img.shields.io/pypi/v/python-wowapi.svg)]( [![](https://img.shields.io/pypi/pyversions/:python-wowapi.svg)](https://pypi.org/project/python-wowapi/))
[![](https://img.shields.io/pypi/pyversions/python-wowapi.svg)](https://pypi.org/project/python-wowapi/)
[![Build Status](https://cloud.drone.io/api/badges/lockwooddev/python-wowapi/status.svg)](https://cloud.drone.io/lockwooddev/python-wowapi)



Python-wowapi is a client library for interacting with the World of Warcraft
Community and Game Data API.

To interact with this library, you need to first get a client-id and client secret by registering [here](https://develop.battle.net/access)

For more information about official World of Warcraft API's visit:
[Official API documentation](https://develop.battle.net/documentation)
[Official API Forum](https://us.battle.net/forums/en/bnet/15051532/)

API documentation can be found at [python-wowapi.readthedocs.org](https://python-wowapi.readthedocs.org). Examples and installation instructions are documented here.

## Installing

```bash
pip install python-wowapi
```

## API instance

```python
import os

from wowapi import WowApi

api = WowApi(os.environ['WOW_CLIENT_ID'], os.environ['WOW_CLIENT_SECRET'])
```

## Community API example

```python
api.get_auctions('eu', 'silvermoon', locale='de_DE')
```


## Game Data API examples


### Get token price
```python
api.get_token('eu', namespace='dynamic-eu', locale='de_DE')
```

### Get class specializations and detail specialization resource
```python
data = api.get_playable_specializations('us', namespace='static-us')

spec_id = data['character_specializations'][0]['id']
specialization = api.get_playable_specialization('us', namespace='static-us', spec_id=spec_id)
```

### Get game data resource by url

This example shows how to fetch a game data resource by url.
The `get_data_resource` method will take care of adding your access_token to the url.

```python
api.get_data_resource('https://eu.api.blizzard.com/data/wow/connected-realm/509?namespace=dynamic-eu', region='eu')
```


## Development & Testing

```bash
pip install -e .
pip install -e .[tests]
pytest
```
