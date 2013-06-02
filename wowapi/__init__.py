__version__ = '0.1'


from .api import (
    get_auctions, get_item, get_item_set, get_character, get_pet_abilities,
    get_pet_species, get_pet_stats, get_realm_leaderboard,
    get_region_leaderboard, get_guild_profile, get_arena_team,
    get_arena_ladder, get_rated_battleground_ladder, get_quest,
    get_realm_status, get_recipe, get_spell, get_battlegroups,
    get_character_races, get_character_classes, get_character_achievements,
    get_guild_rewards, get_guild_perks, get_guild_achievements,
    get_item_classes, get_talents, get_pet_types
)


# Set default logging handler to avoid "No handler found" warnings.
# Took from Python Request. Thanks Kenneth Reitz!
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())