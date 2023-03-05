"""Contains a modified window class
"""

from pygame import display, time
from guiElements.window import Window


class GameWindow(Window):
    """Inherits from the base Window class but disables RESISING
    """

    def __init__(self,size: tuple, fps: int, title: str = "App") -> None:
        """
        The constructor of the class GameWindow
        Args:
            size: the dimensions of the canvas to be created as an attribute
            fps: the tick rate on which iteration is going to be ran
        """

        self.size = size
        self.FPS = fps
        self.title = title

        self.clock = time.Clock()

        info = display.Info()
        self.screenSize = (info.current_w, info.current_h)

        self.isFullscreen = False

        self.canvas = display.set_mode(size)
        display.set_caption(title)
