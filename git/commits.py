#!/usr/bin/env python3
"""Explore the repo of git itself."""

from pathlib import Path
import git
from git import Repo
import sys

def clone_from_remote(url: str, local: Path) -> Repo:
    """Get a local copy of a remote repo."""
    if local.is_dir():
        return Repo(local)
    return Repo.clone_from(url, local)


def git_dir_present(repo: Repo) -> bool:
    """Verify that repo.git_dir == path/to/working/repo/.git."""
    if repo.bare:
        return False
    return Path(repo.git_dir) == Path(repo.working_tree_dir) / ".git"


def count_commits(repo: Repo) -> int:
    """Count the number of commits in the repo."""
    commits = list(repo.iter_commits("master"))
    return len(commits)


def first_commit(repo: Repo) -> str:
    """Return the SHA1 of the first commit."""
    commits = list(repo.iter_commits("master"))
    return str(commits[-1])
