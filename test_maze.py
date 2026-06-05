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

    def test_wall_detection(self):
        grid = [
            ["S", "#"],
            [".", "E"]
        ]

        maze = Maze(grid)

        self.assertTrue(
            maze.is_wall(0, 1)
        )

    def test_get_neighbors(self):
        grid = [
            ["S", "."],
            [".", "E"]
        ]

        maze = Maze(grid)

        self.assertCountEqual(
            maze.get_neighbors(0, 0),
            [(0, 1), (1, 0)]
        )
    
    def test_find_exit(self):
        grid = [
            ["#", "#", "#", "#"],
            ["S", ".", ".", "."],
            ["#", "#", "#", "#"]
        ]

        maze = Maze(grid)

        self.assertEqual(
            maze.find_exit(),
            (1, 3)
        )

if __name__ == "__main__":
    unittest.main()