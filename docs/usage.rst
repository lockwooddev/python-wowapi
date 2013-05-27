Usage
=====

.. py:module:: wowapi

Read here about using python-wowapi after setting it up.


Resources
---------


Auctions
~~~~~~~~

.. function:: get_auctions(host, realm_slug)

::

    resource = get_auctions('eu.battle.net', 'khadgar')


Items
~~~~~

.. function:: get_item(host, item_id, locale=None)

::

    resource = get_item('eu.battle.net', '9999')

    # locale filter
    resource = get_item('eu.battle.net', '9999', locale='de_DE')


Character
~~~~~~~~~

.. function:: get_character(host, realm_slug, character_name, locale=None, fields=None)

::

    resource = get_character('eu.battle.net', 'khadgar', 'player1')

    resource = get_character('eu.battle.net', 'khadgar', 'player1', locale='de_DE')

    resource = get_character('eu.battle.net', 'khadgar', 'player1', fields=['reputation', 'titles'])