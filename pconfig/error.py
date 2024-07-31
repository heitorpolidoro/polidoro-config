"""
Module: error.py

This module contains all the exceptions for pconfig.
"""


class ConfigError(AttributeError):
    """Raised when the config attribute is not found."""


class MissingParameters(AttributeError):
    """Raised when some parameters are missing."""
