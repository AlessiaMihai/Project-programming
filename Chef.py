
import pyxel


class Chef:
    """Class representing the two chefs in the game."""

    def __init__(self, side: str):
        """Initialize a chef depending on its side."""

        self.side = side
        self.speed = 2

        self.width = 16
        self.height = 16

        if side == "up":
            # Chef 1: upper side
            self.x = 120
            self.y = 50

            self.min_y = 0
            self.max_y = 128 - self.height

            self.x_image = 0
            self.y_image = 0

        elif side == "down":
            # Chef 2: lower side
            self.x = 120
            self.y = 178

            self.min_y = 128
            self.max_y = 256 - self.height

            self.x_image = 128
            self.y_image = 0

        else:
            raise ValueError("Side must be 'up' or 'down'")

    def update(self):
        """Move the chef using the keyboard."""

        if self.side == "up":

            # Chef 1: WASD
            if pyxel.btn(pyxel.KEY_W):
                self.y -= self.speed
            if pyxel.btn(pyxel.KEY_S):
                self.y += self.speed
            if pyxel.btn(pyxel.KEY_A):
                self.x -= self.speed
            if pyxel.btn(pyxel.KEY_D):
                self.x += self.speed

        elif self.side == "down":

            # Chef 2: Arrow keys
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= self.speed
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += self.speed
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= self.speed
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += self.speed

        # Keep the chef inside its own half
        self.y = max(self.min_y, min(self.y, self.max_y))

        # Keep the chef inside the screen horizontally
        self.x = max(0, min(self.x, 256 - self.width))

    def draw(self):
        """Draw the chef."""

        pyxel.blt(
            self.x, self.y,
            0,
            self.x_image, self.y_image,
            self.width, self.height,
            0
        )
