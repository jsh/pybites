#!/usr/bin/env python3

from pathlib import Path
from git import Repo
import argparse

TMP = Path("/tmp")
SCRATCH = "scratch"
SCRATCH_PATH = TMP / SCRATCH

def getargs():
    parser = argparse.ArgumentParser(description="Create a scratch repo.")
    parser.add_argument("reponame", default="scratch", help="name of repo to create")
    parser.add_argument("-r", "--remote", action="store_true", help="Create a remote repo with local clones")
    return parser.parse_args()



def create_scratch(path: Path = SCRATCH_PATH) -> None:
    repo = Repo.init(path)


def create_bare_scratch(path: Path=None) -> None:
    if not path:
        path = TMP / (SCRATCH + ".git")
    repo = Repo.init(path, bare=True)




if __name__ == "__main__":
    args = getargs()
    create_scratch(args.reponame)
    print(args)
