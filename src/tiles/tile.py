"""Contains the tile class
"""

from typing import Tuple

from pygame.sprite import Sprite, Group
from pygame import Surface

from sprites import Spritesheet
from sprites import SpritesheetLoadException, ColorkeyNotDefined


class Tile(Sprite):

    def __init__(self, pos: Tuple[int, int], size: Tuple[int, int], *groups: Group, sprite_coords: Tuple[int, int, int, int] = None) -> None:
        super().__init__(*groups)

        self.image = Surface((size[0], size[1]))

        # hitbox
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

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
            print("Colorkey was not defined")
