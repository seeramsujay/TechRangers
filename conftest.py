import sys
from unittest.mock import MagicMock

for mod_name in ["psycopg2", "psycopg2.extras", "numpy"]:
    if mod_name not in sys.modules:
        sys.modules[mod_name] = MagicMock()
