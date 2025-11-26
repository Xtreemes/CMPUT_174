"""
Opens a den file of dragons and prompts the user
to either exit or display the roster.

Author: Luc Bibeau
When: November 26, 2025
"""

DISPLAY_SPACES = 17

def read_dragons(filename):
    """
    Opens a den file and creates a roster of dragons.
    :param filename: name of den file, str
    :return: roster, dict
    """
    roster = {}

    file = open(filename)
    data = file.read().splitlines()
    file.close()

    for line in data:
        dragon_info = line.split(",")

        name = dragon_info[0]
        dragon_type = dragon_info[1]
        stamina = dragon_info[2]
        training = dragon_info[3]

        roster[name] = [dragon_type, stamina, training]

    return roster


def display_dragons(roster):
    """
    Displays a roster of dragons
    :param roster: dict
    :return: None
    """

    for name in roster:
        info = roster[name]
        spaces = " " * (DISPLAY_SPACES - len(name))

        print(f"{name}{spaces}TYPE: {info[0]} - STA: {info[1]} - LVL: {info[2]}")


def menu():
    """
    Displays a menu to the user and gets their choice.
    :return:
    """
    print("""
MENU
1. Display dragons
2. Exit""")

    choice = input("Enter choice: ")
    try:
        choice = int(choice)
        if 1 <= choice <= 2:
            return choice
    except ValueError:
        pass

    print("Invalid input!")
    return menu()



def main():
    filename = input("Enter a filename: ")
    roster = read_dragons(filename)

    repeat = True
    while repeat:
        choice = menu()

        if choice == 1:
            display_dragons(roster)
        elif choice == 2:
            print("Goodbye dragons!")
            repeat = False


if __name__ == "__main__":
    main()