"""
Module: loader.py
This module provides functionality for managing configuration loads
"""

import logging
import sys
from abc import abstractmethod

logger = logging.getLogger(__name__)


class ConfigLoader:
    """Loader base class.

    To create a configuration loader, create a subclass and implement the `load_config(config_class)` method
    returning a _dict_ of configuration values.

    ```python
    from pconfig.loaders import ConfigLoader

    class ConfigEnvVarLoader(ConfigLoader):
        @classmethod
        def load_config(cls, _config_class):
            return dict(os.environ)
    ```
    """

    order: int = sys.maxsize
    """ The order in which loaders will be called. Smallest first."""

    @staticmethod
    def load(config_class: "ConfigBase") -> dict[str, object]:
        """
        Call the `load_config` for all the ConfigLoader child classes,
        returning the consolidated configuration _dict_.

        # TODO change to **kwargs
        :param config_class: The configuration class to get some parameters from
        :type config_class: ConfigBase

        :return: The consolidated configuration _dict_
        :rtype: dict[str, object]
        """
        config = {}
        for loader in sorted(
            ConfigLoader.__subclasses__(),
            key=lambda loader_: loader_.order,
            reverse=True,
        ):
            config.update(loader.load_config(config_class))
        return config

    @classmethod
    @abstractmethod
    def load_config(cls, config_class: "ConfigBase") -> dict[str, object]:
        """
        Method to be implemented by the child class. Must return a _dict_ of configuration values.

        :param config_class: The configuration class to get some parameters from
        :type config_class: ConfigBase

        :return: The consolidated configuration _dict_
        :rtype: dict[str, object]
        """
        raise NotImplementedError(f"{cls.__name__} must implement this method.")
