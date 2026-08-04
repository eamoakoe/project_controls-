import streamlit as st
import pandas as pd


def render(df):

    if df is None or df.empty:
        st.warning("No programme data available.")
        return

    df = df.copy()
    df.columns = df.columns.astype(str).str.strip()

    required_columns = [
        "BL1 Finish",
        "Finish",
        "Total Float",
        "Activity % Complete"
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        st.error(
            f"Missing required columns: {', '.join(missing)}"
        )
        return

    # ========================================
    # CLEAN DATA
    # ========================================

    df["BL1 Finish"] = pd.to_datetime(
        df["BL1 Finish"],
        errors="coerce",
        dayfirst=True
    )

    df["Finish"] = pd.to_datetime(
        df["Finish"],
        errors="coerce",
        dayfirst=True
    )

    df["Total Float"] = pd.to_numeric(
        df["Total Float"],
        errors="coerce"
    )

    df["Activity % Complete"] = (
        df["Activity % Complete"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    df["Activity % Complete"] = pd.to_numeric(
        df["Activity % Complete"],
        errors="coerce"
    ).fillna(0)

    # ========================================
    # KPI CALCULATIONS
    # ========================================

    baseline_finish = df["BL1 Finish"].max()

    forecast_finish = df["Finish"].max()

    variance_days = int(
        (forecast_finish - baseline_finish).days
    )

    terminal_float = int(
        df["Total Float"].min()
    )

    outstanding = len(
        df[df["Activity % Complete"] < 100]
    )

    # ========================================
    # HEALTH
    # ========================================

    if variance_days <= 7 and terminal_float > 0:

        health = "GREEN"
        colour = "#22c55e"

    elif variance_days <= 28:

        health = "AMBER"
        colour = "#f59e0b"

    else:

        health = "RED"
        colour = "#ef4444"

    # ========================================
    # PROJECT INFORMATION
    # ========================================

    current_stage = "Outline Design"
    next_gate = "Submission of Outline Design Pack"

    insight = (
        f"The programme is currently "
        f"{variance_days} days behind baseline. "
        f"{outstanding} activities remain incomplete "
        f"and terminal float is {terminal_float} days."
    )

    if terminal_float <= 0:

        action = (
            "Recover critical path activities and "
            "prioritise remaining outline design deliverables."
        )

    elif variance_days > 14:

        action = (
            "Focus on delayed activities and develop "
            "recovery opportunities."
        )

    else:

        action = (
            "Maintain delivery momentum and continue "
            "progress monitoring."
        )

    # ========================================
    # DISPLAY
    # ========================================

    left_col, centre_col, right_col = st.columns([1.1, 1.4, 1.2])

    with left_col:

        st.markdown("##### PROJECT HEALTH")

        st.markdown(
            f"""
            <div style="
                color:{colour};
                font-size:42px;
                font-weight:700;
            ">
                {health}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            f"Forecast completion has slipped by "
            f"{variance_days} days against the "
            f"approved baseline."
        )

    with centre_col:

        st.markdown("##### INSIGHT")
        st.write(insight)

        st.markdown("##### RECOMMENDED ACTION")
        st.write(action)

    with right_col:

        st.markdown(
            f"""
            **Current Stage**  
            {current_stage}

            **Next Gate**  
            {next_gate}

            **Baseline Finish**  
            {baseline_finish.strftime("%d %b %Y")}

            **Forecast Finish**  
            {forecast_finish.strftime("%d %b %Y")}

            **Variance**  
            {variance_days} Days

            **Terminal Float**  
            {terminal_float} Days
            """
        )