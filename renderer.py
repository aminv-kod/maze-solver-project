import time
import os

def animate_search(maze, visited):

    for step in visited:

        maze_copy = [row[:] for row in maze]

        for r, c in step:

            if maze_copy[r][c] != ("S"):
                maze_copy[r][c] = "v"

        os.system("cls")

        print("BFS Searching...\n")

        print_maze(maze_copy)

        time.sleep(0.05)

def print_maze(maze):
    for row in maze:
        print(" ".join(row))


def visualize_path(maze, path):

    maze_copy = [row[:] for row in maze]

    for r, c in path:

        if maze_copy[r][c] not in ("S", "E"):
            maze_copy[r][c] = "*"

    return maze_copy