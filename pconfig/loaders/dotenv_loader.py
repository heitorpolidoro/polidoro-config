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

    order = 0

    @classmethod
    def load_config(cls, file_path: str | None = None) -> dict[str, object]:
        """Load a .env file into environment variables.

        Args:
            file_path: .env style file path. Optional.

        Returns:
            The configuration `dict`
        """
        file_path = os.getenv("CONFIG_ENV", file_path or ".env")
        config = {}
        if dotenv and os.path.isfile(file_path):
            current = dict(os.environ)
            dotenv.load_dotenv(file_path)
            config = ConfigEnvVarLoader.load_config()
            config = dict(set(config.items()) - set(current.items()))
        return config
