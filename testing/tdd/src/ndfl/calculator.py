def calculate_ndfl(income: float) -> float:
    if income <= 2_400_000:
        tax = income * 0.13
    elif income <= 5_000_000:
        tax = 312_000 + (income - 2_400_000) * 0.15
    elif income <= 20_000_000:
        tax = 702_000 + (income - 5_000_000) * 0.18
    elif income <= 50_000_000:
        tax = 3_402_000 + (income - 20_000_000) * 0.20
    else:
        tax = 9_402_000 + (income - 50_000_000) * 0.22
    return round(tax, 2)
