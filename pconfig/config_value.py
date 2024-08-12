"""
Module: config_value.py
This module provides functionality for managing configurations
It allows you to load configuration settings from various sources such as
environment variables, configuration files (e.g., YAML).
"""

from typing_extensions import TypeVar

ConfigValueType = TypeVar("ConfigValue")


class ConfigValue:
    """
    A class representing a configuration value.

    This class allows updating and accessing configuration values using attribute and item notation.

    :param params: A dictionary of initial configuration values.

    Example usage
    ::

        config = ConfigValue(param1='value1', param2='value2')
        print(config.param1)  # Output: 'value1'
        print(config['param2'])  # Output: 'value2'


    """

    def __init__(self, **params) -> None:
        self._params = params

    def update(
        self, values: dict[str, object | dict] | object
    ) -> ConfigValueType | object:
        """
        Update the configuration values with new values.

        :param values: A dictionary of new values to update the configuration.
                       The keys are the parameter names and the values are the
                       corresponding new values.

                       Each value can be one of the following:
                       - An object of any type, which will be directly set as the new value.
                       - Another dictionary, representing nested configuration values.

        :return: The updated configuration object.
                 If the input values are not a dictionary, the original configuration object is returned.
        """
        if not isinstance(values, dict):
            return values
        for name, value in values.items():
            if isinstance((self_value := self[name]), ConfigValue):
                value = self_value.update(value)
            self._params[name] = value
        return self

    def __repr__(self) -> str:
        attributes = ", ".join(f"{k}={repr(v)}" for k, v in self._params.items())
        return f"{self.__class__.__name__}({attributes})"

    def __getattr__(self, item: str) -> ConfigValueType | object:
        return self._params[item]

    def __getitem__(self, item: str) -> ConfigValueType | object:
        return self._params[item]
