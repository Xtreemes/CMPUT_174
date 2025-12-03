"""
Creates a catalog of listings from a file. Prints a summary
of the listings and discounts any overpriced listings.

Author: Luc Bibeau
When: December 2, 2025
"""

from rental1 import Listing


class RentalCatalog:
    """
    An object that contains an array of Listings
    """

    def __init__(self):
        """
        Creates and returns the RentalCatalog object
        """
        self.rental_units = []

    def add_listings_from_file(self, filename):
        """
        Reads listings from a file and stores them in self
        :param filename: name of file, str
        :return: None
        """
        file = open(filename)
        lines = file.read().splitlines()
        file.close()

        for line in lines:
            listing_id, has_gym, price = line.split(", ")
            self.rental_units.append(Listing(listing_id, has_gym == "True", float(price)))

    def get_listing(self, listing_id):
        """
        Uses linear search to find a listing by ID
        :param listing_id: str
        :return: Listing or None
        """
        for listing in self.rental_units:
            if listing.listing_id == listing_id:
                return listing

    def count_listings(self):
        """
        Returns the number of listings
        :return: int
        """
        return len(self.rental_units)

    def average_price(self):
        """
        Returns the average price of the listings
        :return: float
        """
        total_listings = self.count_listings()

        if total_listings == 0:
            return 0.  # prevent division by zero

        total = 0.

        for listing in self.rental_units:
            total += listing.get_price()

        return round(total / total_listings, 2)

    def reduce_prices_above_average(self):
        """
        Discounts any listings above average by 5%
        :return: reduced listings, tuple
        """
        average_price = self.average_price()
        reduced = []

        for listing in self.rental_units:
            if listing.get_price() > average_price:
                listing.reduce_price(5)
                reduced.append(listing.get_listing_id())

        return tuple(reduced)

    def print_summary(self):
        """
        Prints a summary of the listings in this catalog object
        :return: None
        """
        print(f"Total Listings: {self.count_listings()}")
        print(f"Average Price: ${self.average_price()}")

        print("\nAll Listings:")
        for listing in self.rental_units:
            print(listing)


def main():
    """Demonstrate the RentalCatalog functionality with file loading and price reduction."""
    filename = input("Enter filename: ").strip()
    catalog = RentalCatalog()

    # Load listings from file
    catalog.add_listings_from_file(filename)

    # Print initial summary
    print("\nInitial Summary")
    catalog.print_summary()

    # Print Average Price
    print(f"\nAvg Price: ${catalog.average_price():,.2f}")

    # Reduce prices above average
    print("\nReducing prices above average...")
    print(f"Discounted: {', '.join(catalog.reduce_prices_above_average())}")

    # Print updated summary
    print("\nUpdated Summary")
    catalog.print_summary()


if __name__ == "__main__":
    main()
