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
    # DELIVERY STATUS + LOOKAHEAD
    # ==========================================

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("## 📊 Delivery Status")

        st.info(
            "Pie Chart Component Coming Next"
        )

    with col2:

        st.markdown("## 📅 Next 7 Days")

        st.info(
            "7-Day Lookahead Component Coming Next"
        )

    st.markdown("---")

    # ==========================================
    # DELIVERABLES
    # ==========================================

    st.markdown("## 🚩 Deliverables & Milestones")

    st.info(
        "Milestone Component Coming Next"
    )