Python-wowapi
=============

Python-wowapi is a client library for interacting with the World of Warcraft
Community API.

::

    >>> import wowapi

    >>> item = wowapi.get_item('eu.battle.net', '9999')

    >>> item.name
    'Black Mageweave Leggings'

::

    >>> item = wowapi.get_item('eu.battle.net', '9999', locale='de_DE')

    >>> item.name
    'Schwarze Magiestoffgamaschen'

For more information on the official community API visit:

- `Official API documentation on github <http://blizzard.github.io/api-wow-docs/>`_
- `Official Community Platform API Forum <http://us.battle.net/en/forum/#forum15051531/>`_

Contents
========

.. toctree::
   :maxdepth: 3

   installation
   usage
   exceptions
   changelog



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

