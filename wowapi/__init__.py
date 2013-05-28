from .api import (
    get_auctions, get_item, get_item_set, get_character, get_pet_abilities,
    get_pet_species, get_pet_stats, get_realm_leaderboard,
    get_region_leaderboard
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