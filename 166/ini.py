"""Bite 166. Complete a tox ini file parser class."""

import configparser
from typing import List


class ToxIniParser:
    """Parser for Tox ini file."""

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config."""
        config = configparser.ConfigParser()
        config.read(ini_file)
        self.config = config

    @property
    def number_of_sections(self) -> int:
        """Return the number of sections in the ini file.

        New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self) -> List[str]:
        """Return a list of environments.

        (= "envlist" attribute of [tox] section)
        """
        # envs = self.config["tox"]["envlist"].replace("\n", "").split(",")
        envlist = self.config["tox"]["envlist"].replace("\n", ",")
        envs = envlist.split(",")
        envs = [env.strip() for env in envs if env]
        return envs

    @property
    def base_python_versions(self) -> List[str]:
        """Return a list of all basepython across the ini file."""
        basepythons = set()
        for section in self.config.sections():
            if "basepython" in self.config[section]:
                basepythons.add(self.config[section]["basepython"])
        return list(basepythons)
