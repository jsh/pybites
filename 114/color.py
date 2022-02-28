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

    color_dict = COLOR_NAMES.copy()

    def __init__(self, color: str):
        """Create object."""
        self._color = color
        key = self._color.upper()
        self.rgb = self.color_dict[key] if key in self.color_dict else None

    @staticmethod
    def hex2rgb(hex_str: str) -> Tuple[int, int, int]:
        """Class method that converts a hex value into an rgb one."""
        first = int(hex_str[1:3], 16)
        second = int(hex_str[3:5], 16)
        third = int(hex_str[5:7], 16)
        return (first, second, third)

    @staticmethod
    def rgb2hex(rgb: Tuple[int, int, int]) -> str:
        """Class method that converts an rgb value into a hex one."""
        if not isinstance(rgb, tuple) or len(rgb) != 3:
            raise ValueError
        hex_str = "#"
        for rgb_val in rgb:
            if 0 <= rgb_val <= 255:
                hex_str += f"{rgb_val:02x}"
            else:
                raise ValueError(f"expected 0 <= {rgb_val} <= 255")
        return hex_str

    def __repr__(self) -> str:
        """Return the repl of the object."""
        return f"{self.__class__.__name__}('{self._color}')"

    def __str__(self) -> str:
        """Return the string value of the color object."""
        if self.rgb:
            return str(self.rgb)
        return "Unknown"
