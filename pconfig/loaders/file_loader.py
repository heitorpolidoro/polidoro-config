"""
Module: file_loader.py
This module provides functionality for load configuration from file
"""

import logging
from abc import abstractmethod
from pathlib import PosixPath

from pconfig.config import ConfigBase
from pconfig.error import ConfigError
from pconfig.loaders.loader import ConfigLoader

logger = logging.getLogger(__name__)


try:
    import yaml
except ImportError:
    yaml = None


class ConfigFileLoader(ConfigLoader):
    """Load configuration from file."""

    @classmethod
    def load_config(cls, config_class: "ConfigBase") -> dict[str, object]:
        config = {}
        for file_loader in sorted(
            ConfigFileLoader.__subclasses__(), key=lambda loader_: loader_.order
        ):
            if config_file := getattr(config_class, "_config_file_path", None):
                if isinstance(config_file, PosixPath):
                    config_file = config_file.name
                if config_file and file_loader.is_match(config_file):
                    content = file_loader.get_content(config_file)
                    data = file_loader.get_data(content)
                    config.update(data)
        return config

    @classmethod
    @abstractmethod
    def is_match(cls, file_path: str) -> bool:
        """Returns if the file is a match for the ConfigFileLoader"""
        raise NotImplementedError(f"{cls.__name__} must implement this method.")

    @classmethod
    @abstractmethod
    def get_content(cls, file_path: str) -> str:
        """Loads the configuration data from file"""
        raise NotImplementedError(f"{cls.__name__} must implement this method.")

    @classmethod
    @abstractmethod
    def get_data(cls, content: str) -> dict[str, object]:
        """Loads the configuration data from file"""
        raise NotImplementedError(f"{cls.__name__} must implement this method.")


class ConfigYAMLLoader(ConfigFileLoader):
    """Load configuration from YAML file."""

    @classmethod
    def is_match(cls, file_path: str | PosixPath) -> bool:
        return file_path.endswith(".yml") or file_path.endswith(".yaml")

    @classmethod
    def get_content(cls, file_path: str) -> str:
        with open(file_path, "r") as file:
            data = file.read()
        return data

    @classmethod
    def get_data(cls, content: str) -> dict[str, object]:
        if yaml is None:
            raise ConfigError(
                "Must install pyyaml to use this feature. `pip install pyyaml`"
            )
        return yaml.safe_load(content)
