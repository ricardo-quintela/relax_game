"""Contains the game class
"""

from guiElements.window import WindowEvent
from pygame.sprite import Group

from settings import WHITE, SPRITESHEET_PATH
from window import GameWindow
from tiles import Tile

from sprites import Spritesheet


class Game:
    """Main class for the game where all the
    events, entities and graphics will be handeled
    """

    def __init__(self, window: GameWindow) -> None:
        self.win = window

        self.event_handeler = WindowEvent()


        # sprites
        self.floor_grid = Group()

    
    def load_resources(self):
        """Loads the game resources before the mainloop
        """

        Spritesheet.load_spritesheet(SPRITESHEET_PATH)
        Spritesheet.set_color_key((255,0,255))


    def update(self):
        """Updates the game graphics
        """

        self.win.fill(WHITE)


        self.floor_grid.draw(self.win.canvas)

        self.win.update()


    def mainloop(self):
        """Game mainloop
        """

        self.load_resources()

        Tile((100,100), (128,128), self.floor_grid, sprite_coords=(0,0,32,32))

        # mainloop
        while self.event_handeler.getEvent("windowState"):

            # check for window events
            self.event_handeler.eventsCheck()

            # tick the window clock
            self.win.tick()


            # update the display
            self.update()
