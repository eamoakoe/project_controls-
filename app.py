import streamlit as st

from overview.ferry.project_summary import (
    render as render_project_summary
)


def show_overview(asset):

    if asset != "Ferry PS":

        st.info(
            f"{asset} overview not built yet."
        )

        return

    # ==========================================
    # PROJECT SUMMARY
    # ==========================================

    render_project_summary()

    st.markdown("---")

    # ==========================================
    # PLACEHOLDERS
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("## 📊 Delivery Status")

        st.info(
            "Pie chart component coming next."
        )

    with col2:

        st.markdown("## 📅 Next 7 Days")

        st.info(
            "7-day lookahead component coming next."
        )

    st.markdown("---")

    st.markdown("## 🚩 Deliverables & Milestones")

    st.info(
        "Milestone and deliverables component coming next."
    )