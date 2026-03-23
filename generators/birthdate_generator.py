"""Birthdate generator for Taiwan fake data."""

from __future__ import annotations

from datetime import date, timedelta
import random


def format_minguo_date(value: date) -> str:
    """Convert a Gregorian date to Taiwan Minguo format: YYY年MM月DD日."""
    minguo_year = value.year - 1911
    return f"{minguo_year:02d}年{value.month:02d}月{value.day:02d}日"


def generate_birthdate(
    rng: random.Random,
    existing: set[str] | None = None,
    min_age: int = 18,
    max_age: int = 80,
) -> str:
    """Generate a realistic fake birthdate string in Taiwan Minguo format."""
    today = date.today()
    youngest = today.replace(year=today.year - min_age)
    oldest = today.replace(year=today.year - max_age)
    date_span_days = (youngest - oldest).days

    # Prefer non-duplicate dates within the current batch, but do not require uniqueness.
    for _ in range(20):
        offset_days = rng.randint(0, date_span_days)
        birthdate = oldest + timedelta(days=offset_days)
        birthdate_str = format_minguo_date(birthdate)

        if existing is None or birthdate_str not in existing:
            if existing is not None:
                existing.add(birthdate_str)
            return birthdate_str

    fallback_birthdate = oldest + timedelta(days=rng.randint(0, date_span_days))
    return format_minguo_date(fallback_birthdate)
