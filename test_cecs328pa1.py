# Tests for PA1 - Asymptotic Analysis
# Alex Gonzalez

# Asymptotic symbols used: O, Θ, Ω
import pytest

from cecs328pa1 import *


@pytest.mark.parametrize(
    "test_left_function, test_right_function, test_symbol, expected_result",
    [
        ("(log(n))^2", "lg(n^3)", "O", False),
        ("2*n^2+n*log(n)+5", "n^2", "Θ", True),
        ("n^2+n+5", "n*(log(n))^2", "Ω", True),
        ("n^2*log(n)+n", "n^2", "Ω", True),
        ("n^2*log(n)+n", "n^3", "Ω", False),
        ("5*n^2+n*log(n)", "n^2", "Θ", True),
    ],
)
def test_asymptotic_analysis(
    test_left_function, test_right_function, test_symbol, expected_result
):
    assert (
        asymptotic_analysis(test_left_function, test_right_function, test_symbol)
        == expected_result
    )
