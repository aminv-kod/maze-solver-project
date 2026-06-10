import os

def load_maze(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Maze file '{filename}' could not be found.")

    maze = []
    with open(filename, "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                maze.append(list(stripped))

    if not maze:
        raise ValueError("Loaded maze is empty.")

    # Validate rectangular shape
    width = len(maze[0])
    for idx, row in enumerate(maze):
        if len(row) != width:
            raise ValueError(f"Inconsistent maze row length at row {idx}. All rows must be of length {width}.")

    # Validate characters and symbols
    flattened = [cell for row in maze for cell in row]
    
    # Check start and exit positions
    if flattened.count("S") != 1:
        raise ValueError("Maze must contain exactly one start position ('S').")

    # Exit detection: check for explicit exit 'E' or open border cell
    has_exit = False
    if "E" in flattened:
        has_exit = True
    else:
        # Check borders for an opening '.'
        rows = len(maze)
        cols = len(maze[0])
        for r in range(rows):
            for c in range(cols):
                is_border = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
                if is_border and maze[r][c] == ".":
                    has_exit = True
                    break
            if has_exit:
                break
                
    if not has_exit:
        raise ValueError("Maze must contain at least one exit (either 'E' or an open border cell '.').")

    return maze