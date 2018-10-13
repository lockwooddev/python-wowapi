Python-wowapi
=============

Python-wowapi is a client library for interacting with the World of Warcraft Community API.

This library requires a client-id and client secret for the Community API OAuth client credentials flow.

For more information visit:

- `Official API documentation <https://develop.battle.net/documentation>`_
- `Official API Forum <https://us.battle.net/forums/en/bnet/15051532/>`_


Usage
-----

::

    >>> from wowapi import WowApi
    >>> api = WowApi('client-id', 'client-secret')
    >>> item = api.get_item('eu', 9999)

    {
        "id": 9999,
        "disenchantingSkillRank": 125,
        "description": "",
        "name": "Black Mageweave Leggings",
        "icon": "inv_pants_09",
        ...
    }

::

    >>> item = api.get_item('eu', 9999, locale='de_DE')

    {
        "id": 9999,
        "disenchantingSkillRank": 125,
        "description": "",
        "name": "Schwarze Magiestoffgamaschen",
        "icon": "inv_pants_09",
        ...
    }


Api endpoints
-------------

.. toctree::
   :maxdepth: 3

   modules/modules


Installation
------------

Install the package with ``pip`` in your terminal::

    pip install python-wowapi


Or install the package directly from Github::

    pip install git+https://github.com/lockwooddev/python-wowapi.git


Running tests
-------------

.. code-block:: bash

    $ make devinstall
    $ make tests


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

