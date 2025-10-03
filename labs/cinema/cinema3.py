"""
Asks the user for their name, favourite spice,
and favourite genre to create a code for them.

Displays all available movies in their favourite genre.

Buys the most expensive ticket from said movies that
they can afford.

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

# formula used to calculate user's balance
balance = (len(spice) + len(genre)) // 2 + (len(name) % 2)

print(f"\nYour movie balance: ${balance}\n")

movies = []

if genre == "Action":
    movies.append(("John Wick", 7))
    movies.append(("Top Gun", 5))
elif genre == "Comedy":
    movies.append(("Dictator", 6))
    movies.append(("Night School", 5))
elif genre == "Scifi":
    movies.append(("Inception", 8))
    movies.append(("Avatar", 5))
elif genre == "History":
    movies.append(("Oppenheimer", 10))
    movies.append(("The Imitation Game", 5))
else:
    print(f"There are no available movies for {genre} genre")
    exit()  # exiting avoids an extra if

ticket = None

print("Available Movies:")
for movie in movies:
    movie_title = movie[0]
    price = movie[1]
    print(f"{movie_title} - ${price}")

    # the movie tuples are already sorted by price
    # so the first one we can buy is the
    # most expensive.
    if ticket is None and balance >= price:
        balance -= price
        ticket = movie_title

print("")

if ticket is None:
    print("You cannot afford a movie ticket :(")
else:
    print(f"Bought a ticket for {ticket}!")

print(f"\nRemaining balance: ${balance}")

