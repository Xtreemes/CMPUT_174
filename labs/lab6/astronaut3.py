"""
Opens and displays a station map file and finds the
astronaut's position, escape pod's position, and all
valid moves from the astronaut.

Author: Luc Bibeau
When: November 18, 2025
"""

ADJACENT_DIRECTIONS = ((-1, 0), (1, 0), (0,-1), (0, 1))
POSSIBLE_MOVES = ["up", "down", "left", "right"]
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


def locate_char(station_map, char):
    """
    Locates a character in the station map
    :param station_map: station map, list<list<str>>
    :param char: character, str
    :return: position, tuple<int>
    """
    row_index = 0
    for row in station_map:
        col_index = 0

        for entry in row:
            if entry == char:
                return row_index, col_index
            col_index += 1

        row_index += 1


def find_astronaut(station_map):
    """
    Finds the astronaut's position in the station map
    :param station_map: station map, list<list<str>>
    :return: position, tuple<int>
    """
    return locate_char(station_map, "A")


def locate_escape_pod(station_map):
    """
    Finds the escape pod's position in the station map
    :param station_map: station map, list<list<str>>
    :return: position, tuple<int>
    """
    return locate_char(station_map, "E")


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

    max_row = len(station_map)
    max_col = len(station_map[0])

    for direction in ADJACENT_DIRECTIONS:
        current_row = row + direction[0]
        current_col = col + direction[1]

        if 0 <= current_row < max_row and 0 <= current_col < max_col:
            char = station_map[current_row][current_col]

            if char == "E" or char == "*":
                valid_moves.append((current_row, current_col))

    return valid_moves


def get_move(valid_moves, pos):
    """
    Prompts the user to enter a move and verifies that it is valid.
    :param valid_moves: list<tuple<int>>
    :param pos: position, tuple<int>
    :return: move, tuple<int>
    """
    move = ""
    while move not in POSSIBLE_MOVES:
        move = input("Enter move: ").lower().strip()

    row = pos[0]
    col = pos[1]

    match move:
        case "up": row -= 1
        case "down": row += 1
        case "left": col -= 1
        case "right": col += 1

    new_pos = (row, col)

    if new_pos in valid_moves:
        return new_pos

    return get_move(valid_moves, pos)  # reprompt user


def move_astronaut(station_map, pos, converted_move):
    """
    Moves the astronaut
    :param station_map: station map, list<list<str>>
    :param pos: current position, tuple<int>
    :param converted_move: new position, tuple<int>
    :return: None
    """

    station_map[pos[0]][pos[1]] = "*"
    station_map[converted_move[0]][converted_move[1]] = "A"
    # list is mutable so no return needed


if __name__ == "__main__":
    filename = input("Enter filename: ")
    station_map = read_station(filename)
    display_station(station_map)
    pos = find_astronaut(station_map)
    escape_location = locate_escape_pod(station_map)

    if escape_location is None:
        print("Critical: station-map shows zero escape pods. Good luck!")
    else:
        while pos != escape_location:
            valid_moves = get_valid_moves(station_map, pos)
            converted_move = get_move(valid_moves, pos)
            move_astronaut(station_map, pos, converted_move)
            display_station(station_map)
            pos = find_astronaut(station_map)

        print("You have reached the escape pod!")