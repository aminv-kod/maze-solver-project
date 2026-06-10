import random
from collections import deque

def generate_maze(width, height):
    # Validate and adjust dimensions (must be odd and >= 5 for proper grid carving)
    adjusted = False
    orig_w, orig_h = width, height

    if width < 5:
        width = 5
        adjusted = True
    elif width % 2 == 0:
        width += 1
        adjusted = True

    if height < 5:
        height = 5
        adjusted = True
    elif height % 2 == 0:
        height += 1
        adjusted = True

    if adjusted:
        print(f"[Generator] Adjusted size from {orig_w}x{orig_h} to {width}x{height} to preserve grid alignment.")

    maze = []
    for row in range(height):
        maze.append(["#"] * width)

    # Initialize start point for carving
    maze[1][1] = "."

    # Iterative randomized DFS carving
    stack = [(1, 1)]
    while stack:
        row, col = stack[-1]

        directions = [
            (-2, 0),
            (2, 0),
            (0, -2),
            (0, 2)
        ]
        random.shuffle(directions)

        carved = False
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                1 <= new_row < height - 1 and
                1 <= new_col < width - 1 and
                maze[new_row][new_col] == "#"
            ):
                # Carve path and wall in between
                maze[row + dr // 2][col + dc // 2] = "."
                maze[new_row][new_col] = "."
                stack.append((new_row, new_col))
                carved = True
                break

        if not carved:
            stack.pop()

    # Post-processing: remove some random walls to create loops/cycles (braid maze)
    # This increases solving complexity and makes BFS vs DFS comparison more interesting
    for row in range(2, height - 2):
        for col in range(2, width - 2):
            if maze[row][col] == "#":
                horizontal_connect = (maze[row][col-1] == "." and maze[row][col+1] == ".")
                vertical_connect = (maze[row-1][col] == "." and maze[row+1][col] == ".")
                if (horizontal_connect or vertical_connect) and random.random() < 0.08:
                    maze[row][col] = "."

    # Locate candidates on the border for S and E
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

    if not border_candidates:
        # Fallback if no border candidates found (should not happen for valid sizes)
        maze[1][0] = "S"
        maze[height - 2][width - 1] = "E"
        return maze

    exit_position = random.choice(border_candidates)
    border_candidates.remove(exit_position)
    exit_row, exit_col = exit_position

    # Place temporary open path at exit to perform BFS distance check
    inside_row, inside_col = exit_row, exit_col
    if exit_row == 0:
        inside_row = 1
    elif exit_row == height - 1:
        inside_row = height - 2

    if exit_col == 0:
        inside_col = 1
    elif exit_col == width - 1:
        inside_col = width - 2

    # Run BFS from exit to find the farthest border candidate for the start position
    queue = deque([(inside_row, inside_col)])
    distances = {(inside_row, inside_col): 0}

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
                distances[(new_row, new_col)] = distances[(row, col)] + 1
                queue.append((new_row, new_col))

    farthest_distance = -1
    start_position = None

    for candidate in border_candidates:
        row, col = candidate
        inside_row, inside_col = row, col

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

    # If start candidate was not reachable via BFS, pick random remaining candidate
    if start_position is None:
        start_position = random.choice(border_candidates) if border_candidates else (1, 0)

    start_row, start_col = start_position
    maze[start_row][start_col] = "S"
    maze[exit_row][exit_col] = "E"

    return maze