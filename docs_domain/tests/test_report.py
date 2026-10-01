import pytest

from sales import (
    Sale,
    build_report,
    filter_by_threshold,
    read_sales,
    total_amount,
    totals_by_category,
)
from sales.report import parse_line

COFFEE = Sale("Кофе", "напитки", 150.5, 2)
CROISSANT = Sale("Круассан", "выпечка", 90, 3)
TEA = Sale("Чай", "напитки", 100, 1)
SALES = [COFFEE, CROISSANT, TEA]


@pytest.mark.parametrize(
    "line",
    [
        "Кофе,напитки,150.5",
        "Кофе,напитки,150.5,2,лишнее",
        "Кофе,напитки,дорого,2",
        "Кофе,напитки,150.5,2.5",
        "Кофе,напитки,-1,2",
        "Кофе,напитки,150.5,0",
        "",
    ],
)
def test_invalid_line_is_skipped(line):
    assert parse_line(line) is None


def test_read_sales_skips_bad_lines(tmp_path):
    path = tmp_path / "sales.txt"
    path.write_text(
        "Кофе,напитки,150.5,2\nсломанная строка\n\nКруассан,выпечка,90,3\n",
        encoding="utf-8",
    )
    assert read_sales(path) == [COFFEE, CROISSANT]


def test_total_amount():
    assert total_amount(SALES) == 671


def test_total_amount_with_discount():
    assert total_amount(SALES, discount_percent=10) == 603.9


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount_raises(discount):
    with pytest.raises(ValueError):
        total_amount(SALES, discount)


def test_filter_by_threshold_includes_boundary():
    assert filter_by_threshold(SALES, 270) == [COFFEE, CROISSANT]


def test_totals_by_category():
    assert totals_by_category(SALES) == {"напитки": 401, "выпечка": 270}


def test_build_report():
    assert build_report(SALES) == (
        "Отчёт о продажах\n\nвыпечка: 270.00\nнапитки: 401.00\n\nИтого: 671.00"
    )
