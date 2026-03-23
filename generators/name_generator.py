"""Chinese name generator for Taiwan-style fake data."""

from __future__ import annotations

import random

SURNAMES: list[str] = [
    "陳",
    "林",
    "黃",
    "張",
    "李",
    "王",
    "吳",
    "劉",
    "蔡",
    "楊",
    "許",
    "鄭",
    "謝",
    "洪",
    "郭",
    "邱",
    "曾",
    "廖",
    "賴",
    "徐",
]

GIVEN_NAME_CHARS: list[str] = [
    "志",
    "家",
    "冠",
    "承",
    "宗",
    "柏",
    "宇",
    "宏",
    "俊",
    "庭",
    "家",
    "佳",
    "怡",
    "佩",
    "雅",
    "欣",
    "婉",
    "品",
    "宥",
    "彥",
    "睿",
    "恩",
    "哲",
    "鈞",
    "穎",
    "芳",
    "婷",
    "萱",
    "芸",
    "潔",
    "詠",
    "翔",
    "翔",
    "豪",
    "凱",
    "妤",
    "心",
    "雯",
    "昕",
    "書",
    "維",
    "德",
    "昱",
    "柏",
]


def generate_chinese_name(rng: random.Random, existing: set[str]) -> str:
    """Generate a unique Taiwan-style Chinese name."""
    while True:
        surname = rng.choice(SURNAMES)
        given_length = 2 if rng.random() < 0.88 else 1
        given_name = "".join(rng.choice(GIVEN_NAME_CHARS) for _ in range(given_length))
        full_name = f"{surname}{given_name}"

        if full_name not in existing:
            existing.add(full_name)
            return full_name
