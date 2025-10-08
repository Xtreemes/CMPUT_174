"""
Allows the user to open and read information
about a case file.

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


def main():
    print("""******************************
<< Welcome to Sherlock Desk >>
******************************""")

    repeat = True
    while repeat:
        case_filename = input("Enter case file name: ")
        info = get_info(read_file(case_filename))
        print(f"\nHere is the detail you requested about the case:\n# {info}")

        repeat = input("\nInvestigate more?: ").lower() == "y"

    print("<< Session Terminated >>")


if __name__ == "__main__":
    main()
