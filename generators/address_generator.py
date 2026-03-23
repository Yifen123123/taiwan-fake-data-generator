"""Address generation utilities for Taiwan-style fake data."""

from __future__ import annotations

import random

CITY_DISTRICTS: dict[str, list[str]] = {
    "台北市": ["中正區", "大安區", "信義區", "松山區", "內湖區", "士林區"],
    "新北市": ["板橋區", "中和區", "新莊區", "新店區", "三重區", "永和區"],
    "桃園市": ["桃園區", "中壢區", "龜山區", "八德區", "蘆竹區"],
    "台中市": ["西屯區", "北屯區", "南屯區", "西區", "北區", "豐原區"],
    "台南市": ["中西區", "東區", "永康區", "安平區", "北區"],
    "高雄市": ["前鎮區", "左營區", "三民區", "鼓山區", "鳳山區"],
    "新竹市": ["東區", "北區", "香山區"],
    "嘉義市": ["東區", "西區"],
}

ROAD_NAMES: list[str] = [
    "中山",
    "中正",
    "民生",
    "民權",
    "忠孝",
    "和平",
    "仁愛",
    "信義",
    "復興",
    "光復",
    "建國",
    "成功",
    "文化",
    "自由",
    "敦化",
]

ROAD_TYPES: list[str] = ["路", "街", "大道"]


def build_taiwan_address(rng: random.Random) -> str:
    """Build a natural-looking Taiwan-style fake address."""
    city = rng.choice(list(CITY_DISTRICTS))
    district = rng.choice(CITY_DISTRICTS[city])
    road = rng.choice(ROAD_NAMES)
    road_type = rng.choice(ROAD_TYPES)

    section = f"{rng.randint(1, 7)}段" if rng.random() < 0.45 else ""
    lane = f"{rng.randint(1, 120)}巷" if rng.random() < 0.55 else ""
    alley = f"{rng.randint(1, 80)}弄" if rng.random() < 0.4 else ""
    number = f"{rng.randint(1, 300)}號"
    floor = f"{rng.randint(1, 18)}樓" if rng.random() < 0.7 else ""
    room = f"之{rng.randint(1, 6)}" if floor and rng.random() < 0.25 else ""

    return f"{city}{district}{road}{road_type}{section}{lane}{alley}{number}{floor}{room}"
