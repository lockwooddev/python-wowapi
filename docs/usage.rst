Usage
=====

.. py:module:: wowapi

Read here about using python-wowapi after setting it up.


API Endpoints
=============

All the endpoints of the Community API are implemented in this library.

Every endpoint returns a resource object with a bunch of attributes that are
acquired from the first level of keys of the APIs json response.

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
--------

.. function:: get_auctions(host, realm_slug)

Returns an ``AuctionResource`` for the selected realm.

::

    >>> resource = wowapi.get_auctions('eu.battle.net', 'defias-brotherhood')

    >>> resource
    <wowapi.resources.AuctionResource object at 0x104853c90>

This endpoint does not directly fetch all the auction data. First it fetches an overview page with
an url to the auctions resource and a last modified timestamp.

It sets the following attributes on the instance:

- ``last_modified`` js timestamp of last update.
- ``url`` uri to actual auction data.

Fetch auctions
^^^^^^^^^^^^^^

.. py:method:: AuctionResource.is_new(last_timestamp=None, fetch=False)

This method will check if the timestamp argument given is smaller than the timestamp from the
instance ``last_modified``.

::

    >>> resource.last_modified
    1000

    >>> resource.is_new(999)
    True, {"realm": {"name":"Defias Brotherhood", "slug":"defias-brotherhood"}..}

    >>> resource.is_new(2000)
    False, None


If ``is_new`` is successfully evaluated, then you can also access ``resource.auction_data``

Download auctions directly
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:method:: AuctionResource.download_auctions()

This method directly downloads the auctions.

::

    >>> resource.download_auctions()
    {
        "realm": {
            "name":"Defias Brotherhood",
            "slug":"defias-brotherhood"
        },
        "auctions": {
            "auctions":[
                {"auc":1,"item":1,"owner":"p1","bid":1,"buyout":1, "quantity":1,"timeLeft":"SHORT"},
                {"auc":2,"item":1,"owner":"p2","bid":1,"buyout":1, "quantity":1,"timeLeft":"SHORT"},
                {"auc":3,"item":1,"owner":"p3","bid":1,"buyout":1, "quantity":1,"timeLeft":"SHORT"},
            ]
        },
    }


Items
-----

Returns an ``ItemResource`` of an individual item.

.. function:: get_item(host, item_id, locale=None)

::

    resource = wowapi.get_item('eu.battle.net', '9999')

    # locale filter
    resource = wowapi.get_item('eu.battle.net', '9999', locale='de_DE')


Item sets
---------

Returns an ``ItemSetResource`` of an individual item set.

.. function:: get_item_set(host, set_id, locale=None)

::

    resource = wowapi.get_item_set('eu.battle.net', '1060')


Character Profile
-----------------

Returns a ``CharacterResource`` of an individual character.

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
-------------

Returns a ``PetAbilitiesResource`` of an individual pet ability.

.. function:: get_pet_abilities(host, ability_id, locale=None)

::

    resource = wowapi.get_pet_abilities('eu.battle.net', '100')


Pet species
-----------

Returns a ``PetSpeciesResource`` of an individual pet species.

.. function:: get_pet_species(host, species_id, locale=None)

::

    resource = wowapi.get_pet_species('eu.battle.net', '258')


Pet stats
---------

Returns a ``PetStatsResource`` of an individual pet species.

.. function:: get_pet_stats(host, species_id, locale=None, level=1, breedId=3, qualityId=1)

extra filters:

- ``level`` the pets level.
- ``breedId`` the Pet's breed.
- ``qualityId`` The Pet's quality.

::

    resource = wowapi.get_pet_stats('eu.battle.net', '258')


Realm Leaderboard
-----------------

Returns a ``RealmLeaderboardResource`` of all challenges on an individual
realm.

.. function:: get_realm_leaderboard(host, realm_slug, locale=None)

::

    resource = wowapi.get_realm_leaderboard('eu.battle.net', 'silvermoon')


Region Leaderboard
------------------

