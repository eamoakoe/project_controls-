import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header

from modules.overview import render_overview
from modules.project_delivery import render_project_delivery
from modules.communications import render_communications
from modules.reports import render_reports


# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="UU Project Controls Hub",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# SIDEBAR
# ==========================================
framework, asset, page = render_sidebar()


# ==========================================
# HEADER
# ==========================================
render_header(
    framework,
    asset,
    page
)


# ==========================================
# PAGE ROUTING
# ==========================================
try:

    if page == "Overview":

        render_overview(
            framework,
            asset
        )

    elif page == "Project Delivery":

        render_project_delivery(asset)

    elif page == "Communications":

        render_communications(asset)

    elif page == "Reports":

        render_reports(asset)

    else:

        st.warning("Page not found.")

except Exception as e:

    st.error(f"Error loading page: {e}")