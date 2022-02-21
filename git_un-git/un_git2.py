#!/usr/bin/env python3

from pathlib import Path
import shutil

import pygit2

REPO="."
GIT_DIR=".git"
SCRATCH="scratch2"


def un_git(repo="."):
    shutil.rmtree(repo + "/.git", ignore_errors=True)

def create_repo(repo="."):
    return pygit2.init_repository(repo)

if __name__ == "__main__":
    shutil.rmtree(SCRATCH, ignore_errors=True)
    create_repo(SCRATCH)
