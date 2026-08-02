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

        except:
            continue

        days_remaining = (
            deadline_date - today_date
        ).days

        if days_remaining >= 0:

            if (
                min_days is None
                or
                days_remaining < min_days
            ):

                min_days = days_remaining
                next_item = row

    if next_item is None:
        return

    key = next_item["KEY"]

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:white;
            margin-bottom:5px;
        ">
            NEXT DEADLINE
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            background:#1b1464;
            padding:12px;
            border-radius:10px;
            border-left:4px solid #ff5252;
            margin-bottom:10px;
        ">

            <div style="
                color:white;
                font-weight:600;
                margin-bottom:5px;
            ">
                🎯 {key}
            </div>

            <div style="
                color:#d1d1d1;
                font-size:13px;
            ">
                {int(next_item[month])} {month}
            </div>

            <div style="
                color:#ffd54f;
                font-size:12px;
                margin-top:5px;
            ">
                ⏳ {min_days} days remaining
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# PROGRAMME TRACKER
# ==================================================

def render_programme_tracker():

    file_path = "subcontract/contract_submission_dates.xlsx"

    if not os.path.exists(file_path):
        return

    df = pd.read_excel(file_path)

    df.columns = df.columns.str.strip()

    today = datetime.datetime.today()

    month = today.strftime("%B")
    today_day = today.day

    if month not in df.columns:
        return

    current = df[["KEY", month]].dropna()

    st.markdown(
        f"""
        <div style="
            font-size:12px;
            color:white;
            margin-bottom:8px;
        ">
            📅 {month.upper()} PROGRAMME
        </div>
        """,
        unsafe_allow_html=True
    )

    for _, row in current.iterrows():

        key = row["KEY"]
        day = int(row[month])

        if day < today_day:
            status = "✅"

        elif day == today_day:
            status = "⚠️"

        else:
            status = ""

        st.markdown(
            f"""
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                background:#ffffff10;
                padding:8px;
                margin-bottom:4px;
                border-radius:6px;
                font-size:12px;
                color:white;
            ">

                <span>{key}</span>

                <span>
                    <b>{day}</b>
                    {status}
                </span>

            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# SIDEBAR
# ==================================================

def render_sidebar():

    with st.sidebar:

        # ----------------------------------------------
        # LOGO
        # ----------------------------------------------

        if os.path.exists("assets/logo.png"):

            st.image(
                "assets/logo.png",
                width=180
            )

        # ----------------------------------------------
        # FRAMEWORK
        # ----------------------------------------------

        st.markdown("### FRAMEWORK")

        framework = st.radio(
            "",
            list(FRAMEWORKS.keys()),
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ----------------------------------------------
        # ASSET
        # ----------------------------------------------

        st.markdown("### ASSET")

        asset = st.radio(
            "",
            FRAMEWORKS[framework],
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ----------------------------------------------
        # NAVIGATION
        # ----------------------------------------------

        st.markdown("### NAVIGATION")

        page = st.radio(
            "",
            [
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

        # ----------------------------------------------
        # DEADLINE
        # ----------------------------------------------

        render_next_deadline()

        st.markdown("---")

        # ----------------------------------------------
        # PROGRAMME
        # ----------------------------------------------

        render_programme_tracker()

    return framework, asset, page