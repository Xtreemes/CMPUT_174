"""
Opens and displays a station map file and finds the
astronaut's position, escape pod's position, and all
valid moves from the astronaut.

Author: Luc Bibeau
When: November 18, 2025
"""

EMOJIS = (
    ("A", "👨"),
    ("#", "🚧"),
    ("*", "🟢"),
    ("E", "🛸")
)


def read_station(filename):
    """
    Opens a station map file and formats it
    as a 2D array
    :param filename: name of file, str
    :return: station map, list<list<str>>
    """
    file = open(filename)
    data = file.read().splitlines()
    file.close()

    station_map = []

    for line in data:
        line_array = []

        for character in line:
            line_array.append(character)

        station_map.append(line_array)

    return station_map


def get_emoji(char):
    """
    Converts a station map character
    into an emoji.
    :param char: character, str
    :return: emoji, str
    """

    for pair in EMOJIS:
        if char == pair[0]:
            return pair[1]


def display_station(station_map):
    """
    Displays the station map as a neatly
    aligned grid.
    :param station_map: station map, list<list<str>>
    :return: None
    """
    for row in station_map:

        line = []

        for entry in row:
            line.append(get_emoji(entry))

        print(" ".join(line))


def find_astronaut(station_map):
    """
    Finds the astronaut's position in the station map
    :param station_map: station map, list<list<str>>
    :return: position, tuple<int>
    """
    row_index = 0
    for row in station_map:
        col_index = 0

        for entry in row:
            if entry == "A":
                return row_index, col_index
            col_index += 1

        row_index += 1


def locate_escape_pod(station_map):
    """
    Finds the escape pod's position in the station map
    :param station_map: station map, list<list<str>>
    :return: position, tuple<int>
    """
    row_index = 0
    for row in station_map:
        col_index = 0

        for entry in row:
            if entry == "E":
                return row_index, col_index
            col_index += 1

        row_index += 1


def get_valid_moves(station_map, pos):
    """
    Returns a list of all valid moves
    that can be made from a position.
    :param station_map: station map, list<list<str>>
    :param pos: position, tuple<int>
    :return:
    """
    valid_moves = []

    row = pos[0]
    col = pos[1]

    max_row = len(station_map) - 1
    max_col = len(station_map[0]) - 1

    # use min & max functions to ensure moves are inbound
    row_left_bound = max(0, row - 1)
    row_right_bound = min(max_row, row + 1)

    col_left_bound = max(0, col - 1)
    col_right_bound = min(max_col, col + 1)


    for row_iter in range(row_left_bound, row_right_bound + 1):  # add 1 because range is exclusive
        if row_iter != row:
            pos = (row_iter, col)

            if is_valid(station_map, pos):
                valid_moves.append(pos)

    for col_iter in range(col_left_bound, col_right_bound + 1):  # add 1 because range is exclusive
        if col_iter != col:
            pos = (row, col_iter)

            if is_valid(station_map, pos):
                valid_moves.append(pos)

    return valid_moves


def is_valid(station_map, pos):
    """
    Returns if a position is a valid spot
    to move into.
    :param station_map: station map, list<list<str>>
    :param pos: position, tuple<int>
    :return:
    """
    char = station_map[pos[0]][pos[1]]

    return char == "E" or char == "*"




if __name__ == "__main__":
    filename = input("Enter filename: ")
    station_map = read_station(filename)

    display_station(station_map)
    pos = find_astronaut(station_map)
    print(f"Astronaut is at: {pos}")

    escape_location = locate_escape_pod(station_map)
    valid_moves = get_valid_moves(station_map, pos)

    print(f"Escape pod is at: {escape_location}")
    print(f"Valid moves: {valid_moves}")