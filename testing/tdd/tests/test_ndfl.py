from ndfl.calculator import calculate_ndfl


def test_zero_income_gives_zero_tax():
    assert calculate_ndfl(0) == 0


def test_basic_rate_is_13_percent():
    assert calculate_ndfl(100_000) == 13_000
    assert calculate_ndfl(1_000_000) == 130_000
