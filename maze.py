class Maze:

    def __init__(self, grid):
        self.grid = grid

    def find_start(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "S":
                    return (row, col)

    def find_end(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "E":
                    return (row, col)
                
    def find_exit(self):

        rows = len(self.grid)
        cols = len(self.grid[0])

        for row in range(rows):
            for col in range(cols):

                is_border = (
                    row == 0 or
                    row == rows - 1 or
                    col == 0 or
                    col == cols - 1
                )

                if (
                    is_border and
                    self.grid[row][col] != "#" and
                    self.grid[row][col] != "S"
                ):
                    return (row, col)

        return None

    def is_wall(self, row, col):
        return self.grid[row][col] == "#"

    def get_neighbors(self, row, col):
        neighbors = []

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < len(self.grid)
                and 0 <= new_col < len(self.grid[0])
                and not self.is_wall(new_row, new_col)
            ):
                neighbors.append((new_row, new_col))

        return neighbors