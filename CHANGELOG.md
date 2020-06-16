# Changelog

## 4.0.0 (15-06-2020)

* Deprecate Community API
* Update Data & Profile API and missing endpoints


## 3.0.0

* Split community, game data and profile API's into separate mixins
* Add flake8 and isort to test requirements
* Drop support for python 2.7
* Changes in game data endpoints:
    * `get_races` became `get_playable_race_index`
    * `get_race` became `get_playable_race`
    * `get_connected_realms` became `get_connected_realm_index`
    * `get_mythic_keystone_dungeon` became `get_mythic_keystone_dungeon_index`
    * `get_mythic_keystones` became `get_mythic_keystone_index`
    * `get_mythic_keystone_periods` became `get_mythic_keystone_period_index`
    * `get_mythic_keystone_seasons` became `get_mythic_keystone_season_index`
    * `get_mythic_keystone_leaderboards` became `get_mythic_keystone_leaderboard_index`
    * `get_playable_specializations` became `get_playable_specialization_index`
    * `get_power_types` became `get_power_type_index`
    * `get_realms` became `get_realm_index`
    * `get_regions` became `get_region_index`
    * `get_token` became `get_token_index`
    * new achievments endpoints
    * new creatures endpoints
    * new guild endpoints
    * new guild crest endpoints
    * new item endpoints
    * new mount endpoints
    * new pets endpoints
    * new pvp endpoints
    * new quest endpoints
    * new pvp season endpoints
    * new pvp tier endpoints
    * new titles endpoints
* Changes in profile endpoints:
    * new character achievements endpoint
    * new character appearance endpoint
    * new character equipment endpoint
    * new character media endpoint
    * new character profile endpoint
    * new character pvp endpoints
    * new character specialization endpoint
    * new character statistics endpoint
    * new character titles endpoint
* Changes in community endpoints:
    * new `get_oauth_profile` endpoint


## 2.3.1 (20-05-2019)

* Added some leeway protection against expired tokens


## 2.3.0 (06-05-2019)

* Add profile api


## 2.2.1 (16-02-2019)

* Add functionality to retry failed connections


## 2.2.0 (25-12-2018)

* Add new Game Data API's


## 2.1.0 (13-12-2018)

* Add Game Data API methods
* Token handling per region


## 2.0.1 (Unreleased)

* Add drone cloud support for CI
* Bump requests library to 2.20.1
* Change packaging with setup.py


## 2.0.0 (14-10-2018)

* Deprecate 1.0 WowApi
* Implement client credentials flow for OAuth authentication
* Add dronefile for testing against multiple python versions
* Add coverage to pytest
* Add logging
