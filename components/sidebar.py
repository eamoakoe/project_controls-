import streamlit as st
import pandas as pd
import datetime
import os


# ==================================================
# FRAMEWORKS
# ==================================================

FRAMEWORKS = {

    "UU DD&B Framework": [
        "Ferry PS",
        "Flass Lane",
        "Tally Ho",
        "Rossall Outfall",
        "Eccleston Bridge"
    ],

    "UU Enterprise Framework": [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]
}


# ==================================================
# NEXT DEADLINE
# ==================================================

def render_next_deadline():

    file_path = "subcontract/contract_submission_dates.xlsx"

    if not os.path.exists(file_path):
        return

    df = pd.read_excel(file_path)

    df.columns = df.columns.str.strip()

    today = datetime.datetime.today()

    month = today.strftime("%B")
    year = today.year
    today_date = today.date()

    if month not in df.columns:
        return

    current = df[["KEY", month]].dropna()

    next_item = None
    min_days = None

    for _, row in current.iterrows():

        day = int(row[month])

        try:
            deadline_date = datetime.date(
                year,
                today.month,
                day
            )

        except Exception:
            continue

        days_remaining = (
            deadline_date - today_date
        ).days

        if days_remaining >= 0:

            if (
                min_days is None
                or days_remaining < min_days
            ):
                min_days = days_remaining
                next_item = row

    if next_item is None:
        return

    key = next_item["KEY"]
    day = int(next_item[month])

    st.markdown("### 🎯 Next Deadline")

    st.markdown(
        f"""
        <div style="
            background:#0f1e56;
            padding:12px;
            border-radius:8px;
            border-left:4px solid #ff4d4d;
            margin-top:5px;
        ">
            <div style="
                font-size:14px;
                font-weight:600;
                color:white;
                margin-bottom:6px;
            ">
                {key}
            </div>

            <div style="
                color:#d9d9d9;
                margin-bottom:6px;
            ">
                → <strong>{day} {month}</strong>
            </div>

            <div style="
                color:#ffd54f;
                font-size:13px;
            ">
                ⏳ In {min_days} day(s)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# SIDEBAR
# ==================================================

def render_sidebar():

    with st.sidebar:

        # ------------------------------------------
        # LOGO
        # ------------------------------------------

        if os.path.exists("assets/logo.png"):

            st.image(
                "assets/logo.png",
                width=180
            )

        st.markdown("---")

        # ------------------------------------------
        # FRAMEWORK
        # ------------------------------------------

        st.markdown("### Framework")

        framework = st.radio(
            "",
            options=list(FRAMEWORKS.keys()),
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ------------------------------------------
        # ASSET
        # ------------------------------------------

        st.markdown("### Asset")

        asset = st.radio(
            "",
            options=FRAMEWORKS[framework],
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ------------------------------------------
        # NAVIGATION
        # ------------------------------------------

        st.markdown("### Navigation")

        page = st.radio(
            "",
            options=[
                "Overview",
                "Framework Roadmap",
                "Delivery & Programme",
                "Communications",
                "Documents",
                "Reports",
                "Settings"
            ],
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ------------------------------------------
        # NEXT DEADLINE
        # ------------------------------------------

        render_next_deadline()

    return framework, asset, page