import turtle

SIZE = 400

EAST=0
NORTH=1
WEST=2
SOUTH=3

class Maze:
    """ This class creates a random maze """

    def __init__(self):
        self.reset()

    def reset(self):
        self.s = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.s.setup(width=SIZE, height=SIZE)
        self.turtle.goto(-(SIZE / 2 - 20), SIZE / 2 - 20)
        self.matrix = [[1 for i in range(int(SIZE / 20))] for i in range(int(SIZE / 20))]
        self.s.bgcolor('blue')
        self.turtle.shape('square')
        self.turtle.color('white')
        self.turtle.stamp()
        self.matrix[0][0] = 0

    def dig(self, d):
        return self.turtle.pos()

    def getMatrixValueAt(self,pos):
        # pos = tuple (-180,180)
        # take (-180,180) and convert to [0][0] v = self.matrix[0][0]
        """ returns value of matrix at position pos """
        pass

    def setMatrixValueAt(self,value):
        # get turtle position (-160,180) store the value into self.matrix[1][0]
        """ sets the value of the matrix at turtle position to value """
        pass