"""
Opens and displays a station map file and finds the
astronaut's position.

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


if __name__ == "__main__":
    filename = input("Enter filename: ")
    station_map = read_station(filename)
    print(station_map)
    display_station(station_map)
    position = find_astronaut(station_map)
    print(f"Astronaut is at: {position}")