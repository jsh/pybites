"""Bite 95. Subclass the dict built-in."""

MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Dict that announces duplicates.

    Override dict to print a message every time a new person is added that has
    the same birthday (day+month) as somebody already in the dict
    """

    def __init__(self, *args, **kwargs) -> None:
        """Create BirthdayDict object."""
        dict.__init__(self, *args, **kwargs)

    def __setitem__(self, name, birthday) -> None:
        """Add an entry to the dict."""
        month = birthday.month
        day = birthday.day
        for date in self.values():
            if date.month == month and date.day == day:
                print(MSG.format(name))
        dict.__setitem__(self, name, birthday)
