import turtle

SIZE = 400


class Maze:
    """ This class creates a random maze """

    def __init__(self):
        self.s = turtle.Screen()
        self.turtle = turtle.Turtle()
        scr = turtle.Screen()
        self.s.bgcolor("blue")
        self.s.setup(width=SIZE, height=SIZE)
        self.matrix = [[1 for i in range(20)] for j in range(20)]

    def reset(self):
        self.turtle.goto(-(SIZE / 2 - 10), SIZE / 2 - 10)
        self.matrix = [[1 for i in range(int(SIZE / 20))] for i in range(int(SIZE / 20))]
        self.s.bgcolor('blue')
        self.turtle.shape('square')
        self.turtle.color('white')
        self.turtle.stamp()
        self.matrix[0][0] = 0

