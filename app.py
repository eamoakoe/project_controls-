import streamlit as st
from components.sidebar import render_sidebar

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
# MAIN PAGE
# ==================================================

st.title("Project Controls Hub")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"**Framework**\n\n{framework}")

with col2:
    st.info(f"**Asset**\n\n{asset}")

with col3:
    st.info(f"**Page**\n\n{page}")

st.markdown("---")

st.subheader("Development Area")

if page == "Overview":
    st.success("Overview page coming next")

elif page == "Framework Roadmap":
    st.success("Framework Roadmap page coming next")

elif page == "Delivery & Programme":
    st.success("Delivery & Programme page coming next")

elif page == "Communications":
    st.success("Communications page coming next")

elif page == "Documents":
    st.success("Documents page coming next")

elif page == "Reports":
    st.success("Reports page coming next")

elif page == "Settings":
    st.success("Settings page coming next")