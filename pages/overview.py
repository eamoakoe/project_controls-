import streamlit as st

from overview.ferry.project_summary import render as render_project_summary


def show_overview(asset):

    if asset != "Ferry PS":

        st.info(
            f"{asset} overview not built yet."
        )

        return

    render_project_summary()

    st.markdown("---")

    st.markdown("## 🚦 Project Health")

    st.info(
        """
        Status: AMBER

        Current Stage: Outline Design

        Next Gate: Scope Freeze

        Baseline Finish: 24 Sep 2026

        Forecast Finish: 20 Oct 2026

        Variance: -18 Days

        Terminal Float: 0 Days
        """
    )

    st.markdown("---")

    st.markdown("## 🛣 Framework Progress")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.success("✅ Feasibility")

    with c2:
        st.success("✅ Concept Design")

    with c3:
        st.warning("🟠 Outline Design")

    with c4:
        st.info("⚪ Detailed Design")

    with c5:
        st.info("⚪ Construction Support")

    st.markdown("---")

    st.markdown("## 📊 Key Metrics")

    m1, m2, m3, m4, m5, m6 = st.columns(6)

    m1.metric(
        "Today",
        "03 Aug 2026"
    )

    m2.metric(
        "Health",
        "AMBER"
    )

    m3.metric(
        "Forecast Finish",
        "20 Oct 2026"
    )

    m4.metric(
        "Variance",
        "-18 Days"
    )

    m5.metric(
        "Float",
        "0 Days"
    )

    m6.metric(
        "Comms",
        "1 Open"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("## 📅 Upcoming Milestones")

        st.write("• Scope Freeze - 14 Aug 2026")
        st.write("• Client Review Submission - 23 Sep 2026")
        st.write("• Outline Design Acceptance - 06 Oct 2026")
        st.write("• Detailed Design Start - 07 Oct 2026")
        st.write("• Project Completion - 20 Oct 2026")

    with col2:

        st.markdown("## 🚨 Actions Required")

        st.write("• Respond to outstanding RFI")
        st.write("• Client review pack due")
        st.write("• Deliverables awaiting acceptance")
        st.write("• Baseline variance exceeds threshold")