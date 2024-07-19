"""
Module: config.py
This module provides functionality for managing configurations
It allows you to load configuration settings from various sources such as
environment variables, configuration files (e.g., YAML).
"""

import logging
import os

logger = logging.getLogger(__name__)

try:
    import dotenv
except ImportError:
    dotenv = None
    logger.info(
        "There's a .env file present but python-dotenv is not installed. Run 'pip install python-dotenv' to use it."
    )


class ConfigError(AttributeError):
    """Raised when the config attribute is not found."""


class ConfigLoader:
    """Loads configuration data from various sources like .env files or environment variables."""

    @staticmethod
    def load_dotenv(dotenv_path: str | None = None) -> bool:
        """
        Load a .env file into environment variables.
        :return: A boolean indicating whether the .env file is successfully loaded.
        """
        if dotenv and os.path.isfile(".env"):
            dotenv.load_dotenv(dotenv_path)
            return True
        return False


class _ConfigMeta(type):
    """Metaclass that loads environment variables into class attributes."""

    def __init__(
        cls: type["ConfigBase"],
        name: str,
        bases: tuple[type] | None = None,
        attributes: dict[str, object] | None = None,
    ) -> None:
        super().__init__(name, bases, attributes)
        ConfigLoader.load_dotenv()
        for attr, value in (attributes or {}).items():
            if attr.isupper():
                setattr(cls, attr, os.getenv(attr, value))


class ConfigBase(metaclass=_ConfigMeta):
    """
    A base class for configuration classes.
    To use, create a subclass and define your settings as class attributes.
    Ex:
    class Config(ConfigBase):
        NAME1 = VALUE1
        NAME2 = VALUE2
    These attributes will be automatically overridden by environment variables of the same name.
    """
