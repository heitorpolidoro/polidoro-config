"""
Module: config.py

This module provides functionality for managing configurations

It allows you to load configuration settings from various sources such as
environment variables, configuration files (e.g., YAML).

The main components of this module are:

- ConfigLoader: Responsible for loading configuration data from different sources.
- ConfigError: Raised when the config is not found.
- ConfigBase: The base class to be inherited for manage the project configuration.

"""

import os


class ConfigLoader:
    """ Responsible for loading configuration data from different sources. """
    @staticmethod
    def load_dotenv(dotenv_path: str | None = None) -> bool:
        """
        Load the .env file if it is present.

        :return: A boolean indicating whether the .env file is present.
        """
        is_env_file_present = os.path.isfile(".env")
        if is_env_file_present:
            try:
                # noinspection PyPackageRequirements,PyUnresolvedReferences
                import dotenv

                dotenv.load_dotenv(dotenv_path)
                return True
            except ImportError:
                print(
                    " * Tip: There are .env file present."
                    ' Do "pip install python-dotenv" to use them.',
                )
        return False


class ConfigError(AttributeError):
    """Exception raised for errors in the configuration."""


class _ConfigMeta(type):
    """Metaclass that loads environment variables into class attributes.

    This metaclass is responsible for automatically loading environment variables and setting them as class attributes.
    It is designed to be used as the metaclass for the `ConfigBase` class.

    """

    def __init__(
        cls: type["ConfigBase"],
        what: str,
        bases: tuple[type] | None = None,
        dict_values: dict[str:object] | None = None,
    ) -> None:
        super().__init__(what, bases, dict_values)
        if what != "ConfigBase":
            ConfigLoader.load_dotenv()
            for env, value in dict_values.items():
                if not env.startswith("__"):
                    setattr(cls, env, os.getenv(env, value))
        # cls.__dict__.update(os.environ)


class ConfigBase(metaclass=_ConfigMeta):
    """
    This class is the base class for configuration classes.

    Create you config class inheriting from ConfigBase
    Ex:
    class Config(ConfigBase):
        NAME1 = VALUE1
        NAME2 = VALUE2
    """
