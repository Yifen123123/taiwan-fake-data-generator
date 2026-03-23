"""Contact data generators for Taiwan fake data."""

from __future__ import annotations

import random
import string

EMAIL_SYLLABLES: list[str] = [
    "ming",
    "ting",
    "wei",
    "yu",
    "jun",
    "hao",
    "chen",
    "lin",
    "hsin",
    "chia",
    "yun",
    "pei",
    "kai",
    "hsuan",
    "shan",
]


def generate_gmail_address(rng: random.Random, existing: set[str]) -> str:
    """Generate a unique, Gmail-style fake email address."""
    while True:
        parts = [
            rng.choice(EMAIL_SYLLABLES),
            rng.choice(EMAIL_SYLLABLES),
            str(rng.randint(10, 9999)),
        ]
        if rng.random() < 0.35:
            local_part = ".".join(parts[:2]) + parts[2]
        else:
            local_part = "".join(parts)

        email = f"{local_part.lower()}@gmail.com"
        if email not in existing:
            existing.add(email)
            return email


def generate_taiwan_mobile(rng: random.Random, existing: set[str]) -> str:
    """Generate a unique Taiwan mobile number in 09xxxxxxxx format."""
    while True:
        phone = f"09{rng.randint(0, 99999999):08d}"
        if phone not in existing:
            existing.add(phone)
            return phone
