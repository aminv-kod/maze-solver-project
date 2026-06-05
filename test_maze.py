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

    def test_find_start(self):
        grid = [
            ["S", "."],
            [".", "E"]
        ]

        maze = Maze(grid)

        self.assertEqual(
            maze.find_start(),
            (0, 0)
        )
    def test_find_end(self):
        grid = [
            ["S", "."],
            [".", "E"]
        ]

        maze = Maze(grid)

        self.assertEqual(
            maze.find_end(),
            (1, 1)
        )


if __name__ == "__main__":
    unittest.main()