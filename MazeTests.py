import unittest
import turtle
from Maze import Maze

SIZE = 400

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


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
        self.assertTrue(self.m.turtle.pos() == (-(SIZE / 2 - 20), SIZE / 2 - 20))

    def testSettingMatrixValues(self):
        self.m.reset()
        value = self.m.getMatrixValueAt(self.m.turtle.position)
        self.assertTrue(0 == value)
        value = 1
        self.m.setMatrixValueAt(m.turtle.position, value)
        self.assertEqual(self.m.matrix[0][0], 1)


if __name__ == "__main__":
    unittest.main()
