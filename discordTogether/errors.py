from discord import ClientException

class InvalidChannelID(ClientException):
    """Raised when an invalid channel ID was entered."""
    pass

class InvalidActivityChoice(ClientException):
    """Raised when an invalid activity choice was entered."""
    pass

class InvalidCustomID(ClientException):
    """Raised when an invalid custom application ID was entered."""
    pass

class RangeExceeded(ClientException):
    """Raised when the allowed ranges for max_age and max_uses parameters were exceeded."""
    pass
