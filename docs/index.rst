Python-wowapi
=============

Python-wowapi is a client library for interacting with the World of Warcraft
Community API.

::

    >>> import wowapi

    >>> item = wowapi.get_item('eu.battle.net', '9999')

    >>> print item.name
    u'Black Mageweave Leggings'

::

    >>> item = wowapi.get_item('eu.battle.net', '9999', locale='de_DE')

    >>> print item.name
    u'Schwarze Magiestoffgamaschen'

For more information on the official community API visit:

- `API documentation on github <http://blizzard.github.io/api-wow-docs/>`_
- `Community Platform API Forum <http://us.battle.net/wow/en/forum/2626217/>`_

Contents:
~~~~~~~~~

.. toctree::
   :maxdepth: 3

   installation
   usage
   exceptions



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

