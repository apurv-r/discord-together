from discord import ClientException

class InvalidChannelID(ClientException):
    """Raised when an invalid channel ID was entered."""
    pass

class InvalidActivityChoice(ClientException):
    """Raised when an invalid activity choice was entered."""
    pass