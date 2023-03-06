"""Contains the tile class
"""

from typing import Tuple

from numpy import ndarray, array, matmul, int16
from numpy.linalg import inv
from pygame import Surface
from pygame.sprite import Sprite, Group

from sprites import Spritesheet
from sprites import SpritesheetLoadException, ColorkeyNotDefined

from .exceptions import UndefinedScreenOffset


class Tile(Sprite):
    """Handles tile behaviour and plane transformations
    A tile has a sprite
    """

    transf_matrix = array([[0.5, -0.5], [0.25, 0.25]])
    inv_matrix = inv(transf_matrix)

    screen_offset: Tuple[int, int]

    def __init__(
            self,
            pos: Tuple[int, int],
            size: Tuple[int, int],
            *groups: Group,
            sprite_coords: Tuple[int, int, int, int] = None
        ) -> None:
        super().__init__(*groups)

        self.image = Surface(size)

        # hitbox
        self.rect = self.image.get_rect()

        self.rect.topleft = Tile.convert_isometric(pos, size)

        # load the sprite of the tile
        try:
            if sprite_coords is None:
                Spritesheet.load_debug_texture(self.image)
            else:
                Spritesheet.load_sprite(self.image, sprite_coords)

        # spritesheet was not loaded
        except SpritesheetLoadException:
            Spritesheet.load_debug_texture(self.image)

        except AttributeError:
            Spritesheet.load_debug_texture(self.image)

        except ValueError:
            Spritesheet.load_debug_texture(self.image)

        except ColorkeyNotDefined:
            pass

    @classmethod
    def set_screen_offset(cls, offset_vector: Tuple[int, int]):
        """Defines the screen offset vector to the screen's center

        Args:
            offset_vector (Tuple[int, int]): the offset vector of the screen center
        """

        cls.screen_offset = offset_vector

    @staticmethod
    def convert_isometric(pos: Tuple[int, int], size: Tuple[int,int]) -> ndarray:
        """Converts a normal plane's coordinates to an isometric plane

        Args:
            pos (Tuple[int,int]): the position of the tile
            size (Tuple[int,int]): the size of the tile

        Returns:
            ndarray: the transformed coordinates in an isometric plane

        Raises:
            UndefinedScreenOffset: if the screen offset vector was not defined
        """

        trasnformed_grid = matmul(Tile.transf_matrix, pos)


        try:
            screen_offset = (
                Tile.screen_offset[0] - size[0] // 2,
                Tile.screen_offset[1] - size[1] // 2
            )

        except AttributeError:
            raise UndefinedScreenOffset("Screen offset vector was not defined") from AttributeError
        
        return trasnformed_grid * size + screen_offset


    @staticmethod
    def convert_linear(mouse_pos: Tuple[int,int], size: Tuple[int, int]) -> ndarray:
        """Convert the isometric coordinates back to linear

        Args:
            mouse_pos (Tuple[int, int]): the current isometric plane position
            size (Tuple[int, int]): the size of each tile

        Returns:
            ndarray: the original coordinates in the linear plane

        Raises:
            UndefinedScreenOffset: if the screen offset vector was not defined
        """

        try:
            screen_offset = (
                Tile.screen_offset[0] - size[0] // 2,
                Tile.screen_offset[1] - size[1] // 2
            )

        except AttributeError:
            raise UndefinedScreenOffset("Screen offset vector was not defined") from AttributeError
        
        return (matmul(Tile.inv_matrix, mouse_pos) / size).astype(int16) - screen_offset
