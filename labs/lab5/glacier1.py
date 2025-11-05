"""

Author: Luc Bibeau
When: November 4, 2025
"""

def create_grid(filename):

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
    max_length = 3

    for row in grid:

        row_strings = []

        for entry in row:
            temperature_string = str(entry)
            spaces = max_length - len(temperature_string)
            temperature_string = (" " * spaces) + temperature_string

            row_strings.append(temperature_string)

        print(" ".join(row_strings))


def main():
    filename = input("Filename: ")
    grid = create_grid(filename)

    print("Original Glacier Temperature Grid:")
    display_grid(grid)


if __name__ == "__main__":
    main()