import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
from .grid import Grid, GridLocation


def visualize_maze(maze: Grid, path: list[GridLocation]):
    # Convert the maze into a numeric array: 0 for walls, 1 for passable cells, and 2 for visited cells
    maze_array = np.array([[0 if maze[GridLocation(r, c)] is None else
                            2 if maze[GridLocation(r, c)] is False else
                            1 for c in range(len(maze.grid[0]))] for r in range(len(maze.grid))])

    # Create the plot
    fig, ax = plt.subplots()
    ax.imshow(maze_array, cmap='gray_r')  # 'gray_r' for inverted grayscale (black for passable, white for walls)

    # Extract row and column positions for the path
    path_rows = [loc.row for loc in path]
    path_cols = [loc.col for loc in path]

    # Plot the path
    ax.plot(path_cols, path_rows, 'r-o')

    # Mark the start and end points
    ax.text(path[0].col, path[0].row, 'Start', color='blue', fontsize=12, ha='center', va='center')
    ax.text(path[-1].col, path[-1].row, 'End', color='green', fontsize=12, ha='center', va='center')

    # Add red rectangles for walls
    for r in range(len(maze.grid)):
        for c in range(len(maze.grid[0])):
            if maze[GridLocation(r, c)] is None:  # If it's a wall, add a red block
                rect = patches.Rectangle((c - 0.5, r - 0.5), 1, 1, linewidth=1, edgecolor='red', facecolor='red')
                ax.add_patch(rect)

    # Show the plot
    plt.show()