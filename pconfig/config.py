"""
Module: config.py
This module provides functionality for managing configurations
It allows you to load configuration settings from various sources such as
environment variables, configuration files (e.g., YAML).
"""

import json
import logging

from pconfig.config_value import ConfigValue
from pconfig.loaders.loader import load_configs

try:
    from pydantic import BaseModel
except ImportError:
    BaseModel = None

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
        params = {
            key: value for key, value in vars(cls).items() if not key.startswith("__")
        }
        config = load_configs(**params)
        for attr, value in (attributes or {}).items():
            if attr.startswith("__"):
                continue
            new_value = config.get(attr, value)
            if isinstance(value, ConfigValue):
                if not isinstance(new_value, ConfigValue):
                    if not isinstance(new_value, dict):
                        new_value = json.loads(new_value)
                    new_value = value.update(new_value)
            elif BaseModel and isinstance(value, BaseModel):
                new_value = value.__class__.model_validate(new_value)
            setattr(cls, attr, new_value)

    def __repr__(cls) -> str:
        attributes = ", ".join(
            f"{k}={repr(v)}" for k, v in cls.__dict__.items() if not k.startswith("_")
        )
        return f"{cls.__name__}({attributes})"


class ConfigBase(metaclass=_ConfigMeta):
    """A base class for configuration classes.
    To use it, create a subclass and define your settings as class attributes.
    ::

        from pconfig.config import ConfigBase

        class Config(ConfigBase):
            DB_HOST = "localhost"
            ENVIRONMENT = "development"
            ...

    These attributes will be overridden in the class creation calling the
    :meth:`load_configs() <pconfig.loaders.loader.load_configs>` method.

    You can create more complex configurations  using the :meth:`ConfigValue()` class like:
    ::

        from pconfig.config import ConfigBase, ConfigValue

        class Config(ConfigBase):
            ENV = "dev"
            features = ConfigValue(feat1=True, feat2=False)
            ...

    Then access use:
    ::

        Config.features.feat1 == True
        Config.features.feat2 == False

    To update these values the easiest way is using the :class:`ConfigEnvVarLoader <pconfig.loaders.ConfigEnvVarLoader>`
    but you can also update using a JSON, like:

    .. code-block:: bash

        features='{"feat2": true}'

    To enable the ``feat2``, for instance.

    """
