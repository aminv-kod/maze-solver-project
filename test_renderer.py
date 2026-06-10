import unittest
from renderer import visualize_path


class TestRenderer(unittest.TestCase):

    def test_visualize_path(self):

        maze = [
            ["S", ".", "."],
            ["#", "#", "."],
            [".", ".", "E"]
        ]

        path = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2)
        ]

        result = visualize_path(maze, path)

        expected = [
            ["S", "*", "*"],
            ["#", "#", "*"],
            [".", ".", "E"]
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()