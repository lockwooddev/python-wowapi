Usage
=====

.. py:module:: wowapi

Read here about using python-wowapi after setting it up.


API Resources
------------

All the endpoints of the Community API are implemented in this library.

Every endpoint returns a resource object. Depending on the type of resource,
the data attributes are set on the object based on the dataset.

Example with an ItemResource::

    >>> import wowapi

    >>> resource = wowapi.get_item('eu.battle.net', '9999')

    >>> resource
    <wowapi.resources.ItemResource object at 0x100e51bd0>

    >>> dir(resource)
    [...
    'armor', 'baseArmor', 'bonusStats', 'buyPrice', 'containerSlots', 'data',
    'description', 'disenchantingSkillRank', 'displayInfoId', 'equippable',
    'hasSockets', 'heroicTooltip', 'icon', 'id', 'inventoryType',
    'isAuctionable','itemBind', 'itemClass', 'itemLevel', 'itemSource',
    'itemSpells', 'itemSubClass', 'maxCount', 'maxDurability', 'minFactionId',
    'minReputation', 'name', 'nameDescription', 'nameDescriptionColor',
    'quality', 'requiredLevel', 'requiredSkill', 'requiredSkillRank',
    'sellPrice', 'stackable', 'upgradable']


Auctions
~~~~~~~~

.. function:: get_auctions(host, realm_slug)

Returns an auction resource for the selected realm.

::

    >>> resource = wowapi.get_auctions('eu.battle.net', 'defias-brotherhood')

    >>> resource
    <wowapi.resources.AuctionResource object at 0x104853c90>

This endpoint does not directly fetch all the auctions data. It creates the
following data attributes on the ``AuctionResource`` instance:

- ``last_modified`` js timestamp of last update.
- ``url`` uri to actual auctions data.

This in between step allows API developers to compare timestamps between
previous requested data.

::

    # returns true, fetches auctions and ignores the timestamp check.
    resource.is_new()

    # checks if your given timestamp is older. If True, the data is requested
    # and extra data attributes are set on the instance.
    resource.is_new(timestamp=1369578638000)


new attributes if ``is_new()`` is ``True``:

- ``all`` list of dictionaries with all auctions and extra key ``faction``
- ``alliance`` list of dictionaries with alliance auctions
- ``horde`` list of dictionaries with horde auctions
- ``neutral`` list of dictionaries with neutral auctions
- ``realm_name`` name of realm
- ``realm_slug`` slug of realm


Items
~~~~~

.. function:: get_item(host, item_id, locale=None)

::

    resource = wowapi.get_item('eu.battle.net', '9999')

    # locale filter
    resource = wowapi.get_item('eu.battle.net', '9999', locale='de_DE')


Item sets
~~~~~~~~~

.. function:: get_item_set(host, set_id, locale=None)

::

    resource = wowapi.get_item_set('eu.battle.net', '1060')


Character Profile
~~~~~~~~~~~~~~~~~

.. function:: get_character(host, realm_slug, character_name, locale=None, fields=[extra fields])

extra fields:

- ``achievements``
- ``appearance``
- ``feed``
- ``guild``
- ``hunterPets``
- ``items``
- ``mounts``
- ``pets``
- ``petSlots``
- ``professions``
- ``progression``
- ``pvp``
- ``quests``
- ``reputation``
- ``stats``
- ``talents``
- ``titles``

::

    resource = wowapi.get_character('eu.battle.net', 'khadgar', 'player1')

    resource = wowapi.get_character('eu.battle.net', 'khadgar', 'player1', locale='de_DE')

    resource = wowapi.get_character('eu.battle.net', 'khadgar', 'player1', fields=['reputation', 'titles'])


Pet abilities
~~~~~~~~~~~~~

.. function:: get_pet_abilities(host, ability_id, locale=None)

::

    resource = wowapi.get_pet_abilities('eu.battle.net', '100')


Pet species
~~~~~~~~~~~

.. function:: get_pet_species(host, species_id, locale=None)

::

    resource = wowapi.get_pet_species('eu.battle.net', '258')


Pet stats
~~~~~~~~~

.. function:: get_pet_stats(host, species_id, locale=None, level=1, breedId=3, qualityId=1)

extra filters:

- ``level`` the pets level.
- ``breedId`` the Pet's breed.
- ``qualityId`` The Pet's quality.

::

    resource = wowapi.get_pet_stats('eu.battle.net', '258')


