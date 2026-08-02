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

        # ------------------------------------------
        # FRAMEWORK
        # ------------------------------------------

        st.markdown("### Framework")

        framework = st.radio(
            "",
            list(FRAMEWORKS.keys()),
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ------------------------------------------
        # ASSET
        # ------------------------------------------

        st.markdown("### Asset")

        asset = st.radio(
            "",
            FRAMEWORKS[framework],
            label_visibility="collapsed"
        )

        st.markdown("---")

        # ------------------------------------------
        # NAVIGATION
        # ------------------------------------------

        st.markdown("### Navigation")

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

        render_programme_tracker()

        st.markdown("---")

        render_next_deadline()

    return framework, asset, page