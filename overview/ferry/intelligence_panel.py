import streamlit as st
import pandas as pd


def render(df):

    df = df.copy()

    df.columns = df.columns.str.strip()

    latest_date = pd.to_datetime(
        df["SnapshotDate"]
    ).max()

    latest = df[
        df["SnapshotDate"] == latest_date
    ].copy()

    latest["Finish"] = pd.to_datetime(
        latest["Finish"],
        errors="coerce"
    )

    dates = sorted(
        pd.to_datetime(
            df["SnapshotDate"]
        ).dropna().unique()
    )

    baseline_date = dates[0]

    baseline = df[
        df["SnapshotDate"] == baseline_date
    ].copy()

    baseline["Finish"] = pd.to_datetime(
        baseline["Finish"],
        errors="coerce"
    )

    baseline_finish = baseline["Finish"].max()
    forecast_finish = latest["Finish"].max()

    variance = (
        forecast_finish -
        baseline_finish
    ).days

    total_float = pd.to_numeric(
        latest["Total Float"],
        errors="coerce"
    ).min()

    if variance <= 7:

        health = "GREEN"
        colour = "#22C55E"
        icon = "🟢"

    elif variance <= 21:

        health = "AMBER"
        colour = "#F59E0B"
        icon = "🟠"

    else:

        health = "RED"
        colour = "#EF4444"
        icon = "🔴"

    overdue = latest[
        latest["Finish"] <
        pd.Timestamp.today()
    ]

    insight = (
        f"The programme is currently "
        f"{variance} days from the "
        f"baseline forecast. "
        f"{len(overdue)} activities are overdue."
    )

    if variance > 14:

        action = (
            "Review critical path activities "
            "and expedite outstanding "
            "deliverables."
        )

    else:

        action = (
            "Continue to monitor progress "
            "against the approved programme."
        )

    st.markdown(
        f"""
        <div class="dashboard-card">

            <div style="
                display:grid;
                grid-template-columns:
                1.2fr
                1.5fr
                1fr;
                gap:30px;
            ">

                <div>

                    <div style="
                        color:#CBD5E1;
                        font-size:14px;
                        margin-bottom:12px;
                    ">
                        PROJECT HEALTH
                    </div>

                    <div style="
                        font-size:42px;
                        font-weight:700;
                        color:{colour};
                    ">
                        {icon} {health}
                    </div>

                    <div style="
                        margin-top:12px;
                        color:#CBD5E1;
                        line-height:1.6;
                    ">
                        Forecast completion has moved
                        by {variance} days against
                        the approved baseline.
                    </div>

                </div>

                <div>

                    <div style="
                        color:#60A5FA;
                        font-weight:600;
                        margin-bottom:10px;
                    ">
                        INSIGHT
                    </div>

                    <div style="
                        color:white;
                        line-height:1.7;
                    ">
                        {insight}
                    </div>

                    <div style="
                        color:#60A5FA;
                        font-weight:600;
                        margin-top:20px;
                        margin-bottom:10px;
                    ">
                        RECOMMENDED ACTION
                    </div>

                    <div style="
                        color:white;
                        line-height:1.7;
                    ">
                        {action}
                    </div>

                </div>

                <div>

                    <table style="
                        width:100%;
                        color:white;
                    ">

                        <tr>
                            <td>Current Stage</td>
                            <td style="text-align:right;">
                                Outline Design
                            </td>
                        </tr>

                        <tr>
                            <td>Next Gate</td>
                            <td style="text-align:right;">
                                Scope Freeze
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
                                {variance} Days
                            </td>
                        </tr>

                        <tr>
                            <td>Terminal Float</td>
                            <td style="text-align:right;">
                                {int(total_float)} Days
                            </td>
                        </tr>

                    </table>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )