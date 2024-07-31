"""
Module: dotenv_loader.py
This module provides functionality for load configuration from dotenv files
"""

import os
import sys

from pconfig.loaders.loader import ConfigLoader


class ConfigEnvVarLoader(ConfigLoader):
    """Load the configuration values from environment variables."""

    order = -sys.maxsize

    @classmethod
    def load_config(cls) -> dict[str, object]:
        """Return the environment variables as `dict`

        Returns:
            The configuration `dict`
        """
        return dict(os.environ)
