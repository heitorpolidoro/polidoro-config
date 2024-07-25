"""
This module is part of Polidoro Config.

It holds all the available loaders classes
"""

__all__ = [
    "ConfigLoader",
    "ConfigEnvVarLoader",
    "ConfigDotEnvLoader",
    "ConfigFileLoader",
]

from pconfig.loaders.dotenv_loader import ConfigDotEnvLoader
from pconfig.loaders.envvar_loader import ConfigEnvVarLoader
from pconfig.loaders.file_loader import ConfigFileLoader
from pconfig.loaders.loader import ConfigLoader
