"""Bite 114. Implement a Color class with staticmethod."""

import os
import sys
import urllib.request
from typing import Tuple

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Take the string of a color name and return its RGB value.
    """

    def __init__(self, color: str):
        """Create object."""
        self._color = color

    @staticmethod
    def hex2rgb(hex: int) -> Tuple[int, int, int]:
        """Class method that converts a hex value into an rgb one."""
        return (0, 0, 0)

    @staticmethod
    def rgb2hex(rgb: Tuple[int, int, int]) -> str:
        """Class method that converts an rgb value into a hex one."""
        return "#000000"

    def __repr__(self) -> str:
        """Return the repl of the object."""
        return f'{self.__class__.__name__}("{self._color}")'

    def __str__(self) -> str:
        """Return the string value of the color object."""
        return self._color
