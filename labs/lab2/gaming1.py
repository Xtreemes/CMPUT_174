"""
Lists game 

Author: Luc Bibeau
When: October 1, 2025
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
    print(f"{i + 1}. {characters[i]} - {franchises[i]}")

choice_index = int(input(f"Please enter a number between 1 and {num_of_entries}: ")) - 1
print(f"The chosen figure is {characters[choice_index]}")
