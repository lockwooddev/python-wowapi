Python-wowapi
=============

Python-wowapi is a client library for interacting with the World of Warcraft.
Community API.

I designed the library to wrap data in python instead of returning json.
It also has to be easy and fast to use.

::

    >>> import wowapi

    >>> item = wowapi.get_item("eu.battle.net", "9999")

    >>> print item.name
    u'Black Mageweave Leggings'

::

    >>> item = wowapi.get_item("eu.battle.net", "9999", locale='de_DE')

    >>> print item.name
    u'Schwarze Magiestoffgamaschen'

For more information on the official community API visit:

- `API documentation on github <http://blizzard.github.io/api-wow-docs/>`_
- `Community Platform API Forum <http://us.battle.net/wow/en/forum/2626217/>`_

Contents:
~~~~~~~~~

.. toctree::
   :maxdepth: 2

   installation
   usage



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

