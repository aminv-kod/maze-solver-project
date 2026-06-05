class Maze:

    def __init__(self, grid):
        self.grid = grid

    def find_start(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "S":
                    return (row, col)