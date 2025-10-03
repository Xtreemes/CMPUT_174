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

keep_playing = True
while keep_playing:
    choice_index = int(input(f"\nPlease enter a number between 1 and {num_of_entries}: ")) - 1
    print(f"The chosen figure is {characters[choice_index]}")

    attempt = 0
    franchise = franchises[choice_index]
    correct_guess = False
    while not (attempt == 3 or correct_guess): # stop when they guess 3 times or correctly
        attempt += 1
        print(f"ATTEMPT {attempt}")
        guess = input("Franchise: ")
        correct_guess = guess == franchise
        # ternary operator saves space in the code
        print("Correct! Well done, Player" if correct_guess else "Incorrect guess")

    if not correct_guess:
        print(f"Out of guesses! The correct answer was {franchise}")

    keep_playing = input("Play again (y/n?) ").lower() == "y"

print("\nThanks for playing!")
