"""Contains the tile class
"""

from typing import Tuple

from pygame.sprite import Sprite, Group
from pygame import Surface
from pygame.draw import line

class Tile(Sprite):

    def __init__(self, pos: Tuple[int, int], size: Tuple[int, int], *groups: Group) -> None:
        super().__init__(*groups)

        self.image = Surface((size[0], size[1]))
        self.image.fill((0,0,0))

        # hitbox
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]


    def draw_surface(self):
        line(self.image, (255,255,255), )
