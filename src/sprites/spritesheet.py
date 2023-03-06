from typing import Tuple

from pygame import Surface, RLEACCEL
from pygame.image import load
from pygame.transform import scale

from .exceptions import SpritesheetLoadException, ColorkeyNotDefined

class Spritesheet:
    """Contains generic spritesheet handeling methods
    """

    image: Surface
    colorkey: Tuple[int,int,int]

    @classmethod
    def load_spritesheet(cls, path: str):
        """Loads a spritesheet on the given path into memory

        Args:
            path (str): the path to the spritesheet
        """
        try:
            cls.image = load(path).convert_alpha()
        except IOError:
            print(f"ERROR {__file__}: could not load spritesheet at {path}")
            cls.image = None

    @classmethod
    def set_color_key(cls, color: Tuple[int, int, int]):
        """Defines the color key value to the given color

        Args:
            color (Tuple[int,int,int]): the colorkey value

        Raises:
            ValueError: If the given color is not a tuple of 3
            integers or if it's values are not in [0,255]
        """

        if len(color) != 3:
            raise ValueError("Color value must be in RGB [0,255]")

        if not 0 <= color[0] <= 255:
            raise ValueError("Color value must be in RGB [0,255]")

        if not 0 <= color[1] <= 255:
            raise ValueError("Color value must be in RGB [0,255]")

        if not 0 <= color[2] <= 255:
            raise ValueError("Color value must be in RGB [0,255]")

        cls.colorkey = color

    @staticmethod
    def load_debug_texture(surface: Surface):
        """Loads the classic black and magenta debug texture on the given surface

        Args:
            surface (Surface): the surface to draw the texture into
        """
        size = surface.get_width(), surface.get_height()

        # load basic texture
        surface.fill((0, 0, 0), (0, 0, size[0]//2, size[1]//2))
        surface.fill((0, 0, 0), (size[0]//2, size[1]//2, size[0], size[1]))
        surface.fill((255, 0, 255), (size[0]//2, 0, size[0], size[1]//2))
        surface.fill((255, 0, 255), (0,size[1]//2,size[0]//2,size[1]))

    @classmethod
    def load_sprite(cls, surface: Surface, sprite_coords: Tuple[int, int, int, int]):
        """Loads a sprite from the spritesheet to the given surface

        Args:
            surface (Surface): the surface where to draw the sprite on
            sprite_coords (Tuple[int, int, int, int]): the sprite coordinates on the spritesheet

        Raises:
            SpritesheetLoadException: If an error occured while loading the spritesheet
            AttributeError: If the spritesheet was not loaded
        """

        if cls.image is None:
            raise SpritesheetLoadException("Spritesheet is not loaded")

        if len(sprite_coords) != 4:
            raise ValueError("Sprite coords must be a tuple of 4 integers")

        sprite = Surface(sprite_coords[2:])

        sprite.blit(cls.image, (0,0), sprite_coords)

        scale(sprite, surface.get_size(), surface)

        try:
            surface.set_colorkey(cls.colorkey, RLEACCEL)
        except AttributeError:
            raise ColorkeyNotDefined("Color key was not defined") from AttributeError
