def print_maze(maze):
    for row in maze:
        print(" ".join(row))


def visualize_path(maze, path):

    maze_copy = [row[:] for row in maze]

    for r, c in path:

        if maze_copy[r][c] not in ("S", "E"):
            maze_copy[r][c] = "*"

    return maze_copy