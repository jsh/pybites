"""Bite 199. Multiple inheritance (__mro__)."""
# see __mro__ output in Bite description


class Person:
    """Represent a person."""

    def __repr__(self) -> str:
        """Represent the object."""
        identity = "I am a person"
        return identity


class Father(Person):
    """Represent a father."""

    def __repr__(self) -> str:
        """Represent the object."""
        return super().__repr__() + " and cool daddy"


class Mother(Person):
    """Represent a mother."""

    def __repr__(self) -> str:
        """Represent the object."""
        return super().__repr__() + " and awesome mom"


class Child(Father, Mother):
    """Represent a child."""

    def __repr__(self) -> str:
        """Represent the object."""
        return "I am the coolest kid"
