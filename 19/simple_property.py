"""Bite 19. Write a property."""

from datetime import datetime

NOW = datetime.now()


class Promo:
    """Represent a promotion."""

    def __init__(self, name: str, expires: datetime):
        """Create a Promo object."""
        self._name = name
        self._expires = expires

    @property
    def expired(self) -> bool:
        """Determine whether the Promo has expired."""
        return self._expires < NOW
