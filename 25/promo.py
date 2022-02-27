"""Bite 25. No promo twice, keep state in a class."""

import random

BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
BITES_DONE = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    """There are no more Bites available to pick from."""


class Promo:
    """Track which bites are done."""

    def __init__(self):
        """Create a Promo object."""
        # updated Bite to make local copies (avoid globals!)
        self.all_bites = BITES.copy()
        self.bites_done = BITES_DONE.copy()

    def _pick_random_bite(self) -> int:
        """Pick a random Bite that is not done yet.

        If all
        Bites are done, raise a NoBitesAvailable exception
        """
        remaining_bites = self.all_bites.keys() - self.bites_done
        if not remaining_bites:
            raise NoBitesAvailable
        return random.choice(list(remaining_bites))

    def new_bite(self) -> int:
        """Get  a random Bite using _pick_random_bite.

        Add it to self.bites_done, then return it
        """
        random_bite = self._pick_random_bite()
        self.bites_done.add(random_bite)
        return random_bite
