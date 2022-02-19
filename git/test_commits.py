from commits import clone_from_remote, git_dir_present, count_commits, first_commit
from pathlib import Path
import pytest
import shutil
from git import Repo

URL = "https://github.com/git/git.git"  # or something more fixed

@pytest.fixture(scope="module")
def local_repo() -> None:
    cwd = Path.cwd()
    local = cwd / "local"
    return clone_from_remote(URL, local)


@pytest.fixture(scope="module")
def list_commits(local_repo) -> None:
    return list(local_repo.iter_commits("master"))


def test_retrieve_new_repo():
    cwd = Path.cwd()
    local = cwd / "local"
    shutil.rmtree(local)
    return clone_from_remote(URL, local)


def test_retrieve_repo(local_repo) -> None:
    assert isinstance(local_repo, Repo)


def test_git_dir_present(local_repo) -> None:
        assert git_dir_present(local_repo)


def test_no_git_dir_in_empty_repo(local_repo) -> None:
    bare_repo_path = Path.cwd() / "bare-repo"
    bare_repo = Repo.init(bare_repo_path, bare=True)
    assert not git_dir_present(bare_repo)


def test_count_commits(local_repo) -> None:
    assert count_commits(local_repo) == 65887


def test_first_commit(local_repo) -> None:
    assert first_commit(local_repo) == "e83c5163316f89bfbde7d9ab23ca2e25604af290"

