# python-wowapi


[![](https://img.shields.io/pypi/v/python-wowapi.svg)]( [![](https://img.shields.io/pypi/pyversions/:python-wowapi.svg)](https://pypi.org/project/python-wowapi/))
[![](https://img.shields.io/pypi/pyversions/python-wowapi.svg)](https://pypi.org/project/python-wowapi/)
[![Build Status](https://cloud.drone.io/api/badges/lockwooddev/python-wowapi/status.svg)](https://cloud.drone.io/lockwooddev/python-wowapi)



Python-wowapi is a client library for interacting with the World of Warcraft endpoins of the [Blizzard API](https://develop.battle.net/documentation/guides/getting-started)

Python-wowapi includes support for the following WoW API's:
* Community API
* Game data API
* Character Profile API

To interact with this library, you need to first get a client-id and client secret by registering [here](https://develop.battle.net/access)

For more information about official World of Warcraft API's visit:
* [Official API documentation](https://develop.battle.net/documentation)
* [Official API Forum](https://us.forums.blizzard.com/en/blizzard/c/api-discussion)

API documentation can be found at [python-wowapi.readthedocs.org](https://python-wowapi.readthedocs.org). Examples and installation instructions are documented here.

## Installing

```bash
pip install python-wowapi
```

## Usage example

```python
import os

from wowapi import WowApi

api = WowApi(os.environ['WOW_CLIENT_ID'], os.environ['WOW_CLIENT_SECRET'])

# Token price
api.get_token('eu', namespace='dynamic-eu', locale='de_DE')

# Playable specializations
data = api.get_playable_specializations('us', namespace='static-us')
spec_id = data['character_specializations'][0]['id']
specialization = api.get_playable_specialization('us', namespace='static-us', spec_id=spec_id)

# Character achievements
api.get_character_achievements_summary('eu', 'khadgar', 'awesomepally', 'static-eu', 'fr_FR')
```

## Data resource urls

Some endpoints return a url pointing to another resource. These urls do not include OAuth tokens. `api.get_data_resource` takes care of this.


```python
auctions_ref = api.get_auctions('eu', 'silvermoon', locale='de_DE')
api.get_data_resource(auctions_ref['files'][0]['url'], 'eu')
```

## WoW Classic API support

According to this [Forum post](https://us.forums.blizzard.com/en/blizzard/t/world-of-warcraft-classic-api-endpoints/346), Blizzard is adding support for some game data API's.

In order to use these endpoints, you need to provide the classic namespace:

```python
api.get_item_class_index('us', 'static-classic-us')
```

## Development & Testing

```bash
make devinstall
pytest
```

Alternatively you can also run the full [drone.io](https://drone.io) pipeline [locally](https://docs.drone.io/cli/install/) or [remote](https://cloud.drone.io/lockwooddev/python-wowapi/)

```bash
drone exec
```