Returns a ``RegionLeaderboardResource`` of the top 100 challenge results for
the region.

.. function:: get_region_leaderboard(host, locale=None)

::

    resource = wowapi.get_region_leaderboard('eu.battle.net')


Guild Profile
-------------

Returns a ``GuildProfileResource`` of an individual guild.

.. function:: get_guild_profile(host, realm_slug, guild_name, locale=None, fields=[extra fields])

extra fields:

- ``members``
- ``achievements``
- ``news``
- ``challenge``

::

    resource = wowapi.get_guild_profile('eu.battle.net', 'khadgar', 'Guildname')


Arena Team
----------

Returns an ``ArenaTeamResource`` of an individual arena team.

.. function:: get_arena_team(host, realm_slug, team_size, team_name, locale=None)

``team_size`` options:

- ``2v2``
- ``3v3``
- ``5v5``

::

    resource = wowapi.get_arena_team('eu.battle.net', 'silvermoon', '2v2', 'teamname')


Arena Ladder
------------

Returns an ``ArenaLadderResource`` of an individual battlegroup.

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
-------------------------

Returns a ``BattleGroundLadderResource`` of an individual region.

.. function:: get_rated_battleground_ladder(host, locale=None, page=1, size=50, asc=True)

Extra filters:

- ``page`` which page of results to show.
- ``size`` how many results to return per page.
- ``asc`` whether to return the results in ascending order.

::

    resource = wowapi.get_rated_battleground_ladder('eu.battle.net')


Quest
-----

Returns a ``QuestResource`` of an individual quest.

.. function:: get_quest(host, quest_id, locale=None)

::

    resource = wowapi.get_quest('eu.battle.net', '8743')


Realm Status
------------

Returns a ``RealmStatusResource`` of all realms in the region.

.. function:: get_realm_status(host, locale=None)

::

    resource = wowapi.get_realm_status('eu.battle.net')


Recipe
------

Returns a ``RecipeResource`` of an individual recipe.

.. function:: get_recipe(host, recipe_id, locale=None)

::

    resource = wowapi.get_recipe('eu.battle.net', '74723')


Spell
-----

Returns a ``SpellResource`` of an individual spell.

.. function:: get_spell(host, spell_id, locale=None)

::

    resource = wowapi.get_spell('eu.battle.net', '20577')




Data Resources
==============

Another part of the API are the data endpoints. The data stored behind these
endpoints can be connected to data from other endpoints.

The data endpoints all return a ``DataResource`` with attributes from the
different datasets.

Battlegroups
------------

.. function:: get_battlegroups(host)

::

    resource = wowapi.get_battlegroups('eu.battle.net')


Character Races
---------------

.. function:: get_character_races(host, locale=None)

::

    resource = wowapi.get_character_races('eu.battle.net')


Character Classes
-----------------

.. function:: get_character_classes(host, locale=None)

::

    resource = wowapi.get_character_classes('eu.battle.net')


Character Achievements
----------------------

.. function:: get_character_achievements(host, locale=None)

::

    resource = wowapi.get_character_achievements('eu.battle.net')


Guild Rewards
-------------

.. function:: get_guild_rewards(host, locale=None)

::

    resource = wowapi.get_guild_rewards('eu.battle.net')


Guild Perks
-----------

.. function:: get_guild_perks(host, locale=None)

::

    resource = wowapi.get_guild_perks('eu.battle.net')


Guild Achievements
------------------

.. function:: get_guild_achievements(host, locale=None)

::

    resource = wowapi.get_guild_achievements('eu.battle.net')


Item Classes
------------

.. function:: get_item_classes(host, locale=None)

::

    resource = wowapi.get_item_classes('eu.battle.net')


Talents
-------

.. function:: get_talents(host, locale=None)

::

    resource = wowapi.get_talents('eu.battle.net')


Pet Types
---------

.. function:: get_pet_types(host, locale=None)

::

    resource = wowapi.get_pet_types('eu.battle.net')
