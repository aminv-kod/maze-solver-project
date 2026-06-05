# Helper to print grid with headers
def print_grid_with_headers(grid):
    # Print column headers (units digit)
    print("   " + "".join([str(i % 10) for i in range(len(grid[0]))]))
    for idx, row in enumerate(grid):
        print(f"{idx:2d} " + "".join(row))

grid_str = """
#####################
#.........#.....#...#
#######.###.#######.#
S.....#...#.#...#.###
#.###.###.#.#.#.#.#.#
#.#.#...#.#...#.#.#.#
#.#.#####.#####.###.#
#.#.#...#.#...#.....#
#.#.#.#.#.#.#.#####.#
#.#...#.#...#.#...#.#
#.#####.#####.#.#.#.#
#.....#.....#...#...#
#####.#####.#########
#...#.....#.....#...#
#.#.#####.#####.#.#.#
#.#...#...#...#...#.#
#.#.###.###.###.###.#
#.#.#...#...#...#....
#.#.#####.#######.###
#.#.....#.......#...#
#####################
""".strip().split("\n")

grid = [list(row) for row in grid_str]
print_grid_with_headers(grid)
