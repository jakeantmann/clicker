"""Unit tests for type_dict library."""

from contextlib import nullcontext as does_not_raise

import pytest


def divide(dividend, divisor):
    """Divide two numbers."""
    return dividend / divisor


@pytest.mark.parametrize(
    "divisor,expectation",
    [
        (1, does_not_raise()),
        (0, pytest.raises(ZeroDivisionError)),
    ],
)
def test_divisor(divisor, expectation):
    """Parameterised test example.

    Args:
        divisor (int): 1 or 0
        expectation (Any): pytest.raises object
    """
    with expectation:
        divide(1, divisor)
