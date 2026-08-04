import streamlit as st
import pandas as pd


def render(df):

    df = df.copy()

    df.columns = df.columns.astype(str).str.strip()

    latest_date = pd.to_datetime(
        df["SnapshotDate"],
        errors="coerce"
    ).max()

    latest_df = df[
        pd.to_datetime(
            df["SnapshotDate"],
            errors="coerce"
        )
        == latest_date
    ].copy()

    latest_df["Finish"] = pd.to_datetime(
        latest_df["Finish"],
        errors="coerce"
    )

    latest_df["Total Float"] = pd.to_numeric(
        latest_df["Total Float"],
        errors="coerce"
    )

    latest_df["Activity % Complete"] = (
        latest_df["Activity % Complete"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    latest_df["Activity % Complete"] = pd.to_numeric(
        latest_df["Activity % Complete"],
        errors="coerce"
    ).fillna(0)

    snapshot_dates = sorted(
        pd.to_datetime(
            df["SnapshotDate"],
            errors="coerce"
        )
        .dropna()
        .unique()
    )

    baseline_date = snapshot_dates[0]

    baseline_df = df[
        pd.to_datetime(
            df["SnapshotDate"],
            errors="coerce"
        )
        == baseline_date
    ].copy()

    baseline_df["Finish"] = pd.to_datetime(
        baseline_df["Finish"],
        errors="coerce"
    )

    baseline_finish = baseline_df["Finish"].max()
    forecast_finish = latest_df["Finish"].max()

    variance_days = int(
        (
            forecast_finish -
            baseline_finish
        ).days
    )

    terminal_float = int(
        latest_df["Total Float"].min()
    )

    overdue = latest_df[
        (
            latest_df["Finish"]
            < pd.Timestamp.today()
        )
        &
        (
            latest_df["Activity % Complete"]
            < 100
        )
    ]

    overdue_count = len(overdue)

    if variance_days <= 7:

        health = "GREEN"
        colour = "#22c55e"
        icon = "🟢"

    elif variance_days <= 21:

        health = "AMBER"
        colour = "#f59e0b"
        icon = "🟠"

    else:

        health = "RED"
        colour = "#ef4444"
        icon = "🔴"

    insight = (
        f"{overdue_count} overdue activities "
        f"identified in the current programme. "
        f"The forecast completion date currently "
        f"varies by {variance_days} days versus "
        f"the baseline."
    )

    if terminal_float <= 0:

        action = (
            "Review critical path activities and "
            "recover float on near-term deliverables."
        )

    elif variance_days > 14:

        action = (
            "Prioritise delayed deliverables and "
            "validate recovery opportunities."
        )

    else:

        action = (
            "Maintain current delivery trajectory "
            "and continue progress monitoring."
        )

    st.markdown(
        f"""
        <div class="dashboard-card">

            <div style="
                display:grid;
                grid-template-columns:
                1.1fr 1.5fr 1fr;
                gap:30px;
                align-items:start;
            ">

                <!-- LEFT -->

                <div>

                    <div style="
                        color:#94a3b8;
                        font-size:13px;
                        font-weight:600;
                        letter-spacing:0.5px;
                        margin-bottom:10px;
                    ">
                        PROJECT HEALTH
                    </div>

                    <div style="
                        font-size:44px;
                        font-weight:700;
                        color:{colour};
                    ">
                        {icon} {health}
                    </div>

                    <div style="
                        color:#e2e8f0;
                        margin-top:14px;
                        line-height:1.7;
                    ">
                        Forecast completion has moved
                        by <strong>{variance_days} days</strong>
                        against the approved baseline.
                    </div>

                </div>

                <!-- CENTRE -->

                <div style="
                    border-left:1px solid #173d73;
                    padding-left:24px;
                ">

                    <div style="
                        color:#60a5fa;
                        font-size:14px;
                        font-weight:600;
                        margin-bottom:10px;
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
                        font-size:14px;
                        font-weight:600;
                        margin-top:24px;
                        margin-bottom:10px;
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

                <!-- RIGHT -->

                <div style="
                    border-left:1px solid #173d73;
                    padding-left:24px;
                ">

                    <table style="
                        width:100%;
                        color:white;
                    ">

                        <tr>
                            <td style="padding:8px 0;color:#94a3b8;">
                                Baseline Finish
                            </td>

                            <td style="
                                text-align:right;
                                font-weight:600;
                            ">
                                {baseline_finish.strftime('%d %b %Y')}
                            </td>
                        </tr>

                        <tr>
                            <td style="padding:8px 0;color:#94a3b8;">
                                Forecast Finish
                            </td>

                            <td style="
                                text-align:right;
                                font-weight:600;
                            ">
                                {forecast_finish.strftime('%d %b %Y')}
                            </td>
                        </tr>

                        <tr>
                            <td style="padding:8px 0;color:#94a3b8;">
                                Variance
                            </td>

                            <td style="
                                text-align:right;
                                font-weight:700;
                                color:{colour};
                            ">
                                {variance_days} Days
                            </td>
                        </tr>

                        <tr>
                            <td style="padding:8px 0;color:#94a3b8;">
                                Terminal Float
                            </td>

                            <td style="
                                text-align:right;
                                font-weight:600;
                            ">
                                {terminal_float} Days
                            </td>
                        </tr>

                        <tr>
                            <td style="padding:8px 0;color:#94a3b8;">
                                Overdue Activities
                            </td>

                            <td style="
                                text-align:right;
                                font-weight:600;
                            ">
                                {overdue_count}
                            </td>
                        </tr>

                    </table>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )