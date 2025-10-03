"""
Asks the user for their name, favourite spice,
and favourite genre to create a code for them.

Author: Luc Bibeau
When: September 24, 2025
"""

name = input("Enter your name: ")
spice = input("Enter your favourite spice: ").title()

welcome = f"Welcome to {spice} Cinema"
border = "*" * len(welcome)

print(f"\n{border}\n{welcome}\n{border}")
print(f"Hello {name}!")

genre = input("Enter your favourite genre: ").capitalize()
code = spice[:2] + name[-1] + genre[:2]
code = code.upper()
print(f"Here's your special code for your next visit '{code}'")