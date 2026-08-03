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

    # ==================================================
    # PROJECT SUMMARY
    # ==================================================

    render_project_summary()

    st.markdown("---")

    # ==================================================
    # DELIVERY STATUS + NEXT 7 DAYS
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 📊 Delivery Status
            """
        )

        st.info(
            """
            Delivery Status Pie Chart
            """
        )

    with col2:

        st.markdown(
            """
            ### 📅 Next 7 Days
            """
        )

        st.info(
            """
            Upcoming activities issuing
            within the next 7 days.
            """
        )

    st.markdown("---")

    # ==================================================
    # DELIVERABLES & MILESTONES
    # ==================================================

    st.markdown(
        """
        ### 🚩 Deliverables & Milestones
        """
    )

    st.info(
        """
        CL31 vs CL32 milestone comparison
        and deliverable performance table.
        """
    )