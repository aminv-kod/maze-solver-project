from collections import deque

def solve_bfs(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = None
    end = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    queue = deque([(start, [start])])
    visited = {start}

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                maze[nr][nc] != "#" and
                (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append(
                    ((nr, nc), path + [(nr, nc)])
                )

    return None
def solve_dfs(maze):

    rows = len(maze)
    cols = len(maze[0])

    start = None
    end = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    stack = [(start, [start])]
    visited = {start}

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while stack:

        (r, c), path = stack.pop()

        if (r, c) == end:
            return path

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                maze[nr][nc] != "#" and
                (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                stack.append(
                    ((nr, nc), path + [(nr, nc)])
                )

    return None