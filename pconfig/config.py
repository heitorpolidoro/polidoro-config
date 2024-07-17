"""
Module: config.py

This module provides functionality for managing configurations

It allows you to load configuration settings from various sources such as
environment variables, configuration files (e.g., YAML).

The main components of this module are:

- ConfigLoader: Responsible for loading configuration data from different sources.
- ConfigError: Raised when the config is not found.
- ConfigManager: Manages the loaded configuration data and provides an interface
   for accessing and modifying the configuration settings.

Example usage:

    # Default usage
    Config.DB_HOST

    # Load configuration from a YAML file
    Config.load_from_file('config.yaml')

    # Create a ConfigManager instance
    config_manager = ConfigManager()
    config_manager.set('app.debug', True)
    print(Config.app.debug)
    >> True

    # When the config is not found
    Config.NOT_FOUND
    >> ConfigError: No such environment variable with the name 'NOT_FOUND'
"""

import os


class ConfigError(AttributeError):
    """Exception raised for errors in the configuration."""


class _Config:
    """
    Documentation for class _Config:

    The _Config class provides methods for loading a .env file and retrieving environment variables.

    """

    @staticmethod
    def load_dotenv() -> bool:
        """
        Load the .env file if it is present.

        :return: A boolean indicating whether the .env file is present.
        """
        is_env_file_present = os.path.isfile(".env")
        if is_env_file_present:
            try:
                import dotenv

                dotenv.load_dotenv()
                return True
            except ImportError:
                print(
                    " * Tip: There are .env file present."
                    ' Do "pip install python-dotenv" to use them.',
                )
        return False

    def __getattr__(self, item: str) -> object:
        if item in os.environ:
            return os.environ[item]
        raise ConfigError(f"No such environment variable with the name '{item}'.")


Config = _Config()
