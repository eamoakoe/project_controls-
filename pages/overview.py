import streamlit as st

from overview.ferry.project_summary import render as render_project_summary
from overview.ferry.intelligence_panel import render as render_intelligence_panel
from overview.ferry.framework_progress import render as render_framework_progress
from overview.ferry.metric_cards import render as render_metric_cards
from overview.ferry.upcoming_milestones import render as render_upcoming_milestones
from overview.ferry.actions_required import render as render_actions_required
from overview.ferry.pie_card_ferry import render_pie_ferry
from overview.ferry.next7days_cl32_ferry import render_next7days_table
from overview.ferry.milestone_cl32_ferry import render_milestone_table
from overview.ferry.deliverables_ferry import render_deliverables_table


def show_overview(asset):

    if asset != "Ferry PS":
        st.info(f"{asset} overview not built yet.")
        return

    # ==================================================
    # PROJECT HEADER
    # ==================================================

    render_project_summary()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # PROJECT HEALTH
    # ==================================================

    render_intelligence_panel()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # FRAMEWORK PROGRESS
    # ==================================================

    render_framework_progress()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # KPI METRICS
    # ==================================================

    render_metric_cards()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # UPCOMING MILESTONES | ACTIONS REQUIRED
    # ==================================================

    left_col, right_col = st.columns([1, 1])

    with left_col:
        render_upcoming_milestones()

    with right_col:
        render_actions_required()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # DELIVERY STATUS | NEXT 7 DAYS
    # ==================================================

    left_col, right_col = st.columns([1, 1])

    with left_col:

        st.markdown("### Delivery Status")

        render_pie_ferry(programme_df)

    with right_col:

        st.markdown("### Next 7 Days")

        render_next7days_table()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # DELIVERABLE PERFORMANCE
    # ==================================================

    render_milestone_table()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ==================================================
    # CL31 vs CL32 COMPARISON
    # ==================================================

    render_deliverables_table()