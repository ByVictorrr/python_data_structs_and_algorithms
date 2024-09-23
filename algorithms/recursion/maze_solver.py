from typing import List, Set
from maze.grid import Grid, GridLocation
from maze.visualize import visualize_maze


def generate_valid_moves(maze: Grid, cur: GridLocation) -> Set[GridLocation]:
    moves = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E

    # Debug: print current location
    print(f"Current location: {cur}")

    for dr, dc in directions:
        new_row, new_col = cur.row + dr, cur.col + dc
        new_location = GridLocation(new_row, new_col)

        # Debug: print the location being checked
        print(f"Checking location: {new_location}")

        if maze.in_bounds(new_location):
            # Debug: print in-bounds status
            print(f"Location {new_location} is in bounds")

            if maze.is_passable(new_location):
                # Debug: print passable status
                print(f"Location {new_location} is passable")

                # Add valid move to the set
                moves.add(new_location)
            else:
                print(f"Location {new_location} is not passable")
        else:
            print(f"Location {new_location} is out of bounds")

    # Debug: print the valid moves found
    print(f"Valid moves from {cur}: {moves}")

    return moves


def solve_maze(maze: Grid, start: GridLocation) -> List[GridLocation]:
    """Go through a maze using dfs and try to find the path to exit."""
    if solve_maze_helper(maze, _paths := [], start):
        return _paths
    return []


def solve_maze_helper(maze: Grid, path: list[GridLocation], curr: GridLocation) -> bool:
    # Add the current location to the path (this is part of the solution path we're exploring)
    path.append(curr)

    # Mark the current location as visited so it won't be revisited later
    maze.visit(curr)

    # Check if the current location is the goal
    if maze.is_finished(curr):
        # If it's the goal, the maze is solved, so return True
        return True

    # Get all valid moves (neighboring cells that are in bounds, passable, and not visited)
    for move in generate_valid_moves(maze, curr):
        # Explore the move by recursively calling the helper with the new location
        if solve_maze_helper(maze, path, curr=move):
            return True

    # If no valid moves lead to the goal, remove the current location from the path (backtrack)
    path.remove(curr)

    # If all recursive paths fail, return False to indicate this path didn't lead to the goal
    return False


if __name__ == "__main__":
    rows, cols = 5, 5
    goal = GridLocation(4, 4)
    grid = Grid(rows, cols, goal=goal)
    start = GridLocation(0, 0)

    # Set walls and passable paths
    grid.set_passable(start)  # Start
    grid.set_passable(GridLocation(0, 1))
    grid.set_passable(GridLocation(0, 2))
    grid.set_passable(GridLocation(0, 3))

    # Remove the walls at (0, 4) and (1, 4) to open the path
    grid.set_passable(GridLocation(0, 4))  # Remove wall at (0, 4)
    grid.set_passable(GridLocation(1, 4))  # Remove wall at (1, 4)

    grid.set_passable(GridLocation(2, 4))  # Path
    grid.set_passable(GridLocation(3, 4))  # Path
    grid.set_passable(goal)  # Goal

    # Initialize the remaining walls and paths as needed
    # Example: Set walls in other locations explicitly, if needed.

    paths = solve_maze(grid, start)
    visualize_maze(grid, paths)
    print(f"Paths: {paths}")
    print("Maze Setup:")
    print(grid)
