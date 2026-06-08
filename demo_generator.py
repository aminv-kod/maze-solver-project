from generator import generate_maze

maze = generate_maze(25, 25)

for row in maze:
    print(" ".join(row))