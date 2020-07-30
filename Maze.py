import turtle


class Maze():
    """ This class creates a random maze """

    def __init__(self):
        self.s = turtle.Screen()
        self.turtle = turtle.Turtle()
        scr = turtle.Screen()
        self.s.bgcolor("blue")
        self.s.setup(width=400,height=400)
        self.matrix = [[1 for i in range(20)] for j in range(20)]

