"""Bite 166. Complete a tox ini file parser class."""

import configparser


class ToxIniParser:
    """Parser for Tox ini file."""

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config."""

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.

        New to properties? -> https://pybit.es/property-decorator.html
        """

    @property
    def environments(self):
        """Return a list of environments.

        (= "envlist" attribute of [tox] section)
        """

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file."""
