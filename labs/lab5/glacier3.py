"""
Displays glacier temperature information.
Replaces any empty entries with average temperature
of neighbouring cells.
Counts and prints the number of frozen cells
including their coordinate pairs.

Author: Luc Bibeau
When: November 4, 2025
"""

def create_grid(filename):
    """
    Creates a two-dimensional array from the given file
    :param filename: filename, str
    :return: 2d array of temperatures, list<list<int>>
    """

    file = open(filename, 'r')
    lines = file.read().splitlines()
    file.close()

    rows = int(lines.pop(0))
    columns = int(lines.pop(0))

    grid = []
    for row in range(rows):

        row_array = []

        for column in range(columns):
            temperature = int(lines.pop(0))
            row_array.append(temperature)

        grid.append(row_array)

    return grid


def display_grid(grid):
    """
    Displays a grid of temperatures
    :param grid: 2d array of temperatures, list<list<int>>
    :return: None
    """
    max_length = 3

    for row in grid:

        row_strings = []

        for entry in row:
            temperature_string = str(entry)
            spaces = max_length - len(temperature_string)
            temperature_string = (" " * spaces) + temperature_string

            row_strings.append(temperature_string)

        print(" ".join(row_strings))


def find_neighbours(grid, row, col):
    """
    Finds and returns the neighbouring cells of (row, col)
    :param grid: temperature grid, list<list<int>>
    :param row: row, int
    :param col: column, int
    :return: list of neighbouring temperatures, list<int>
    """

    neighbours = []

    row_range = range(row - 1, row + 2)
    col_range = range(col - 1, col + 2)

    for row_index in range(len(grid)):
        row_entry = grid[row_index]
        for col_index in range(len(row_entry)):
            if row != row_index or col != col_index:
                if (row_index in row_range) and (col_index in col_range):

                    neighbours.append(grid[row_index][col_index])

    print(f"Neighbours of cell ({row},{col}) are {neighbours}")

    return neighbours


def fill_missing(grid):
    """
    Fills in any zeros with the average of their
    neighbouring cells.
    :param grid: grid of temperatures, list<list<int>>
    :return: None
    """
    for row_index in range(len(grid)):
        row_entry = grid[row_index]

        for column_index in range(len(row_entry)):
            if row_entry[column_index] == 0:
                neighbours = find_neighbours(grid, row_index, column_index)

                total = 0
                for neighbour in neighbours:
                    total += neighbour

                row_entry[column_index] = total // len(neighbours)  # averages the temperature


def count_frozen_zones(grid):
    """
    Counts how many entries have a temperature
    less than or equal to -10
    :param grid: grid of temperatures, list<list<int>>
    :return: count, int
    """
    count = 0
    for row in grid:
        for entry in row:
            if entry <= -10:
                count += 1

    return count


def get_frozen_zones(grid):
    """
    Gets the coordinate pairs for any entries
    with a temperature less than or equal to -10
    :param grid: grid of temperatures, list<list<int>>
    :return: coordinate pairs, list<tuple<int>>
    """
    result = []

    rows = range(len(grid))
    columns = range(len(grid[0]))

    for row_index in rows:
        row_entry = grid[row_index]
        for column_index in columns:
            entry = row_entry[column_index]

            if entry <= -10:
                result.append((row_index, column_index))

    return result


def main():
    filename = input("Filename: ")
    grid = create_grid(filename)

    print("Original Glacier Temperature Grid:")
    display_grid(grid)

    print()
    fill_missing(grid)
    print("\nFilled-in Glacier Temperature Grid:")

    display_grid(grid)

    frozen_count = count_frozen_zones(grid)
    print(f"\nFrozen zone count: {frozen_count}")

    frozen_zones = get_frozen_zones(grid)
    print(f"Frozen zone positions: {frozen_zones}")


if __name__ == "__main__":
    main()