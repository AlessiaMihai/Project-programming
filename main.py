
import pyxel
from Chef import Chef


class Game:

    def __init__(self):

        pyxel.init(256, 256, title="Cooking Game")

        # Load the sprites
        pyxel.load("assets/resources.pyxres")

        # Create the two chefs
        self.chef1 = Chef("up")
        self.chef2 = Chef("down")

        pyxel.run(self.update, self.draw)

    def update(self):

        self.chef1.update()
        self.chef2.update()

    def draw(self):

        pyxel.cls(7)

        # Draw both chefs
        self.chef1.draw()
        self.chef2.draw()


Game()
