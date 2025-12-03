"""
Compares two listings.

Author: Luc Bibeau
When: December 2, 2025
"""


class Listing:
    """
    An object that represents a real estate listing
    """

    def __init__(self, listing_id, has_gym, price):
        """
        Creates and returns a Listing object
        :param listing_id: ID of the listing, str
        :param has_gym: Whether the listing has a gym, bool
        :param price: Price of the listing, float
        """
        self.listing_id = listing_id
        self.has_gym = has_gym
        self.price = price

    def get_listing_id(self):
        """
        Gets the listing id
        :return: str
        """
        return self.listing_id

    def get_price(self):
        """
        Gets the price of the listing
        :return: float
        """
        return self.price

    def reduce_price(self, discount_pct):
        """
        Reduces the price of the listing by X%
        :param discount_pct: percentage to decrease, float
        :return: None
        """
        self.price *= 1 - (discount_pct / 100.)

    def is_better_deal(self, other_listing):
        """
        Compares self to another listing to see if it's a better deal
        :param other_listing: Listing to compare, Listing
        :return: bool
        """
        other_price = other_listing.get_price()

        if self.price > other_price:
            return False

        if self.has_gym and not other_listing.has_gym:
            return True

        if self.has_gym == other_listing.has_gym:
            return self.price != other_price

        return False

    def __str__(self):
        return f"Listing ID: {self.get_listing_id()}, Has Gym: {self.has_gym}, Price: ${round(self.get_price(), 2)}"


def main():
    """Demonstrate the Listing class functionality with examples."""
    # Create a Listing object
    listing1 = Listing("L001", True, 450.00)
    listing2 = Listing("L002", False, 600.00)

    # Print original listing
    print("Original Listing:")
    print(listing1)

    # Test getter methods
    print("\nTesting getter methods...")
    print(f"ID: {listing1.get_listing_id()}")
    print(f"Price: ${listing1.get_price()}")

    # Apply a discount
    print("\nApplying 20% discount...")
    listing1.reduce_price(20)

    # Print after discount
    print("\nListing After Discount:")
    print(listing1)

    # Compare two listings
    print("\nComparing two listings:")
    print(listing1)
    print(listing2)
    if listing1.is_better_deal(listing2):
        print(f"{listing1.get_listing_id()} is a better deal than {listing2.get_listing_id()}.")
    else:
        print(f"{listing1.get_listing_id()} is not a better deal than {listing2.get_listing_id()}.")


if __name__ == "__main__":
    main()
