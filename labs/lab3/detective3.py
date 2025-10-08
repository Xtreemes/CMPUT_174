"""
Allows the user to open and read information
about a case file, view all possible suspects,
and find any matching suspects.

Author: Luc Bibeau
When: October 7, 2025
"""

CASE_HEADERS = ("Case Number", "Incident Type", "Lead Officer", "Suspect Description")


def read_file(case_filename):
    """
    Opens a case file and returns a list of each line
    :param case_filename: name of file, str
    :return: list of each line, list
    """
    file = open(case_filename)
    data = file.read().splitlines()
    file.close()
    return data


def get_info(case_list):
    """
    Prompts the user to choose a piece of information
    from the given case file data
    :param case_list: case file data, list
    :return: formatted information, str
    """

    for index, header in enumerate(CASE_HEADERS):
        print(f"{index + 1}. {header}")

    option = -1
    while not 0 <= option < 4:
        option_string = input("Enter the sno. of the detail: ")
        if option_string.isdecimal():
            option = int(option_string) - 1  # option is the index, not the displayed num (3 is index 2)

    return f"{CASE_HEADERS[option]}: {case_list[option]}"


def get_suspects(case_filename):
    """
    Gets all possible suspects from a case file
    :param case_filename: name of case file, str
    :return: unified list of suspects, list
    """

    # turns "case1.txt" -> ["case1","txt"] -> "case1" -> "1"
    # imma be so real i just didnt wanna write it all out
    case_number = case_filename.split(".")[0][4:]

    suspect_info = []

    for suspect_id in range(1, 4):
        suspect_filename = f"{case_number}suspect{suspect_id}.txt"
        suspect_file = read_file(suspect_filename)
        suspect_info.extend(suspect_file)

    return suspect_info


def display_suspects(unified_list):
    """
    Displays possible suspects to the user
    :param unified_list: unified list of suspects, list
    :return: None
    """
    for suspect_num in range(len(unified_list) // 2):
        print(f"\n# Suspect {suspect_num + 1}")

        suspect_index = suspect_num * 2
        print(f"{unified_list[suspect_index]}\n{unified_list[suspect_index + 1]}")


def match_suspects(case_list, unified_list):
    """
    Searches through the unified list to find
    a matching suspect in case list
    :param case_list: case info, list
    :param unified_list: possible suspects, list
    :return: result, str
    """
    suspect_desc = case_list[3]

    for index in range(0, len(unified_list) * 2, 2):
        possible_suspect_desc = unified_list[index + 1]

        if possible_suspect_desc == suspect_desc:
            return f"-- Suspect named {unified_list[index]} is a match! --"

    return "-- No match found in suspects! --"


def main():
    print("""******************************
<< Welcome to Sherlock Desk >>
******************************""")

    repeat = True
    while repeat:
        case_filename = input("Enter casefile name: ")
        case_list = read_file(case_filename)
        info = get_info(case_list)
        print(f"\nHere is the detail you requested about the case:\n# {info}")

        if input("\nSee possible suspects?: ").lower() == "y":
            suspects = get_suspects(case_filename)
            display_suspects(suspects)

            if input("\nCheck for match?: ").lower() == "y":
                print(match_suspects(case_list, suspects))

        repeat = input("\nInvestigate more?: ").lower() == "y"

    print("<< Session Terminated >>")


if __name__ == "__main__":
    main()
