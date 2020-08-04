import unittest
import turtle
from Maze import Maze

SIZE = 400


class MazeTests(unittest.TestCase):
    def setUp(self):
        self.m = Maze()

    def testScreen(self):
        self.assertTrue(type(self.m.s) == turtle._Screen, "No Screen!")

    def testTurtle(self):
        self.assertTrue(type(self.m.turtle) == turtle.Turtle)

    def testBackground(self):
        self.assertTrue(self.m.s.bgcolor() == 'blue')

    def testSize(self):
        self.assertTrue(self.m.s.window_height() == SIZE, f"window height is {self.m.s.window_height()}")
        self.assertTrue(self.m.s.window_width() == SIZE)

    def testMatrixSize(self):
        self.assertTrue(len(self.m.matrix) == SIZE / 20)

    def testReset(self):
        self.m.reset()
        self.assertTrue(self.m.turtle.pos() == (-(SIZE / 2 - 10), SIZE / 2 - 10))


if __name__ == "__main__":
    unittest.main()
