"""
This module is part of Polidoro Config.

It holds all the public pconfig.config classes
"""

__all__ = [
    "ConfigBase",
    "ConfigLoader",
]

__version__ = "0.1.3"

from pconfig.config import ConfigBase
from pconfig.loaders import ConfigLoader
