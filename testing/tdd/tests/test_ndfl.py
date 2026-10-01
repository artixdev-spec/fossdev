import pytest

from ndfl.calculator import TaxpayerType, calculate_ndfl


def test_zero_income_gives_zero_tax():
    assert calculate_ndfl(0) == 0


def test_basic_rate_is_13_percent():
    assert calculate_ndfl(100_000) == 13_000
    assert calculate_ndfl(1_000_000) == 130_000


@pytest.mark.parametrize(
    "income, expected",
    [
        (2_400_000, 312_000),
        (5_000_000, 702_000),
        (20_000_000, 3_402_000),
        (50_000_000, 9_402_000),
    ],
)
def test_tax_on_bracket_boundaries(income, expected):
    assert calculate_ndfl(income) == expected


@pytest.mark.parametrize(
    "income, expected",
    [
        (3_000_000, 312_000 + 600_000 * 0.15),
        (10_000_000, 702_000 + 5_000_000 * 0.18),
        (30_000_000, 3_402_000 + 10_000_000 * 0.20),
        (60_000_000, 9_402_000 + 10_000_000 * 0.22),
    ],
)
def test_higher_rate_applies_only_to_excess(income, expected):
    assert calculate_ndfl(income) == pytest.approx(expected)


def test_tax_is_rounded_to_kopecks():
    assert calculate_ndfl(100.55) == 13.07


def test_negative_income_raises():
    with pytest.raises(ValueError):
        calculate_ndfl(-1)


def test_general_taxpayer_is_default():
    assert calculate_ndfl(10_000_000) == calculate_ndfl(
        10_000_000, TaxpayerType.GENERAL
    )


@pytest.mark.parametrize(
    "income, expected",
    [
        (2_400_000, 312_000),
        (10_000_000, 312_000 + 7_600_000 * 0.15),
        (60_000_000, 312_000 + 57_600_000 * 0.15),
    ],
)
def test_investment_income_has_only_two_rates(income, expected):
    assert calculate_ndfl(income, TaxpayerType.INVESTMENT) == pytest.approx(expected)


@pytest.mark.parametrize(
    "income, expected",
    [
        (3_000_000, 3_000_000 * 0.13),
        (5_000_000, 650_000),
        (6_000_000, 650_000 + 1_000_000 * 0.15),
    ],
)
def test_northern_taxpayer_has_higher_threshold(income, expected):
    assert calculate_ndfl(income, TaxpayerType.NORTHERN) == pytest.approx(expected)
