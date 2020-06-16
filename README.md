# python-wowapi


[![](https://img.shields.io/pypi/v/python-wowapi.svg)]( [![](https://img.shields.io/pypi/pyversions/:python-wowapi.svg)](https://pypi.org/project/python-wowapi/))
[![](https://img.shields.io/pypi/pyversions/python-wowapi.svg)](https://pypi.org/project/python-wowapi/)
[![Build Status](https://cloud.drone.io/api/badges/lockwooddev/python-wowapi/status.svg)](https://cloud.drone.io/lockwooddev/python-wowapi)



Python-wowapi is a client library for interacting with the World of Warcraft endpoins of the [Blizzard API](https://develop.battle.net/documentation/guides/getting-started)

Python-wowapi includes support for the following WoW API's:
* Game data API
* Character Profile API

To interact with this library, you need to first get a client-id and client secret by [registering](https://develop.battle.net/access) your application.

For more information about official World of Warcraft API's visit:
* [Official API documentation](https://develop.battle.net/documentation)
* [Official API Forum](https://us.forums.blizzard.com/en/blizzard/c/api-discussion)

## API Docs

For examples and all available endpoints, visit the [API Documentation](docs/api.md)

## Installing

```bash
pip install python-wowapi
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

To build the docs:

```bash
make docinstall
make docs
```
