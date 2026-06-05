from collections import deque
from maze import Maze

def solve_bfs(maze):
    rows = len(maze)
    cols = len(maze[0])

    maze_obj = Maze(maze)

    start = maze_obj.find_start()
    end = maze_obj.find_exit()

    queue = deque([(start, [start])])
    visited = {start}
    visited_steps = []

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path, visited_steps

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

                visited_steps.append(
                    visited.copy()
                )
                queue.append(
                    ((nr, nc), path + [(nr, nc)])
                )

    return None, visited_steps
def solve_dfs(maze):

    rows = len(maze)
    cols = len(maze[0])

    maze_obj = Maze(maze)

    start = maze_obj.find_start()
    end = maze_obj.find_exit()

    stack = [(start, [start])]
    visited = {start}
    visited_steps = []

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while stack:

        (r, c), path = stack.pop()

        if (r, c) == end:
            return path, visited_steps

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
                visited_steps.append(
                    visited.copy()
                )
                stack.append(
                    ((nr, nc), path + [(nr, nc)])
                )

    return None, visited_steps