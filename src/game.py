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

    
    def load_assets(self):
        """Loads the game assets before the mainloop
        """

        Spritesheet.load_spritesheet(SPRITESHEET_PATH)
        Spritesheet.set_color_key((0,0,0))
        
        Tile.set_screen_offset((self.win.size[0] // 2, self.win.size[1] // 2))
        print(Tile.screen_offset)


    def update(self):
        """Updates the game graphics
        """

        self.win.fill(WHITE)


        self.floor_grid.draw(self.win.canvas)

        self.win.update()


    def mainloop(self):
        """Game mainloop
        """

        self.load_assets()

        # quick map
        for i in range(-4, 4):
            for j in range(-4, 4):
                Tile((i,j), (96,96), self.floor_grid, sprite_coords=(0,0,32,32))


        # mainloop
        while self.event_handeler.getEvent("windowState"):

            # check for window events
            self.event_handeler.eventsCheck()

            # tick the window clock
            self.win.tick()


            # update the display
            self.update()
