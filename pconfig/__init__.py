"""
This module is part of Polidoro Config.

It holds all the public pconfig.config classes
"""

__all__ = [
    "ConfigBase",
    "ConfigLoader",
]

from pconfig.config import ConfigBase
from pconfig.loaders import ConfigLoader
