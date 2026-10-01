"""Чтение продаж из файла, подсчёт сумм и формирование отчёта.

Формат файла и правила валидации описаны в ``docs/SPECIFICATION.md``.
"""

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Sale:
    """Одна продажа — строка файла.

    :param product: название товара
    :param category: категория товара
    :param unit_price: цена за единицу, не меньше 0
    :param quantity: количество, целое больше 0
    """

    product: str
    category: str
    unit_price: float
    quantity: int

    @property
    def amount(self) -> float:
        """Сумма позиции: цена × количество."""
        return self.unit_price * self.quantity


def parse_line(line: str) -> Sale | None:
    """Разобрать строку файла.

    :param line: строка вида ``товар,категория,цена,количество``
    :return: запись :class:`Sale` или ``None``, если строка некорректна
    """
    parts = [part.strip() for part in line.split(",")]
    if len(parts) != 4:
        return None
    product, category, price_raw, quantity_raw = parts
    try:
        unit_price = float(price_raw)
        quantity = int(quantity_raw)
    except ValueError:
        return None
    if unit_price < 0 or quantity <= 0:
        return None
    return Sale(product, category, unit_price, quantity)


def read_sales(path: str | Path) -> list[Sale]:
    """Прочитать файл продаж в UTF-8.

    Некорректные и пустые строки пропускаются.

    :param path: путь к файлу
    :return: список корректных записей
    """
    sales = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            sale = parse_line(line)
            if sale is not None:
                sales.append(sale)
    return sales


def total_amount(sales: list[Sale], discount_percent: float = 0) -> float:
    """Итоговая сумма всех продаж со скидкой.

    :param sales: записи о продажах
    :param discount_percent: скидка в процентах, от 0 до 100
    :return: сумма, округлённая до копеек
    :raises ValueError: если скидка вне диапазона 0–100
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    total = sum(sale.amount for sale in sales)
    return round(total * (1 - discount_percent / 100), 2)


def filter_by_threshold(sales: list[Sale], threshold: float) -> list[Sale]:
    """Крупные продажи — сумма позиции не меньше порога.

    :param sales: записи о продажах
    :param threshold: порог суммы позиции
    :return: записи с ``amount >= threshold``
    """
    return [sale for sale in sales if sale.amount >= threshold]


def totals_by_category(sales: list[Sale]) -> dict[str, float]:
    """Суммы по категориям.

    :param sales: записи о продажах
    :return: словарь ``категория -> сумма``, суммы округлены до копеек
    """
    totals: dict[str, float] = defaultdict(float)
    for sale in sales:
        totals[sale.category] += sale.amount
    return {category: round(total, 2) for category, total in totals.items()}


def build_report(sales: list[Sale]) -> str:
    """Текстовый отчёт: заголовок, суммы по категориям (по алфавиту) и итог.

    :param sales: записи о продажах
    :return: текст отчёта
    """
    lines = ["Отчёт о продажах", ""]
    for category, total in sorted(totals_by_category(sales).items()):
        lines.append(f"{category}: {total:.2f}")
    lines.append("")
    lines.append(f"Итого: {total_amount(sales):.2f}")
    return "\n".join(lines)
