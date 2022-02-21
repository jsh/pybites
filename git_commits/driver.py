#!/usr/bin/env python3

from commits2 import set_repo, first_commit, last_commit, count_commits

if __name__ == "__main__":
    repo = set_repo("scratch")
    first = first_commit(repo)
    last = last_commit(repo)
    ncommits = count_commits(repo)
    print(f"first commit is {first}, last commit is {last}, number of commits is {ncommits}")

