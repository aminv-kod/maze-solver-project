from solver import solve_bfs, solve_dfs
from renderer import print_maze, visualize_path, animate_search
from loader import load_maze

maze = load_maze("maze.txt")

print("Choose algorithm:")
print("1. BFS")
print("2. DFS")

choice = input("Enter choice: ")

print("Original maze:")
print_maze(maze)

if choice == "1":
    algorithm = "BFS"
    path, visited_steps = solve_bfs(maze)

elif choice == "2":
    algorithm = "DFS"
    path, visited_steps = solve_dfs(maze)

else:
    print("Invalid choice")
    exit()

print(f"\nAlgorithm: {algorithm}")

print("\nPath:")
print(path)


animate_search(
    maze,
    visited_steps
)

solved = visualize_path(maze, path)

print("\nSolved maze:")
print_maze(solved)