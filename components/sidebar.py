import streamlit as st
import datetime
import os
import base64


# =====================================================
# FRAMEWORK DATA
# =====================================================
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


# =====================================================
# LOAD LOGO
# =====================================================
def get_base64_image(path):

    if not os.path.exists(path):
        return None

    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


# =====================================================
# SIDEBAR
# =====================================================
def render_sidebar():

    logo = get_base64_image("assets/logo.png")

    st.markdown(
        """
        <style>

        [data-testid="stSidebarNav"] {
            display:none;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #dff7dc 0%,
                #c7efc3 100%
            );
        }

        .sidebar-card {
            background:white;
            padding:12px;
            border-radius:12px;
            margin-bottom:10px;
            box-shadow:0 1px 4px rgba(0,0,0,0.12);
        }

        .sidebar-title {
            font-size:20px;
            font-weight:700;
            text-align:center;
            margin-bottom:0px;
        }

        .sidebar-subtitle {
            text-align:center;
            color:#666;
            font-size:12px;
            margin-bottom:10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:

        # =================================================
        # LOGO
        # =================================================
        if logo:

            st.markdown(
                f"""
                <div style="text-align:center;padding-top:10px;">
                    logo}"
                        width="120">
                </div>
                """,
                unsafe_allow_html=True
            )

        # =================================================
        # HEADER
        # =================================================
        st.markdown(
            """
            <div class="sidebar-card">

                <div class="sidebar-title">
                    Project Controls Hub
                </div>

                <div class="sidebar-subtitle">
                    United Utilities
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PROJECT CONTEXT
        # =================================================
        st.markdown(
            """
            <div class="sidebar-card">
                <b>📁 Project Context</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        framework = st.selectbox(
            "Framework",
            list(FRAMEWORKS.keys())
        )

        asset = st.selectbox(
            "Asset",
            FRAMEWORKS[framework]
        )

        # =================================================
        # NAVIGATION
        # =================================================
        st.markdown(
            """
            <div class="sidebar-card">
                <b>📌 Navigation</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        page = st.radio(
            "",
            [
                "Overview",
                "Project Delivery",
                "Communications",
                "Reports",
                "Schedule",
                "Cost",
                "Risk",
                "Change Control",
                "Documents"
            ],
            label_visibility="collapsed"
        )

        # =================================================
        # PROJECT INFORMATION
        # =================================================
        today = datetime.datetime.today()

        st.markdown(
            f"""
            <div class="sidebar-card">

                <b>🏗️ Project Information</b>

                <hr>

                <b>Framework</b><br>
                {framework}

                <br><br>

                <b>Asset</b><br>
                {asset}

                <br><br>

                <b>Date</b><br>
                {today.strftime("%d %b %Y")}

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # KPI PLACEHOLDERS
        # =================================================
        st.markdown(
            """
            <div class="sidebar-card">
                <b>📊 Project Health</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Status",
                "🟢"
            )

        with col2:
            st.metric(
                "Health",
                "95%"
            )

        st.metric(
            "Schedule",
            "Placeholder"
        )

        st.metric(
            "Cost",
            "Placeholder"
        )

        st.metric(
            "Risk",
            "Placeholder"
        )

        # =================================================
        # NEXT DEADLINE PLACEHOLDER
        # =================================================
        st.markdown(
            """
            <div class="sidebar-card">

                <b>🎯 Next Deadline</b>

                <hr>

                Contract Submission

                <br><br>

                <b>01 August 2026</b>

                <br>

                ⏳ 7 Days Remaining

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PROGRAMME TRACKER PLACEHOLDER
        # =================================================
        st.markdown(
            """
            <div class="sidebar-card">

                <b>📅 Programme Tracker</b>

                <hr>

                ✅ Review Meeting

                <br>

                ✅ Cost Submission

                <br>

                ⚠️ Progress Update

                <br>

                ⏳ Executive Report

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # FOOTER
        # =================================================
        st.markdown("---")

        st.caption(
            "Project Controls Hub v1.0"
        )

    return framework, asset, page