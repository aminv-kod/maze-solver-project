import random
from collections import deque

def generate_maze(width, height):
    print("Generating new maze...")
    print("First random:", random.randint(1, 1000000))

    maze = []

    for row in range(height):
        maze.append(["#"] * width)

    maze[1][1] = "."

    def carve(row, col):

        directions = [
            (-2, 0),
            (2, 0),
            (0, -2),
            (0, 2)
        ]

        random.shuffle(directions)

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if (
                1 <= new_row < height - 1 and
                1 <= new_col < width - 1 and
                maze[new_row][new_col] == "#"
            ):

                maze[row + dr // 2][col + dc // 2] = "."
                maze[new_row][new_col] = "."

                carve(new_row, new_col)

    carve(1, 1)
    border_candidates = []
    for row in range(1, height - 1):

        if maze[row][1] == ".":
            border_candidates.append((row, 0))

        if maze[row][width - 2] == ".":
            border_candidates.append((row, width - 1))
    for col in range(1, width - 1):

        if maze[1][col] == ".":
            border_candidates.append((0, col))

        if maze[height - 2][col] == ".":
            border_candidates.append((height - 1, col))

    exit_position = random.choice(border_candidates)

    border_candidates.remove(exit_position)
    exit_row, exit_col = exit_position

    inside_row = exit_row
    inside_col = exit_col

    if exit_row == 0:
        inside_row = 1
    elif exit_row == height - 1:
        inside_row = height - 2

    if exit_col == 0:
        inside_col = 1
    elif exit_col == width - 1:
        inside_col = width - 2

    queue = deque([(inside_row, inside_col)])

    distances = {
        (inside_row, inside_col): 0
    }
    
    while queue:

        row, col = queue.popleft()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < height and
                0 <= new_col < width and
                maze[new_row][new_col] == "." and
                (new_row, new_col) not in distances
            ):

                distances[(new_row, new_col)] = (
                    distances[(row, col)] + 1
                )

                queue.append(
                    (new_row, new_col)
                )
    farthest_distance = -1
    start_position = None

    for candidate in border_candidates:

        row, col = candidate

        inside_row = row
        inside_col = col

        if row == 0:
            inside_row = 1  
        elif row == height - 1:
            inside_row = height - 2

        if col == 0:
            inside_col = 1
        elif col == width - 1:
            inside_col = width - 2

        if (inside_row, inside_col) in distances:

            distance = distances[(inside_row, inside_col)]

            if distance > farthest_distance:

                farthest_distance = distance
                start_position = candidate

    start_row, start_col = start_position
    exit_row, exit_col = exit_position

    maze[start_row][start_col] = "S"
    maze[exit_row][exit_col] = "E"
    
    return maze