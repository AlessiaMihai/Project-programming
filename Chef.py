def Chef:
    """This is a class to represent the two chefs.In the final game, there will be two characters, chef1 and chef2"""
    def __init__(self, side:str):
        """This is the __init__ function for the chefs. S string represeting the side of each of the characters is in. Chef1 will be up while chef2 will be down"""
        self.side=side

        if side=="up":
            self.x=...
            self.min_y=...
            self.max_y=...
            self.x_image=...
        else:
            self.x=..
            self.min_y

