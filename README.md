# python-wowapi

[![Build Status](https://cloud.drone.io/api/badges/lockwooddev/python-wowapi/status.svg)](https://cloud.drone.io/lockwooddev/python-wowapi)

Python-wowapi is a client library for interacting with the World of Warcraft
Community API.

Documentation about installing and usage can be found at [python-wowapi.readthedocs.org](https://python-wowapi.readthedocs.org)

## Installing

```bash
pip install python-wowapi
```

## Usage

```python
import os

from wowapi import WowApi


api = WowApi(os.environ['WOW_CLIENT_ID'], os.environ['WOW_CLIENT_SECRET'])
data = api.get_auctions('eu', 'silvermoon', locale='de_DE')
print(data)
```

## Development & Testing

```bash
pip install -e .
pip install -e .[tests]
py.test
```
