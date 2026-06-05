import unittest
from maze import Maze


class TestMaze(unittest.TestCase):

    def test_create_maze(self):
        grid = [
            ["S", "."],
            [".", "E"]
        ]

        maze = Maze(grid)

        self.assertEqual(
            maze.grid,
            grid
        )


if __name__ == "__main__":
    unittest.main()