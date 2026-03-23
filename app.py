"""Streamlit app for generating Taiwan-style fake test data."""

from __future__ import annotations

import streamlit as st

from generators.dataset_generator import generate_fake_dataset
from utils.exporters import dataframe_to_csv_bytes, dataframe_to_excel_bytes


def main() -> None:
    """Render the Streamlit application."""
    st.set_page_config(
        page_title="台灣假資料產生器",
        page_icon="📄",
        layout="wide",
    )

    st.title("台灣假資料產生器")
    st.caption("所有資料皆為測試用途的假資料，請勿作為真實個資使用。")

    count = st.selectbox("選擇要產生的筆數", options=[10, 50, 100, 500], index=0)

    if "generated_df" not in st.session_state:
        st.session_state.generated_df = None

    if st.button("產生假資料", type="primary", use_container_width=True):
        st.session_state.generated_df = generate_fake_dataset(count)

    generated_df = st.session_state.generated_df

    if generated_df is not None:
        st.subheader("產生結果")
        st.write(f"本次產生資料筆數：{len(generated_df)} 筆")
        st.dataframe(generated_df, use_container_width=True, hide_index=True)

        csv_bytes = dataframe_to_csv_bytes(generated_df)
        excel_bytes = dataframe_to_excel_bytes(generated_df)

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="下載 CSV",
                data=csv_bytes,
                file_name="taiwan_fake_data.csv",
                mime="text/csv",
                use_container_width=True,
            )
        with col2:
            st.download_button(
                label="下載 Excel（xlsx）",
                data=excel_bytes,
                file_name="taiwan_fake_data.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                ),
                use_container_width=True,
            )


if __name__ == "__main__":
    main()
