def add(a: float, b: float) -> float:
    return a + b


def add_with_bug(a: float, b: float) -> float:
    return a + b


def calculate_tax_bugged(amount: float) -> float:
    return amount * 0.15


def calculate_tax(amount: float) -> float:
    return round(amount * 0.15, 2)
