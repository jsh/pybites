"""Bite 313. Alternative constructors."""

import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:
    """Class to hold a domain name."""

    def __init__(self, name: str):
        """Construct Domain object."""
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        pat = re.compile(r".*\.[a-z]{2,3}$")
        match = pat.match(name)
        if not match:
            raise DomainException()

    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

    def __str__(self) -> str:
        """Return string representing the domain."""
        return self.name

    @classmethod
    def parse_url(cls, url: str) -> "Domain":
        """Parse a URL with http(s):// ."""
        pat = re.compile(r"https?://([^/]+).*$")
        match = pat.match(url)
        if match:
            return cls(match[1])
        return cls("")

    @classmethod
    def parse_email(cls, email: str) -> "Domain":
        """Parse a URL with name@url."""
        pat = re.compile(r"[^@]+@(\S+)$")
        match = pat.match(email)
        if match:
            return cls(match[1])
        return cls("")