Realm Leaderboard
~~~~~~~~~~~~~~~~~

.. function:: get_realm_leaderboard(host, realm_slug, locale=None)

::

    resource = wowapi.get_realm_leaderboard('eu.battle.net', 'silvermoon')


Region Leaderboard
~~~~~~~~~~~~~~~~~~

.. function:: get_region_leaderboard(host, realm_slug, locale=None)

::

    resource = wowapi.get_region_leaderboard('eu.battle.net')


Guild Profile
~~~~~~~~~~~~~

.. function:: get_guild_profile(host, realm_slug, guild_name, locale=None, fields=[extra fields])

extra fields:

- ``members``
- ``achievements``
- ``news``
- ``challenge``

::

    resource = wowapi.get_guild_profile('eu.battle.net', 'khadgar', 'Guildname')


Arena Team
~~~~~~~~~~

.. function:: get_arena_team(host, realm_slug, team_size, team_name, locale=None)

``team_size`` options:

- ``2v2``
- ``3v3``
- ``5v5``

::

    resource = wowapi.get_arena_team('eu.battle.net', 'silvermoon', '2v2', 'teamname')


Arena Ladder
~~~~~~~~~~~~

.. function:: get_arena_ladder(host, battlegroup, team_size, locale=None, page=1, size=50, asc=True)

``team_size`` options:

- ``2v2``
- ``3v3``
- ``5v5``

Extra filters:

- ``page`` which page of results to show.
- ``size`` how many results to return per page.
- ``asc`` whether to return the results in ascending order.

::

    resource = wowapi.get_arena_ladder('eu.battle.net', 'ruin', '2v2')


Rated Battleground Ladder
~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: get_rated_battleground_ladder(host, locale=None, page=1, size=50, asc=True)

Extra filters:

- ``page`` which page of results to show.
- ``size`` how many results to return per page.
- ``asc`` whether to return the results in ascending order.

::

    resource = wowapi.get_rated_battleground_ladder('eu.battle.net')



Quest
~~~~~

.. function:: get_quest(host, quest_id, locale=None)

::

    resource = wowapi.get_quest('eu.battle.net', '8743')


Realm Status
~~~~~~~~~~~~

.. function:: get_realm_status(host, locale=None)

::

    resource = wowapi.get_realm_status('eu.battle.net')


Recipe
~~~~~~

.. function:: get_recipe(host, recipe_id, locale=None)

::

    resource = wowapi.get_recipe('eu.battle.net', '74723')


Spell
~~~~~

.. function:: get_spell(host, spell_id, locale=None)

::

    resource = wowapi.get_spell('eu.battle.net', '20577')




Data Resources
--------------

Another part of the API are the data endpoints. The data stored behind these
endpoints can be connected to data from other endpoints.

Battlegroups
~~~~~~~~~~~~

.. function:: get_battlegroups(host)

::

    resource = wowapi.get_battlegroups('eu.battle.net')


Character Races
~~~~~~~~~~~~~~~

.. function:: get_character_races(host, locale=None)

::

    resource = wowapi.get_character_races('eu.battle.net')


Character Classes
~~~~~~~~~~~~~~~~~

.. function:: get_character_classes(host, locale=None)

::

    resource = wowapi.get_character_classes('eu.battle.net')


Character Achievements
~~~~~~~~~~~~~~~~~~~~~~

.. function:: get_character_achievements(host, locale=None)

::

    resource = wowapi.get_character_achievements('eu.battle.net')


Guild Rewards
~~~~~~~~~~~~~

.. function:: get_guild_rewards(host, locale=None)

::

    resource = wowapi.get_guild_rewards('eu.battle.net')


Guild Perks
~~~~~~~~~~~

.. function:: get_guild_perks(host, locale=None)

::

    resource = wowapi.get_guild_perks('eu.battle.net')


Guild Achievements
~~~~~~~~~~~~~~~~~~

.. function:: get_guild_achievements(host, locale=None)

::

    resource = wowapi.get_guild_achievements('eu.battle.net')


Item Classes
~~~~~~~~~~~~

.. function:: get_item_classes(host, locale=None)

::

    resource = wowapi.get_item_classes('eu.battle.net')


Talents
~~~~~~~

.. function:: get_talents(host, locale=None)

::

    resource = wowapi.get_talents('eu.battle.net')


Pet Types
~~~~~~~~~

.. function:: get_pet_types(host, locale=None)

::

    resource = wowapi.get_pet_types('eu.battle.net')