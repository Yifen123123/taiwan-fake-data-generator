"""Export helpers for dataframe downloads."""

from __future__ import annotations

from io import BytesIO

import pandas as pd


def dataframe_to_csv_bytes(df: pd.DataFrame) -> bytes:
    """Export dataframe to UTF-8 CSV bytes with BOM for Excel compatibility."""
    return df.to_csv(index=False).encode("utf-8-sig")


def dataframe_to_excel_bytes(df: pd.DataFrame) -> bytes:
    """Export dataframe to XLSX bytes."""
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="fake_data")
    output.seek(0)
    return output.getvalue()
