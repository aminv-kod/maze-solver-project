def load_maze(filename):
    maze = []

    with open(filename, "r") as file:
        for line in file:
            maze.append(list(line.strip()))

    return maze