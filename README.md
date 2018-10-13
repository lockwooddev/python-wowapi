# python-wowapi

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

## Drone test runner

```
PYTHON_VERSION=3.7 drone exec
PYTHON_VERSION=3.6 drone exec
PYTHON_VERSION=3.5 drone exec
PYTHON_VERSION=2.7 drone exec
```

For more information about Drone, visit [Drone.io](https://drone.io/)
