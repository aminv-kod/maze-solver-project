import time
import sys
from generator import generate_maze
from solver import solve_bfs, solve_dfs
from renderer import print_maze, visualize_path, animate_search
from loader import load_maze

# Color codes
C_RESET = "\033[0m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_CYAN = "\033[36m"
C_RED = "\033[91m"
C_MAGENTA = "\033[95m"

# Animation toggle (set to True by default, can be toggled via options if desired)
animation_enabled = True

def draw_bar(percentage, length=20, color_code=C_GREEN):
    filled = int(round((percentage / 100.0) * length))
    filled = max(0, min(length, filled))
    bar = "█" * filled + "░" * (length - filled)
    return f"{color_code}[{bar}] {percentage:.1f}%{C_RESET}"

def get_color_for_efficiency(eff):
    if eff >= 70.0:
        return C_GREEN
    elif eff >= 30.0:
        return C_YELLOW
    else:
        return C_CYAN

def print_performance_table(bfs_stats, dfs_stats):
    bfs_time = f"{bfs_stats['time']:.3f} ms" if bfs_stats['path'] else "N/A"
    dfs_time = f"{dfs_stats['time']:.3f} ms" if dfs_stats['path'] else "N/A"
    
    bfs_len = f"{bfs_stats['path_len']} steps" if bfs_stats['path'] else "No path"
    dfs_len = f"{dfs_stats['path_len']} steps" if dfs_stats['path'] else "No path"
    
    bfs_visited = str(bfs_stats['visited_len'])
    dfs_visited = str(dfs_stats['visited_len'])
    
    bfs_peak = str(bfs_stats['peak'])
    dfs_peak = str(dfs_stats['peak'])
    
    bfs_expl = f"{bfs_stats['explored_pct']:.1f}% ({bfs_stats['visited_len']}/{bfs_stats['total_walkable']})" if bfs_stats['path'] else "N/A"
    dfs_expl = f"{dfs_stats['explored_pct']:.1f}% ({dfs_stats['visited_len']}/{dfs_stats['total_walkable']})" if dfs_stats['path'] else "N/A"
    
    bfs_eff = bfs_stats['efficiency']
    dfs_eff = dfs_stats['efficiency']
    
    bfs_bar = draw_bar(bfs_eff, 15, get_color_for_efficiency(bfs_eff)) if bfs_stats['path'] else "N/A"
    dfs_bar = draw_bar(dfs_eff, 15, get_color_for_efficiency(dfs_eff)) if dfs_stats['path'] else "N/A"
    
    # Text-based layout for high readability
    print("\n" + "=" * 65)
    print("                 SOLVER PERFORMANCE COMPARISON")
    print("=" * 65)
    print(f"{'Metric':<25} | {'BFS (Shortest Path)':<17} | {'DFS (Backtracking)':<17}")
    print("-" * 65)
    print(f"{'Time Taken':<25} | {bfs_time:<17} | {dfs_time:<17}")
    print(f"{'Path Length (Steps)':<25} | {bfs_len:<17} | {dfs_len:<17}")
    print(f"{'Nodes Visited':<25} | {bfs_visited:<17} | {dfs_visited:<17}")
    print(f"{'Memory Peak (Frontier)':<25} | {bfs_peak:<17} | {dfs_peak:<17}")
    print(f"{'Search Space Explored':<25} | {bfs_expl:<17} | {dfs_expl:<17}")
    print(f"{'Search Focus Efficiency':<25} | {bfs_bar:<17} | {dfs_bar:<17}")
    print("=" * 65)


def run_solver(maze, algorithm):
    start_time = time.perf_counter()
    if algorithm == "BFS":
        path, visited_steps, max_frontier = solve_bfs(maze)
    else:
        path, visited_steps, max_frontier = solve_dfs(maze)
    elapsed_ms = (time.perf_counter() - start_time) * 1000.0
    
    if animation_enabled and path:
        animate_search(maze, visited_steps, algorithm)
        
    solved_maze = visualize_path(maze, path)
    
    print(f"\n{C_GREEN}=== {algorithm} Solved Maze ==={C_RESET}")
    print_maze(solved_maze)
    
    if path:
        print(f"\n{C_GREEN}✓ Path found in {elapsed_ms:.3f} ms!{C_RESET}")
        print(f"Path Length: {len(path)} steps")
    else:
        print(f"\n{C_RED}✗ No path found from start to exit!{C_RESET}")
        
    total_walkable = sum(cell != "#" for row in maze for cell in row)
    visited_len = len(visited_steps)
    path_len = len(path) if path else 0
    efficiency = (path_len / visited_len * 100.0) if visited_len > 0 else 0.0
    explored_pct = (visited_len / total_walkable * 100.0) if total_walkable > 0 else 0.0
    
    eff_color = get_color_for_efficiency(efficiency)
    
    print("\nSolve Metrics:")
    print(f"- Time Taken:              {elapsed_ms:.3f} ms")
    print(f"- Path Length:             {path_len} steps")
    print(f"- Nodes Visited:           {visited_len} cells")
    print(f"- Memory Peak (Frontier):  {max_frontier} items")
    print(f"- Search Space Explored:   {explored_pct:.1f}% ({visited_len}/{total_walkable} cells)")
    if path:
        print(f"- Search Focus Efficiency: {draw_bar(efficiency, 20, eff_color)}")
    print("=" * 40)


def run_comparison(maze):
    # BFS Solve
    start_time = time.perf_counter()
    bfs_path, bfs_visited, bfs_frontier = solve_bfs(maze)
    bfs_time_ms = (time.perf_counter() - start_time) * 1000.0
    
    # DFS Solve
    start_time = time.perf_counter()
    dfs_path, dfs_visited, dfs_frontier = solve_dfs(maze)
    dfs_time_ms = (time.perf_counter() - start_time) * 1000.0
    
    total_walkable = sum(cell != "#" for row in maze for cell in row)
    
    bfs_len = len(bfs_path) if bfs_path else 0
    dfs_len = len(dfs_path) if dfs_path else 0
    bfs_visited_len = len(bfs_visited)
    dfs_visited_len = len(dfs_visited)
    
    bfs_eff = (bfs_len / bfs_visited_len * 100.0) if bfs_visited_len > 0 else 0.0
    dfs_eff = (dfs_len / dfs_visited_len * 100.0) if dfs_visited_len > 0 else 0.0
    
    bfs_expl = (bfs_visited_len / total_walkable * 100.0) if total_walkable > 0 else 0.0
    dfs_expl = (dfs_visited_len / total_walkable * 100.0) if total_walkable > 0 else 0.0
    
    bfs_stats = {
        'path': bfs_path, 'time': bfs_time_ms, 'path_len': bfs_len,
        'visited_len': bfs_visited_len, 'peak': bfs_frontier,
        'efficiency': bfs_eff, 'explored_pct': bfs_expl, 'total_walkable': total_walkable
    }
    
    dfs_stats = {
        'path': dfs_path, 'time': dfs_time_ms, 'path_len': dfs_len,
        'visited_len': dfs_visited_len, 'peak': dfs_frontier,
        'efficiency': dfs_eff, 'explored_pct': dfs_expl, 'total_walkable': total_walkable
    }
    
    print(f"\n{C_MAGENTA}=== BFS Solved Maze ==={C_RESET}")
    print_maze(visualize_path(maze, bfs_path))
    
    print(f"\n{C_MAGENTA}=== DFS Solved Maze ==={C_RESET}")
    print_maze(visualize_path(maze, dfs_path))
    
    print_performance_table(bfs_stats, dfs_stats)
    
    if bfs_path and dfs_path:
        print("\nComparison Insights:")
        if bfs_len < dfs_len:
            print(f"- Path: BFS path is shorter by {dfs_len - bfs_len} steps.")
        elif dfs_len < bfs_len:
            print(f"- Path: DFS path is shorter by {bfs_len - dfs_len} steps.")
        else:
            print("- Path: Both found paths of equal length.")
            
        if bfs_visited_len < dfs_visited_len:
            print(f"- Exploration: BFS visited {dfs_visited_len - bfs_visited_len} fewer nodes than DFS.")
        elif dfs_visited_len < bfs_visited_len:
            print(f"- Exploration: DFS visited {bfs_visited_len - dfs_visited_len} fewer nodes than BFS.")
        else:
            print("- Exploration: Both visited the same number of nodes.")
            
        if bfs_time_ms < dfs_time_ms:
            print(f"- Speed: BFS solved the maze faster by {dfs_time_ms - bfs_time_ms:.3f} ms.")
        elif dfs_time_ms < bfs_time_ms:
            print(f"- Speed: DFS solved the maze faster by {bfs_time_ms - dfs_time_ms:.3f} ms.")
        else:
            print("- Speed: Both solved the maze in equal time.")


def main():
    while True:
        print(f"\n{C_MAGENTA}=== MAZE SOLVER SYSTEM ==={C_RESET}")
        print("1. Load maze from text file")
        print("2. Generate a new random maze")
        print("3. Exit")
        print("--------------------------")
        
        source_choice = input("Select option (1-3): ").strip()
        
        if source_choice == "1":
            filename = input("Enter maze file path (default: maze.txt): ").strip()
            if not filename:
                filename = "maze.txt"
            try:
                maze = load_maze(filename)
                print(f"\n{C_GREEN}✓ Maze loaded successfully.{C_RESET}")
            except Exception as e:
                print(f"\n{C_RED}✗ Error loading maze: {e}{C_RESET}")
                continue
                
        elif source_choice == "2":
            try:
                width = int(input("Enter maze width (e.g. 25): "))
                height = int(input("Enter maze height (e.g. 15): "))
                maze = generate_maze(width, height)
                print(f"\n{C_GREEN}✓ Random maze generated successfully.{C_RESET}")
            except ValueError:
                print(f"\n{C_RED}✗ Invalid size input. Must be integers.{C_RESET}")
                continue
            except Exception as e:
                print(f"\n{C_RED}✗ Error generating maze: {e}{C_RESET}")
                continue
                
        elif source_choice == "3":
            print("\nExiting Maze Solver. Goodbye!")
            break
        else:
            print(f"\n{C_RED}✗ Invalid choice. Try again.{C_RESET}")
            continue

        # Print the original loaded/generated maze
        print(f"\n{C_MAGENTA}Original Maze Layout:{C_RESET}")
        print_maze(maze)
        
        # Immediate prompt for method selection
        print(f"\n{C_MAGENTA}=== Select Solving Method ==={C_RESET}")
        print("1. BFS (Breadth-First Search)")
        print("2. DFS (Depth-First Search)")
        print("3. Compare BFS & DFS side-by-side")
        print("4. Cancel (Return to Main Menu)")
        print("-----------------------------")
        
        method_choice = input("Select option (1-4): ").strip()
        
        if method_choice == "1":
            run_solver(maze, "BFS")
        elif method_choice == "2":
            run_solver(maze, "DFS")
        elif method_choice == "3":
            run_comparison(maze)
        elif method_choice == "4":
            print("\nAction cancelled. Returning to main menu.")
        else:
            print(f"\n{C_RED}✗ Invalid method selection. Returning to main menu.{C_RESET}")

if __name__ == "__main__":
    main()