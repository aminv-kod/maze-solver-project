import time
import sys
import os

# Enable virtual terminal processing on Windows to support ANSI escape sequences and colors
if os.name == 'nt':
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        h_stdout = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_ulong()
        if kernel32.GetConsoleMode(h_stdout, ctypes.byref(mode)):
            kernel32.SetConsoleMode(h_stdout, mode.value | 0x0004)  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    except Exception:
        pass

# ANSI escape codes for clean terminal colors
C_RESET = "\033[0m"
C_WALL = "\033[90m"        # Dim Gray
C_START = "\033[92;1m"      # Bold Green
C_EXIT = "\033[91;1m"       # Bold Red
C_VISITED = "\033[36m"      # Cyan
C_PATH = "\033[93;1m"       # Bold Yellow

def get_wall_char(grid, r, c):
    """Determine if a wall cell '#' should render as '-' or '|'."""
    cols = len(grid[0])
    # If there is a wall neighbor to the left or right, treat it as a horizontal segment
    left_wall = (c > 0 and grid[r][c-1] == "#")
    right_wall = (c < cols - 1 and grid[r][c+1] == "#")
    if left_wall or right_wall:
        return "-"
    return "|"

def format_cell(grid, r, c):
    """Format a single cell with colors and custom characters."""
    cell = grid[r][c]
    if cell == "#":
        return f"{C_WALL}{get_wall_char(grid, r, c)}{C_RESET}"
    elif cell == ".":
        return " "
    elif cell == "S":
        return f"{C_START}S{C_RESET}"
    elif cell == "E":
        return f"{C_EXIT}E{C_RESET}"
    elif cell == "v":
        return f"{C_VISITED}v{C_RESET}"
    elif cell == "*":
        return f"{C_PATH}*{C_RESET}"
    return cell

def print_maze(grid):
    for r in range(len(grid)):
        row_chars = [format_cell(grid, r, c) for c in range(len(grid[r]))]
        print(" ".join(row_chars))


def animate_search(maze, visited_sequence, algorithm_name="Search"):
    if not visited_sequence:
        return

    maze_copy = [row[:] for row in maze]

    # Hide console cursor for clean animation
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    # Clear terminal screen initially
    os.system("cls" if os.name == "nt" else "clear")

    try:
        sys.stdout.write("\033[H")
        sys.stdout.write(f"{algorithm_name} Searching...\n\n")
        for r in range(len(maze_copy)):
            row_str = " ".join(format_cell(maze_copy, r, c) for c in range(len(maze_copy[r])))
            sys.stdout.write(row_str + "\n")
        sys.stdout.flush()
        time.sleep(0.1)

        for r, c in visited_sequence:
            if maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "v"

                # Repaint in place using cursor home
                sys.stdout.write("\033[H")
                sys.stdout.write(f"{algorithm_name} Searching...\n\n")
                for r_idx in range(len(maze_copy)):
                    row_str = " ".join(format_cell(maze_copy, r_idx, c_idx) for c_idx in range(len(maze_copy[r_idx])))
                    sys.stdout.write(row_str + "\n")
                sys.stdout.flush()

                # Dynamic delay scaling based on sequence length (capped between 50ms and 250ms for visibility)
                delay = max(0.05, min(0.25, 5.0 / len(visited_sequence)))
                time.sleep(delay)
                
    except KeyboardInterrupt:
        pass
    finally:
        # Guarantee restoring the console cursor
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


def visualize_path(maze, path):
    maze_copy = [row[:] for row in maze]
    if path:
        for r, c in path:
            if maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "*"
    return maze_copy