from solver import solve_bfs
from renderer import print_maze, visualize_path
from loader import load_maze

maze = load_maze("maze.txt")

print("Original maze:")
print_maze(maze)

path = solve_bfs(maze)

print("\nPath:")
print(path)

solved = visualize_path(maze, path)

print("\nSolved maze:")
print_maze(solved)