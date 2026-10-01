"""Обработка файла продаж и построение отчёта."""

from sales.report import (
    Sale,
    build_report,
    filter_by_threshold,
    read_sales,
    total_amount,
    totals_by_category,
)

__all__ = [
    "Sale",
    "build_report",
    "filter_by_threshold",
    "read_sales",
    "total_amount",
    "totals_by_category",
]
