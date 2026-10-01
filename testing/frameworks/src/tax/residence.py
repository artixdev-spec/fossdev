RESIDENCE_DAYS_THRESHOLD = 183
DAYS_IN_YEAR = 366


def is_resident(days_in_country: int) -> bool:
    """Налоговый резидент РФ — находится в стране 183 дня и больше за 12 месяцев."""
    if not 0 <= days_in_country <= DAYS_IN_YEAR:
        raise ValueError("days_in_country must be between 0 and 366")
    return days_in_country >= RESIDENCE_DAYS_THRESHOLD
