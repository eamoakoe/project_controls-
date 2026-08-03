import streamlit as st

from overview.ferry.project_summary import render as render_project_summary
from overview.ferry.pie_card_ferry import render_pie_ferry
from overview.ferry.next7days_cl32_ferry import render_next7days_table
from overview.ferry.milestone_cl32_ferry import render_milestone_table


def show_overview(asset):

    if asset != "Ferry PS":
        st.info(f"{asset} overview not built yet.")
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

        st.markdown("## Delivery Status")

        render_pie_ferry(programme_df)

    with col2:

        st.markdown("## Next 7 Days")

        render_next7days_table(programme_df)

    st.markdown("---")

    # ==========================================
    # DELIVERABLES
    # ==========================================

    render_milestone_table(programme_df)