"""
Allows the user to interact with the rental catalog
via a text based menu.

Author: Luc Bibeau
When: December 2, 2025
"""

from rental1 import Listing
from rental2 import RentalCatalog


def main():
    catalog = RentalCatalog()
    repeat = True
    applied_discount = False

    while repeat:
        print("""
Menu:
1. Show catalog summary
2. Add listings from file
3. Compare listings
4. Reduce prices above average
5. Quit
""")
        choice = input("Choose an option (1-5): ")

        match choice:
            case "1":
                catalog.print_summary()

            case "2":
                filename = input("Enter filename: ")
                catalog.add_listings_from_file(filename)
                print(f"Listings added from {filename}.")

            case "3":
                listing_1 = catalog.get_listing(input("Enter the id of listing you want to compare to: "))
                listing_2 = catalog.get_listing(input("Enter the id of listing you want to compare with: "))

                if listing_1 is None or listing_2 is None:
                    print("One or both listings could not be found.")
                else:
                    better = listing_1.is_better_deal(listing_2)
                    if better:
                        print(f"{listing_1.get_listing_id()} is a better deal than {listing_2.get_listing_id()}.")
                    else:
                        print(f"{listing_1.get_listing_id()} is not a better deal than {listing_2.get_listing_id()}.")

            case "4":
                if not applied_discount:
                    discounted = catalog.reduce_prices_above_average()
                    print(f"Discounted: {", ".join(discounted)}")
                    applied_discount = True
                else:
                    print("Already applied discount!")

            case "5":
                repeat = False
                print("Goodbye")

            case _:  # default
                print("Not a valid option!")


if __name__ == "__main__":
    main()
