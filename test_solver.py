import unittest
from solver import solve_bfs, solve_dfs


class TestSolver(unittest.TestCase):

    def test_simple_path(self):
        maze = [
            ["S", ".", "."]
        ]

        expected = [
            (0, 0),
            (0, 1)
        ]

        self.assertEqual(
            solve_bfs(maze)[0],
            expected
        )

    def test_no_path(self):
        maze = [
            ["S", "#", "#"]
        ]

        self.assertIsNone(
            solve_bfs(maze)[0]
        )

    def test_maze_with_turns(self):
        maze = [
            ["#", "#", "#", "#"],
            ["S", ".", ".", "."],
            ["#", "#", "#", "#"]
        ]

        expected = [
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3)
        ]

        self.assertEqual(
            solve_bfs(maze)[0],
            expected
        )

    def test_dfs_simple_path(self):
        maze = [
            ["S", ".", "."]
        ]

        expected = [
            (0, 0),
            (0, 1)
        ]

        self.assertEqual(
            solve_dfs(maze)[0],
            expected
        )

    def test_dfs_no_path(self):
        maze = [
            ["S", "#", "#"]
        ]

        self.assertIsNone(
            solve_dfs(maze)[0]
        )

    def test_visited_steps_format(self):
        maze = [
            ["S", ".", "."],
            ["#", "#", "E"]
        ]
        path, visited, _ = solve_bfs(maze)
        self.assertIsInstance(visited, list)
        if visited:
            self.assertIsInstance(visited[0], tuple)
            self.assertEqual(len(visited[0]), 2)

    def test_bfs_vs_dfs_path_length(self):
        maze = [
            ["S", ".", ".", "."],
            [".", "#", "#", "."],
            [".", ".", ".", "E"]
        ]
        bfs_path, _, _ = solve_bfs(maze)
        dfs_path, _, _ = solve_dfs(maze)
        self.assertIsNotNone(bfs_path)
        self.assertIsNotNone(dfs_path)
        self.assertTrue(len(bfs_path) <= len(dfs_path))


if __name__ == "__main__":
    unittest.main()