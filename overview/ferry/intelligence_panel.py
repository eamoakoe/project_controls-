import streamlit as st
import pandas as pd


def render(df):

    # ==================================================
    # VALIDATION
    # ==================================================

    if df is None:
        st.info("Programme data not available.")
        return

    if df.empty:
        st.info("Programme data not loaded yet.")
        return

    df = df.copy()

    df.columns = df.columns.astype(str).str.strip()

    required_columns = [
        "SnapshotDate",
        "Finish",
        "Total Float",
        "Activity % Complete"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:

        st.warning(
            f"Missing programme columns: {', '.join(missing_columns)}"
        )

        st.write("Available columns:")
        st.write(df.columns.tolist())

        return

    # ==================================================
    # EXISTING CODE CONTINUES BELOW
    # ==================================================

    latest_date = pd.to_datetime(
        df["SnapshotDate"],
        errors="coerce"
    ).max()

    latest_df = df[
        pd.to_datetime(
            df["SnapshotDate"],
            errors="coerce"
        ) == latest_date
    ].copy()
