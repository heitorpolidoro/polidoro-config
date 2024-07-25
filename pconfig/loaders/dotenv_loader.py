"""
Module: dotenv_loader.py
This module provides functionality for load configuration from dotenv files
"""

import logging
import os

from pconfig.loaders.envvar_loader import ConfigEnvVarLoader
from pconfig.loaders.loader import ConfigLoader

logger = logging.getLogger(__name__)


try:
    import dotenv
except ImportError:
    dotenv = None
    if os.path.isfile(".env"):
        logger.info(
            "There's a .env file present but python-dotenv is not installed. Run 'pip install python-dotenv' to use it."
        )


class ConfigDotEnvLoader(ConfigLoader):
    """Load a .env file into environment variables."""

    order = 1

    @classmethod
    def load_config(cls, config_class: "ConfigBase") -> dict[str,object]:
        """
        Load a .env file into environment variables.
        :return: A boolean indicating whether the .env file is successfully loaded.
        """
        if dotenv and os.path.isfile(".env"):
            dotenv.load_dotenv(os.getenv("CONFIG_ENV"))
        return ConfigEnvVarLoader.load_config(config_class)
