"""Taiwan ID validation and checksum helpers."""

from __future__ import annotations

LETTER_CODE_MAP: dict[str, int] = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}


def calculate_taiwan_id_check_digit(prefix: str) -> str:
    """Calculate the final checksum digit for a 9-character Taiwan ID prefix."""
    if len(prefix) != 9:
        raise ValueError("Taiwan ID prefix must be 9 characters long.")

    letter = prefix[0]
    digits = prefix[1:]

    if letter not in LETTER_CODE_MAP or not digits.isdigit():
        raise ValueError("Invalid Taiwan ID prefix format.")

    letter_code = LETTER_CODE_MAP[letter]
    values = [letter_code // 10, letter_code % 10] + [int(digit) for digit in digits]
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    weighted_sum = sum(value * weight for value, weight in zip(values, weights))
    check_digit = (10 - (weighted_sum % 10)) % 10
    return str(check_digit)


def is_valid_taiwan_id(candidate: str) -> bool:
    """Validate a Taiwan ID string against its checksum rule."""
    if len(candidate) != 10:
        return False

    try:
        expected = calculate_taiwan_id_check_digit(candidate[:-1])
    except ValueError:
        return False

    return candidate[-1] == expected
