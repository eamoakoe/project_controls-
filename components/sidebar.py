import streamlit as st
import pandas as pd
import datetime
import os
import base64


# ==========================================
# FRAMEWORKS
# ==========================================
FRAMEWORKS = {
    "UU DD&B Framework": [
        "Flass Lane",
        "Ferry PS",
        "Rossall Outfall",
        "Ecclestone Bridge",
        "Tally Ho",
        "Harbour Yard"
    ],

    "UU Enterprise Framework": [
        "Pennington Flash",
        "ASP4"
    ]
}


# ==========================================
# LOAD LOGO
# ==========================================
def get_base64_image(path):

    if not os.path.exists(path):
        return ""

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ==========================================
# NEXT DEADLINE
# ==========================================
def render_next_deadline():

    file_path = "components/contract_submission_dates.xlsx"

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

        try:
            day = int(row[month])
            deadline = datetime.date(year, today.month, day)

            days_remaining = (deadline - today_date).days

            if days_remaining >= 0:
                if min_days is None or days_remaining < min_days:
                    min_days = days_remaining
                    next_item = row

        except:
            continue

    if next_item is None:
        return

    st.sidebar.markdown("---")

    st.sidebar.markdown(
        f"""
        <div style="
            background:#ffffff;
            padding:10px;
            border-radius:8px;
            border-left:5px solid #e53935;
        ">
            <b>🎯 Next Deadline</b><br>
            {next_item['KEY']}<br>
            <b>{int(next_item[month])} {month}</b><br>
            ⏳ In {min_days} day(s)
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# PROGRAMME TRACKER
# ==========================================
def render_programme_tracker():

    file_path = "components/contract_submission_dates.xlsx"

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

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### 📅 {month} Programme")

    for _, row in current.iterrows():

        try:

            key = row["KEY"]
            day = int(row[month])

            if day < today_day:
                status = "✅"
            elif day == today_day:
                status = "⚠️"
            else:
                status = ""

            st.sidebar.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:space-between;
                    background:#f2f2f2;
                    padding:6px;
                    margin:2px 0;
                    border-radius:4px;
                    font-size:12px;
                ">
                    <span>{key}</span>
                    <span><b>{day}</b> {status}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        except:
            continue


# ==========================================
# SIDEBAR
# ==========================================
def render_sidebar():

    logo = get_base64_image("assets/logo.png")

    st.markdown(
        """
        <style>

        [data-testid="stSidebarNav"] {
            display:none;
        }

        section[data-testid="stSidebar"] {
            background:linear-gradient(
                180deg,
                #d4f5d0 0%,
                #a8e6a3 100%
            );
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:

        # ==================================
        # LOGO
        # ==================================
        if logo:
            st.markdown(
                f"""
                <div style="text-align:center; padding:10px 0 15px 0;">
                    data:image/png;base64,{logo}="110">
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <h2 style='text-align:center; margin-bottom:0;'>
            Project Controls Hub
            </h2>
            <p style='text-align:center; color:#444;'>
            United Utilities
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        # ==================================
        # FRAMEWORK
        # ==================================
        framework = st.radio(
            "📁 Framework",
            list(FRAMEWORKS.keys())
        )

        # ==================================
        # ASSET
        # ==================================
        asset = st.selectbox(
            "🏗️ Asset",
            FRAMEWORKS[framework]
        )

        st.markdown("---")

        # ==================================
        # PAGE NAVIGATION
        # ==================================
        page = st.radio(
            "📌 Navigation",
            [
                "Overview",
                "Project Delivery",
                "Communications",
                "Reports"
            ]
        )

        # ==================================
        # EXISTING WIDGETS
        # ==================================
        render_programme_tracker()

        render_next_deadline()

        st.markdown("---")

        st.caption("Project Controls Hub v1.0")

    return framework, asset, page