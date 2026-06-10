# Maze Solver Project

## Overview

Maze Solver is a Python application that finds a path from a starting point (`S`) to the maze exit using two graph-search algorithms:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

The program loads a maze from a text file, visualizes the search process, and displays the final solution path.

---

## Features

* Load mazes from a text file
* Detect the start position automatically
* Find the nearest maze exit
* Solve mazes using BFS or DFS
* Visualize explored nodes during the search
* Display the final solved maze
* Unit tests included

---

## Project Structure

```text
maze-solver-project/
│
├── main.py              # Main application
├── maze.py              # Maze class and helper methods
├── solver.py            # BFS and DFS algorithms
├── loader.py            # Maze file loader
├── renderer.py          # Visualization utilities
├── maze.txt             # Input maze
│
├── test_maze.py         # Maze tests
├── test_solver.py       # Solver tests
├── test_rendere.py      # Renderer tests
│
└── README.md
```

---

## Maze Symbols

| Symbol | Meaning                    |
| ------ | -------------------------- |
| S      | Start position             |
| E      | Exit                       |
| #      | Wall                       |
| .      | Open path                  |
| *      | Final solution path        |
| v      | Visited cell during search |

---

## Example Maze

```text
#######
#S....#
#.###.#
#.....#
#####E#
```

---

## How It Works

### BFS (Breadth-First Search)

BFS explores all neighboring cells level by level.

Advantages:

* Guarantees the shortest path
* Good for finding optimal solutions

### DFS (Depth-First Search)

DFS explores one path as deeply as possible before backtracking.

Advantages:

* Simpler implementation
* Uses less memory in some cases

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aminv-kod/maze-solver-project.git
cd maze-solver-project
```

Make sure Python 3 is installed:

```bash
python --version
```

---

## Running the Program

```bash
python main.py
```

Choose an algorithm:

```text
Choose algorithm:
1. BFS
2. DFS
```

---

## Sample Output

```text
Original maze:
# # # # #
# S . . #
# . # . #
# . . E #
# # # # #

Algorithm: BFS

Path:
[(1,1), (1,2), (1,3), (2,3), (3,3)]

Solved maze:
# # # # #
# S * * #
# . # * #
# . . E #
# # # # #
```

---

## Testing

Run all tests:

```bash
python -m unittest
```

Run a specific test file:

```bash
python -m unittest test_solver.py
```

---

## Concepts Used

* Object-Oriented Programming (OOP)
* Graph Traversal
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Queues and Stacks
* Path Reconstruction
* Python Data Structures

---

## Authors

Shaxboz Aminov
Shokhrukh Orzuyev

GitHub: https://github.com/aminv-kod
GitHub: https://github.com/deucalion-os
