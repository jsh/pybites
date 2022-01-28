"""Bite 240. Write tests for an Account class."""

import pytest

from account import Account

# write your pytest functions below, they need to start with test_


def test_init() -> None:
    """Create account with correct values."""
    acct = Account("jsh", 69)
    assert acct.owner == "jsh"
    assert acct.amount == 69
    assert acct.balance == 69

    acct = Account("jsh")
    assert acct.owner == "jsh"
    assert acct.amount == 0
    assert acct.balance == 0


def test_repr() -> None:
    """repr() is as it should be."""
    acct = Account("jsh", 69)
    assert repr(acct) == "Account('jsh', 69)"


def test_str() -> None:
    """Stringify behaves correctly."""
    acct = Account("jsh", 69)
    assert str(acct) == "Account of jsh with starting amount: 69"


def test_balance() -> None:
    """Balance is correct."""
    assert Account("jsh", 69).balance == 69


def test_add_transaction() -> None:
    """Transactions work."""
    acct = Account("jsh", 69)
    acct.add_transaction(-1)
    assert acct.balance == 68


def test_bad_transaction() -> None:
    """Bad transactions return correct exception, with correct message."""
    acct = Account("jsh", 69)
    with pytest.raises(ValueError) as exc:
        acct.add_transaction("-1")
    assert "please use int for amount" in str(exc.value)


def test_len() -> None:
    """Correct length reported."""
    acct = Account("jsh", 69)
    acct.add_transaction(-1)
    acct.add_transaction(96)
    assert len(acct) == 2


def test_getitem() -> None:
    """Can index into transaction array."""
    acct = Account("jsh")
    acct.add_transaction(-1)
    acct.add_transaction(96)
    acct.add_transaction(0)
    assert acct[1] == 96


def test_eq() -> None:
    """Equality compares balances."""
    acctA = Account("jsh", 69)
    acctB = Account("jsh2")
    acctB.add_transaction(34)
    acctB.add_transaction(34)
    assert acctA != acctB
    acctB.add_transaction(1)
    assert acctA == acctB


def test_lt() -> None:
    """All inequalities work."""
    acctA = Account("jsh", 69)
    acctB = Account("jsh")
    assert acctB < acctA
    assert acctA > acctB
    assert not acctA < acctA
    assert not acctA > acctA


def test_add() -> None:
    """Addition merges accounts."""
    acctA = Account("jsh", 69)
    acctB = Account("jsh2", 70)
    acctA.add_transaction(1)
    acctB.add_transaction(2)
    acctB.add_transaction(3)
    sum = acctA + acctB
    assert sum.balance == 145
    assert sum.owner == "jsh&jsh2"
    assert len(sum) == 3
