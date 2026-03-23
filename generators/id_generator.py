"""Taiwan ID generation helpers."""

from __future__ import annotations

import random

from utils.tw_id import calculate_taiwan_id_check_digit

AREA_LETTERS: list[str] = list("ABCDEFGHJKLMNPQRSTUVXYWZIO")
GENDERS: list[str] = ["1", "2"]


def generate_taiwan_id(rng: random.Random, existing: set[str]) -> str:
    """Generate a unique Taiwan national identification number."""
    while True:
        letter = rng.choice(AREA_LETTERS)
        gender = rng.choice(GENDERS)
        serial = f"{rng.randint(0, 9999999):07d}"
        prefix = f"{letter}{gender}{serial}"
        check_digit = calculate_taiwan_id_check_digit(prefix)
        candidate = f"{prefix}{check_digit}"

        if candidate not in existing:
            existing.add(candidate)
            return candidate
