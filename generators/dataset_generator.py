"""Dataset assembly for Taiwan fake data."""

from __future__ import annotations

import random

import pandas as pd

from generators.address_generator import build_taiwan_address
from generators.birthdate_generator import generate_birthdate
from generators.contact_generator import generate_gmail_address, generate_taiwan_mobile
from generators.id_generator import generate_taiwan_id
from generators.name_generator import generate_chinese_name


def generate_fake_dataset(count: int, seed: int | None = None) -> pd.DataFrame:
    """Generate a dataframe of Taiwan-style fake test data."""
    rng = random.Random(seed)
    email_set: set[str] = set()
    phone_set: set[str] = set()
    id_set: set[str] = set()
    name_set: set[str] = set()
    birthdate_set: set[str] = set()

    rows: list[dict[str, str]] = []

    for _ in range(count):
        rows.append(
            {
                "中文姓名": generate_chinese_name(rng, name_set),
                "出生年月日": generate_birthdate(rng, birthdate_set),
                "Gmail 格式信箱": generate_gmail_address(rng, email_set),
                "台灣手機號碼": generate_taiwan_mobile(rng, phone_set),
                "台灣地址": build_taiwan_address(rng),
                "台灣身分證字號": generate_taiwan_id(rng, id_set),
            }
        )

    return pd.DataFrame(rows)
