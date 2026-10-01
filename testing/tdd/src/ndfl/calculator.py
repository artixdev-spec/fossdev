import math

Scale = list[tuple[float, float]]

# (верхняя граница ступени, ставка) — ставка применяется к части дохода внутри ступени
GENERAL_SCALE: Scale = [
    (2_400_000, 0.13),
    (5_000_000, 0.15),
    (20_000_000, 0.18),
    (50_000_000, 0.20),
    (math.inf, 0.22),
]


def _tax_by_scale(income: float, scale: Scale) -> float:
    tax = 0.0
    lower = 0.0
    for upper, rate in scale:
        if income <= lower:
            break
        tax += (min(income, upper) - lower) * rate
        lower = upper
    return tax


def calculate_ndfl(income: float) -> float:
    if income < 0:
        raise ValueError("Income cannot be negative")
    return round(_tax_by_scale(income, GENERAL_SCALE), 2)
