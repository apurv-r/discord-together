class InvalidArgument(Exception):
    """Raised when an invalid argument was entered."""
    pass

class RangeExceeded(Exception):
    """Raised when the allowed ranges for max_age and max_uses parameters were exceeded."""
    pass

class BotMissingPerms(Exception):
    """Raised when your bot does not have CREATE_INSTANT_INVITE permissions."""
    pass

class ConnectionError():
    """Raised when a general error occured while communicating with Discord API."""
    pass
