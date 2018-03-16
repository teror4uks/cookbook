from cookbook.settings.base import *

try:
    from cookbook.settings.dev import *
except ImportError as e:
    from cookbook.settings.prod import *

