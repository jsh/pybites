#!/usr/bin/env python3

from pathlib import Path
import shutil

from git import Repo

REPO="."
GIT_DIR=".git"
SCRATCH="scratch"


def un_git(repo="."):
    shutil.rmtree(repo + "/.git", ignore_errors=True)

def create_repo(repo="."):
    return Repo.init(repo)

if __name__ == "__main__":
    shutil.rmtree(SCRATCH, ignore_errors=True)
    create_repo(SCRATCH)
