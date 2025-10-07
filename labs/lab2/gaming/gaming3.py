"""
Lists game characters. The user then chooses
a character and must guess the franchise they
are from in 3 attempts. After a failed attempt,
a hint will be revealed.

Author: Luc Bibeau
When: October 3, 2025
"""

file_name = input("Filename: ")

file = open(file_name)
data = file.read()
file.close()

franchises = []
characters = []

for line in data.splitlines():
    char, franchise = line.split(",") # set char to index 0, franchise to index 1
    franchises.append(franchise)
    characters.append(char)

print("Welcome to the Gaming Hall of Fame")

num_of_entries = len(franchises)
for i in range(num_of_entries):
    print(f"{i + 1}. {characters[i]}")

points = 0

keep_playing = True
while keep_playing:
    choice_index = int(input(f"\nPlease enter a number between 1 and {num_of_entries}: ")) - 1
    print(f"The chosen figure is {characters[choice_index]}")

    attempt = 0
    franchise = franchises[choice_index]
    split_franchise = franchise.split() # this variable is used for hints
    correct_guess = False

    # instead of keeping track of points and then adding at the end,
    # we can tentatively give the player 3 points and just remove
    # a point every time an incorrect answer is given
    round_points = 3

    while not (attempt == 3 or correct_guess): # stop when they guess 3 times or correctly
        attempt += 1
        print(f"ATTEMPT {attempt}")
        guess = input("Franchise: ")
        correct_guess = guess == franchise

        print("Correct! Well done, Player" if correct_guess else "Incorrect guess")
        if not correct_guess:
            round_points -= 1

            if attempt == 1:
                print(f"Hint 1: The franchise has {len(split_franchise)} word(s).")
            elif attempt == 2:
                hint = []
                for word in split_franchise:
                    obfuscated = "*" * (len(word) - 1)
                    hint.append(word[0] + obfuscated) # combines first letter & obfuscated text
                print(f"Hint 2: The franchise is {" ".join(hint)}")

    if not correct_guess:
        print(f"Out of guesses! The correct answer was {franchise}")

    points += round_points
    print(f"Points earned: {round_points}")

    keep_playing = input("Play again (y/n?) ").lower() == "y"

print(f"\nTotal points: {points}")
if points < 6:
    print("Press F for better luck.")
elif points < 11:
    print("Checkpoint! Time to save.")
elif points < 16:
    print("Close call, almost a win.")
else:
    print("Golden keyboard! Pro level!")
