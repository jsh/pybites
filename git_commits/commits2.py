#!/usr/bin/env python3
"""Explore the repo of git itself."""

from pygit2 import Repository, GIT_SORT_TIME

def set_repo(path: str):
    return Repository(path)

def count_commits(repo: Repository) -> int:
    """Count the number of commits in the repo."""
    head = repo[repo.head.target]
    commits = list(repo.walk(head.id, GIT_SORT_TIME))
    return len(commits)

def first_commit(repo: Repository) -> str:
    """Return the SHA1 of the first commit."""
    head = repo[repo.head.target]
    commits = list(repo.walk(head.id, GIT_SORT_TIME))
    return str(commits[-1].id)

def last_commit(repo: Repository) -> str:
    """Return the SHA1 of the last commit."""
    head = repo[repo.head.target]
    return str(head.id)
