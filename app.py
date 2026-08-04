import streamlit as st
import pandas as pd
from pathlib import Path
import re

from components.sidebar import render_sidebar
from pages.overview import show_overview

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Project Controls Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# LOAD CUSTOM CSS
# ==================================================

try:
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

except FileNotFoundError:
    st.warning("styles.css not found")

# ==================================================
# LOAD LATEST CL32 PROGRAMME
# ==================================================

MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def get_cl32_files():

    return list(Path(".").rglob("CL32*.xlsx"))


def get_file_version(file_path):

    filename = file_path.stem

    match = re.search(
        r"CL32-(January|February|March|April|May|June|July|August|September|October|November|December)-(\d{4})",
        filename,
        re.IGNORECASE
    )

    if not match:
        return (0, 0)

    month_name = match.group(1).title()
    year = int(match.group(2))

    return (
        year,
        MONTHS.get(month_name, 0)
    )


cl32_files = get_cl32_files()

if not cl32_files:

    st.error(
        "No CL32 programme files found. "
        "Expected files such as CL32-May-2026.xlsx "
        "or CL32-June-2026.xlsx."
    )

    st.stop()

latest_file = max(
    cl32_files,
    key=get_file_version
)

try:

    programme_df = pd.read_excel(latest_file)

    programme_df.columns = (
        programme_df.columns
        .astype(str)
        .str.strip()
    )

    programme_df["SnapshotDate"] = pd.Timestamp.today()

except Exception as e:

    st.error(
        f"Failed to load programme file: {e}"
    )

    st.stop()

# ==================================================
# SIDEBAR
# ==================================================

framework, asset, page = render_sidebar()

# ==================================================
# CURRENT FILE INFO
# ==================================================

st.sidebar.success(
    f"Programme Loaded:\n{latest_file.name}"
)

# ==================================================
# ROUTING
# ==================================================

if page == "Overview":

    show_overview(asset, programme_df)

elif page == "Framework Roadmap":

    st.subheader("Framework Roadmap")
    st.info("Framework Roadmap page coming next")

elif page == "Delivery & Programme":

    st.subheader("Delivery & Programme")
    st.info("Delivery & Programme page coming next")

elif page == "Communications":

    st.subheader("Communications")
    st.info("Communications page coming next")

elif page == "Documents":

    st.subheader("Documents")
    st.info("Documents page coming next")

elif page == "Reports":

    st.subheader("Reports")
    st.info("Reports page coming next")

elif page == "Settings":

    st.subheader("Settings")
    st.info("Settings page coming next")