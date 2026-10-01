from tax.residence import is_resident

RESIDENT_RATE = 0.13
NON_RESIDENT_RATE = 0.30


def calculate_tax(income: float, days_in_country: int) -> float:
    """Налог с дохода: 13% для резидента, 30% для нерезидента, округление до копеек."""
    if income < 0:
        raise ValueError("Income cannot be negative")
    rate = RESIDENT_RATE if is_resident(days_in_country) else NON_RESIDENT_RATE
    return round(income * rate, 2)
