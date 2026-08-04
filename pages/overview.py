import streamlit as st

from overview.ferry.project_summary import render as render_project_summary
from overview.ferry.intelligence_panel import render as render_intelligence_panel
from overview.ferry.framework_progress import render as render_framework_progress
from overview.ferry.metric_cards import render as render_metric_cards
from overview.ferry.upcoming_milestones import render as render_upcoming_milestones
from overview.ferry.actions_required import render as render_actions_required


def show_overview(asset):

    if asset != "Ferry PS":
        st.info(f"{asset} overview not built yet.")
        return

    # ==================================
    # PROJECT SUMMARY
    # ==================================

    render_project_summary()

    st.markdown("---")

    # ==================================
    # INTELLIGENCE PANEL
    # ==================================

    render_intelligence_panel()

    st.markdown("---")

    # ==================================
    # FRAMEWORK PROGRESS
    # ==================================

    render_framework_progress()

    st.markdown("---")

    # ==================================
    # KPI METRICS
    # ==================================

    render_metric_cards()

    st.markdown("---")

    # ==================================
    # MILESTONES / ACTIONS
    # ==================================

    col1, col2 = st.columns(2)

    with col1