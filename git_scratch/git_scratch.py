#!/usr/bin/env python3
"""Create a scratch repo with initial empty commit."""

import argparse
import sys
from pathlib import Path

from git import Repo

TMP = Path("/tmp")
SCRATCH = "scratch"
SCRATCH_PATH = TMP / SCRATCH


def getargs() -> argparse.Namespace:
    """Get and parse arguments."""
    parser = argparse.ArgumentParser(
        description="Create a scratch repo.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        allow_abbrev=True,
    )
    parser.add_argument(
        "name", nargs="?", type=Path, default=SCRATCH, help="name of repo to create"
    )
    parser.add_argument(
        "--remote", action="store_true", help="Create a remote repo with local clones"
    )
    parser.add_argument("--debug", action="store_true", help="Debugging info.")
    arg_tuple = parser.parse_args()
    arg_tuple.path = Path(arg_tuple.name)
    if arg_tuple.debug:
        print(arg_tuple)
    return arg_tuple


def commit_file(repo: Repo, file: str, comment: str) -> None:
    """Commit a named file."""
    if not repo.working_tree_dir:
        sys.exit("No working tree")
    file_path = Path(repo.working_tree_dir) / file
    file_path.touch(exist_ok=True)
    repo.index.add(file)
    repo.index.commit(comment)


def create_scratch(path: Path = SCRATCH_PATH) -> None:
    """Create a scratch repo, with initial commit."""
    repo = Repo.init(path)
    commit_file(repo, ".gitkeep", "initial commit")


if __name__ == "__main__":
    args = getargs()
    create_scratch(args.path)
