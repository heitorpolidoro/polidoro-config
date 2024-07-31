class ConfigError(AttributeError):
    """Raised when the config attribute is not found."""


class MissingParameters(AttributeError):
    """Raised when some parameters are missing."""
