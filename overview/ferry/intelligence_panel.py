import streamlit as st
import pandas as pd


def render(df):

    if df is None or df.empty:
        st.warning("No programme data loaded.")
        return

    df = df.copy()
    df.columns = df.columns.astype(str).str.strip()

    required = [
        "Finish",
        "BL1 Finish",
        "Total Float",
        "Activity % Complete"
    ]

    missing = [c for c in required if c not in df.columns]

    if missing:
        st.error(
            f"Missing required columns: {', '.join(missing)}"
        )
        return

    # ==================================
    # DATA PREP
    # ==================================

    df["Finish"] = pd.to_datetime(
        df["Finish"],
        errors="coerce",
        dayfirst=True
    )

    df["BL1 Finish"] = pd.to_datetime(
        df["BL1 Finish"],
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

    # ==================================
    # KPI CALCS
    # ==================================

    baseline_finish = df["BL1 Finish"].max()

    forecast_finish = df["Finish"].max()

    variance_days = int(
        (forecast_finish - baseline_finish).days
    )

    terminal_float = int(
        df["Total Float"].min()
    )

    overdue = df[
        (
            df["Finish"] < pd.Timestamp.today()
        )
        &
        (
            df["Activity % Complete"] < 100
        )
    ]

    overdue_count = len(overdue)

    # ==================================
    # HEALTH
    # ==================================

    if variance_days <= 7:

        health = "GREEN"
        colour = "#22c55e"
        icon = "🟢"

    elif variance_days <= 28:

        health = "AMBER"
        colour = "#f59e0b"
        icon = "🟠"

    else:

        health = "RED"
        colour = "#ef4444"
        icon = "🔴"

    # ==================================
    # PROJECT INFO
    # ==================================

    current_stage = "Outline Design"
    next_gate = "Scope Freeze"

    insight = (
        f"Forecast completion has slipped by "
        f"{variance_days} days against the approved "
        f"baseline. {overdue_count} activities remain "
        f"outstanding within the current programme."
    )

    if terminal_float <= 0:

        action = (
            "Complete outstanding deliverables and "
            "recover critical path float."
        )

    elif variance_days > 14:

        action = (
            "Prioritise delayed activities and validate "
            "recovery opportunities."
        )

    else:

        action = (
            "Maintain progress momentum and continue "
            "monitoring delivery performance."
        )

    # ==================================
    # DISPLAY
    # ==================================

    st.markdown(
        f"""
        <div class="dashboard-card">

            <div style="
                display:grid;
                grid-template-columns:1.2fr 1.5fr 1fr;
                gap:30px;
                align-items:start;
            ">

                <div>

                    <div style="
                        color:#94a3b8;
                        font-size:13px;
                        font-weight:600;
                        margin-bottom:10px;
                    ">
                        PROJECT HEALTH
                    </div>

                    <div style="
                        font-size:42px;
                        font-weight:700;
                        color:{colour};
                    ">
                        {health}
                    </div>

                    <div style="
                        color:white;
                        margin-top:12px;
                        line-height:1.7;
                    ">
                        Forecast completion has slipped
                        by <strong>{variance_days} days</strong>
                        against the approved baseline.
                    </div>

                </div>

                <div style="
                    border-left:1px solid #173d73;
                    padding-left:24px;
                ">

                    <div style="
                        color:#60a5fa;
                        font-weight:600;
                        margin-bottom:8px;
                    ">
                        INSIGHT
                    </div>

                    <div style="
                        color:white;
                        line-height:1.8;
                    ">
                        {insight}
                    </div>

                    <div style="
                        color:#60a5fa;
                        font-weight:600;
                        margin-top:20px;
                        margin-bottom:8px;
                    ">
                        RECOMMENDED ACTION
                    </div>

                    <div style="
                        color:white;
                        line-height:1.8;
                    ">
                        {action}
                    </div>

                </div>

                <div style="
                    border-left:1px solid #173d73;
                    padding-left:24px;
                ">

                    <table style="
                        width:100%;
                        color:white;
                    ">

                        <tr>
                            <td>Current Stage</td>
                            <td style="text-align:right;">
                                {current_stage}
                            </td>
                        </tr>

                        <tr>
                            <td>Next Gate</td>
                            <td style="text-align:right;">
                                {next_gate}
                            </td>
                        </tr>

                        <tr>
                            <td>Baseline Finish</td>
                            <td style="text-align:right;">
                                {baseline_finish.strftime('%d %b %Y')}
                            </td>
                        </tr>

                        <tr>
                            <td>Forecast Finish</td>
                            <td style="text-align:right;">
                                {forecast_finish.strftime('%d %b %Y')}
                            </td>
                        </tr>

                        <tr>
                            <td>Variance</td>
                            <td style="
                                text-align:right;
                                color:{colour};
                                font-weight:700;
                            ">
                                {variance_days} Days
                            </td>
                        </tr>

                        <tr>
                            <td>Terminal Float</td>
                            <td style="text-align:right;">
                                {terminal_float} Days
                            </td>
                        </tr>

                    </table>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )