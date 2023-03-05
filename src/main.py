from pygame import init as pinit, quit as pquit
from window import GameWindow

from settings import TITLE, FPS, SIZE

from game import Game

def main():
    """Main function where all the others are going to be called
    """

    # create the root display
    root = GameWindow(SIZE, FPS, TITLE)

    # main game object
    game = Game(root)

    game.mainloop()



if __name__ == "__main__":
    pinit()
    main()
    pquit()
