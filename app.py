import streamlit as st

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
# SIDEBAR
# ==================================================

framework, asset, page = render_sidebar()

# ==================================================
# PAGE ROUTING
# ==================================================

if page == "Overview":

    show_overview(asset)

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