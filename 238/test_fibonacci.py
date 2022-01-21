import pytest

from fibonacci import fib


def test_base_case() -> None:
    """Test 0, 1 terminating cases."""
    assert fib(0) == 0
    assert fib(1) == 1


@pytest.mark.parametrize(
    "arg, expected",
    [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (20, 6765),
        (True, 1),
        (False, 0),
    ],
)
def test_larger_cases(arg, expected) -> None:
    """Test a few other integers."""
    assert fib(arg) == expected

def test_no_arg():
    """Forget to pass an argument."""
    with pytest.raises(TypeError):
        assert fib()


@pytest.mark.parametrize(
    "bad_value, error",
    [
        (-1, ValueError),
        (3.14, ValueError),
    ]
)
def test_handled_error(bad_value, error) -> None:
    """Test caught error condition."""
    with pytest.raises(error):
        assert fib(bad_value)


@pytest.mark.parametrize(
    "bad_value, error",
    [
        ("foozbaz", TypeError),
        ((6, 9), TypeError),
        (["a", "b", "c"], TypeError),
        ({"x": 1}, TypeError),
        ({"x", "y"}, TypeError),
    ]
)
def test_unhandled_error(bad_value, error) -> None:
    """Test other bad input."""
    with pytest.raises(error):
        assert fib(bad_value)

