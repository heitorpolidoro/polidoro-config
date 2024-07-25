"""
Module: config.py
This module provides functionality for managing configurations
It allows you to load configuration settings from various sources such as
environment variables, configuration files (e.g., YAML).
"""

import logging
from pathlib import PosixPath

from pconfig.loaders.loader import ConfigLoader

logger = logging.getLogger(__name__)


class _ConfigMeta(type):
    """Metaclass that loads environment variables into class attributes."""

    def __init__(
        cls: type["ConfigBase"],
        name: str,
        bases: tuple[type] | None = None,
        attributes: dict[str, object] | None = None,
    ) -> None:
        super().__init__(name, bases, attributes)
        config = ConfigLoader.load(cls)
        for attr, value in (attributes or {}).items():
            setattr(cls, attr, config.get(attr, value))


class ConfigBase(metaclass=_ConfigMeta):
    """
    A base class for configuration classes.
    To use it, create a subclass and define your settings as class attributes.

    ```python
    class Config(ConfigBase):
        DB_HOST = 'localhost'
        ENVIRONMENT = 'development'
        ...
    ```
    These attributes will be automatically overridden by environment variables of the same name.
    """
