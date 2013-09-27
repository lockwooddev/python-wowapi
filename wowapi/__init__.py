__version__ = '0.1'


from .api import *


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
