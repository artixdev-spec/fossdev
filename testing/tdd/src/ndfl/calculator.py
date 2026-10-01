import math
from enum import Enum

Scale = list[tuple[float, float]]


class TaxpayerType(Enum):
    GENERAL = "general"
    INVESTMENT = "investment"
    NORTHERN = "northern"


# (верхняя граница ступени, ставка) — ставка применяется к части дохода внутри ступени
SCALES: dict[TaxpayerType, Scale] = {
    TaxpayerType.GENERAL: [
        (2_400_000, 0.13),
        (5_000_000, 0.15),
        (20_000_000, 0.18),
        (50_000_000, 0.20),
        (math.inf, 0.22),
    ],
    TaxpayerType.INVESTMENT: [
        (2_400_000, 0.13),
        (math.inf, 0.15),
    ],
    TaxpayerType.NORTHERN: [
        (5_000_000, 0.13),
        (math.inf, 0.15),
    ],
}


def _tax_by_scale(income: float, scale: Scale) -> float:
    tax = 0.0
    lower = 0.0
    for upper, rate in scale:
        if income <= lower:
            break
        tax += (min(income, upper) - lower) * rate
        lower = upper
    return tax


def calculate_ndfl(
    income: float, taxpayer: TaxpayerType = TaxpayerType.GENERAL
) -> float:
    if income < 0:
        raise ValueError("Income cannot be negative")
    return round(_tax_by_scale(income, SCALES[taxpayer]), 2)
