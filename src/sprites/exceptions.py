"""Contains sprite exceptions
"""

class SpritesheetLoadException(Exception):
    """Spritesheet was not loaded
    """
    pass

class ColorkeyNotDefined(Exception):
    """Colorkey was not defined
    """
    pass
