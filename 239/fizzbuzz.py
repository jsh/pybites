"""Bite 239. Test FizzBuzz."""


def fizzbuzz(num):
    """Test divisibility."""
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num
