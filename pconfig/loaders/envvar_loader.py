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
    def load_config(cls, config_class: "ConfigBase") -> dict[str, object]:
        """
         Return the environment variables as _dict_

        :param config_class: The configuration class to get some parameters from
        :type config_class: ConfigBase

        :return: The consolidated configuration _dict_
        :rtype: dict[str, object]
        """
        return dict(os.environ)
