class GridLocation:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return f"GridLocation({self.row}, {self.col})"


class Grid:
    def __init__(self, rows: int, cols: int, goal: GridLocation = None):
        """
        Initialize the grid with None for walls and False for impassable by default.
        """
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.goal = goal  # Define the goal of the maze

    def in_bounds(self, location: GridLocation) -> bool:
        """
        Check if the location is within the bounds of the grid.
        """
        return 0 <= location.row < len(self.grid) and 0 <= location.col < len(self.grid[0])

    def is_passable(self, location: GridLocation) -> bool:
        """
        Check if the cell is passable: it should not be None and not visited.
        True means unvisited and passable.
        """
        return self.grid[location.row][location.col] is not None and self.grid[location.row][location.col]

    def visit(self, location: GridLocation):
        """
        Mark this cell as visited (turn True to False).
        """
        if self.grid[location.row][location.col] is not None:
            self.grid[location.row][location.col] = False  # Mark the cell as visited

    def is_finished(self, location: GridLocation) -> bool:
        """
        Check if the current location is the goal.
        """
        return location == self.goal  # Compare current location to the goal

    def get_visited(self) -> set:
        """
        Return the set of locations that have been visited
        (where cells are marked as False).
        """
        visited = set()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] is False:  # If cell is False, it's visited
                    visited.add(GridLocation(row, col))
        return visited

    def set_wall(self, location: GridLocation):
        """
        Set a wall (None) at the given location.
        """
        self.grid[location.row][location.col] = None

    def set_passable(self, location: GridLocation):
        """
        Set the cell as passable (True).
        """
        self.grid[location.row][location.col] = True

    def __getitem__(self, location: GridLocation) -> bool:
        """
        Allow access to the grid using grid[location].
        """
        return self.grid[location.row][location.col]

    def __setitem__(self, location: GridLocation, value: bool):
        """
        Allow setting grid values using grid[location] = value.
        """
        self.grid[location.row][location.col] = value

    def __repr__(self) -> str:
        """
        Visual representation of the grid.
        # for walls, . for unvisited, and o for visited cells.
        """
        return '\n'.join(
            [''.join(['#' if cell is None else '.' if cell else 'o' for cell in row]) for row in self.grid]
        )

