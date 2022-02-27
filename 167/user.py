"""Module to implement a User class."""


class User:
    """A User class.

    (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Construct object with base values."""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self) -> str:
        """Return first and last separated by a whitespace.

        Use title case for both.
        """
        return f"{self.first_name} {self.last_name}".title()

    @property
    def username(self) -> str:
        """Return username.

        A username consists of the first char of
        the user's first_name and the first 7 chars
        of the user's last_name, both lowercased.

        If this is your first property, check out:
        https://pybit.es/property-decorator.html
        """
        return (self.first_name[0] + self.last_name[:7]).lower()

    def __str__(self) -> str:
        """Return printable version of object."""

    def __repr__(self) -> str:
        """
        Return technical version of object.

        Don't hardcode the class name, hint: use a
        special attribute of self.__class__ ...
        """
