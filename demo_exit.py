from maze import Maze
from generator import generate_maze

maze = generate_maze(25, 25)

maze_obj = Maze(maze)

print("START:", maze_obj.find_start())
print("EXIT:", maze_obj.find_exit())