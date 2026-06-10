from collections import deque
from maze import Maze

def solve_bfs(maze):
    maze_obj = Maze(maze)
    start = maze_obj.find_start()
    end = maze_obj.find_exit()

    if start is None or end is None:
        return None, []

    queue = deque([start])
    visited = {start}
    visited_steps = []
    parent = {start: None}
    max_frontier = 0

    while queue:
        max_frontier = max(max_frontier, len(queue))
        curr = queue.popleft()

        if curr == end:
            # Reconstruct path using parent backtracking
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, visited_steps, max_frontier

        for nr, nc in maze_obj.get_neighbors(curr[0], curr[1]):
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                visited_steps.append((nr, nc))
                parent[(nr, nc)] = curr
                queue.append((nr, nc))

    return None, visited_steps, max_frontier


def solve_dfs(maze):
    maze_obj = Maze(maze)
    start = maze_obj.find_start()
    end = maze_obj.find_exit()

    if start is None or end is None:
        return None, [], 0

    # Stack contains tuples of (current_node, parent_node)
    stack = [(start, None)]
    visited = set()
    visited_steps = []
    parent = {}
    max_frontier = 0

    while stack:
        max_frontier = max(max_frontier, len(stack))
        curr, p = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)
        visited_steps.append(curr)
        parent[curr] = p

        if curr == end:
            # Reconstruct path using parent backtracking
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, visited_steps, max_frontier

        for nr, nc in maze_obj.get_neighbors(curr[0], curr[1]):
            if (nr, nc) not in visited:
                stack.append(((nr, nc), curr))

    return None, visited_steps, max_frontier