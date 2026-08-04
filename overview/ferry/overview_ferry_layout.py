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


def render_ferry_overview():

    # ==================================
    # SUMMARY
    # ==================================

    render_project_summary()

    # ==================================
    # INTELLIGENCE
    # ==================================

    render_intelligence_panel()

    # ==================================
    # FRAMEWORK
    # ==================================

    render_framework_progress()

    # ==================================
    # KPI CARDS
    # ==================================

    render_metric_cards()

    # ==================================
    # MILESTONES / ACTIONS
    # ==================================

    col1, col2 = st.columns([1, 1])

    with col1:
        render_upcoming_milestones()

    with col2:
        render_actions_required()

    # ==================================
    # DELIVERY STATUS / NEXT 7 DAYS
    # ==================================

    col1, col2 = st.columns([1, 1])

    with col1:
        render_pie_ferry()

    with col2:
        render_next7days_table()

    # ==================================
    # DELIVERABLES
    # ==================================

    render_milestone_table()