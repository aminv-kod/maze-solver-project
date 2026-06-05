import unittest
from solver import solve_bfs, solve_dfs


class TestSolver(unittest.TestCase):

    def test_simple_path(self):
        maze = [
            ["S", ".", "E"]
        ]

        expected = [
            (0, 0),
            (0, 1),
            (0, 2)
        ]

        self.assertEqual(
            solve_bfs(maze),
            expected
        )

    def test_no_path(self):
        maze = [
            ["S", "#", "E"]
        ]

        self.assertIsNone(
            solve_bfs(maze)
        )

    def test_maze_with_turns(self):
        maze = [
            ["S", ".", "#"],
            ["#", ".", "#"],
            ["#", ".", "E"]
        ]

        expected = [
            (0, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (2, 2)
        ]

        self.assertEqual(
            solve_bfs(maze),
            expected
        )

    def test_dfs_simple_path(self):
        maze = [
            ["S", ".", "E"]
        ]

        expected = [
            (0, 0),
            (0, 1),
            (0, 2)
        ]

        self.assertEqual(
            solve_dfs(maze),
            expected
        )

    def test_dfs_no_path(self):
        maze = [
            ["S", "#", "E"]
        ]

        self.assertIsNone(
            solve_dfs(maze)
        )


if __name__ == "__main__":
    unittest.main()