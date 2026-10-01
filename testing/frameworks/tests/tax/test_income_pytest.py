import pytest

from tax.income import calculate_tax
from tax.residence import is_resident

INCOME = 100_000


@pytest.fixture
def resident_days() -> int:
    return 200


@pytest.mark.parametrize(
    "days, expected",
    [(0, False), (182, False), (183, True), (366, True)],
)
def test_residence_boundary(days, expected):
    assert is_resident(days) is expected


@pytest.mark.parametrize("days", [-1, 367])
def test_invalid_days_raise(days):
    with pytest.raises(ValueError):
        is_resident(days)


def test_resident_pays_13_percent(resident_days):
    assert calculate_tax(INCOME, resident_days) == 13_000


def test_non_resident_pays_30_percent():
    assert calculate_tax(INCOME, days_in_country=100) == 30_000


def test_tax_is_rounded_to_kopecks(resident_days):
    assert calculate_tax(100.55, resident_days) == pytest.approx(13.07)


def test_negative_income_raises(resident_days):
    with pytest.raises(ValueError, match="negative"):
        calculate_tax(-1, resident_days)
