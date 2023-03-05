"""Contains the game class
"""

from guiElements.window import WindowEvent
from pygame.sprite import Group

from settings import WHITE
from window import GameWindow
from tiles import Tile


class Game:
    """Main class for the game where all the
    events, entities and graphics will be handeled
    """

    def __init__(self, window: GameWindow) -> None:
        self.win = window

        self.event_handeler = WindowEvent()


        # sprites
        self.floor_grid = Group()


    def update(self):
        """Updates the game graphics
        """

        self.win.fill(WHITE)


        self.floor_grid.draw(self.win.canvas)

        self.win.update()


    def mainloop(self):
        """Game mainloop
        """

        Tile((100,100), (50,50), self.floor_grid)

        while self.event_handeler.getEvent("windowState"):

            # check for window events
            self.event_handeler.eventsCheck()

            # tick the window clock
            self.win.tick()


            # update the display
            self.update()
