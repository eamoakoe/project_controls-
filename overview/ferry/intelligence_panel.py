import streamlit as st
import pandas as pd


def render(df):

    df = df.copy()

    df.columns = df.columns.str.strip()

    latest_date = pd.to_datetime(
        df["SnapshotDate"]
    ).max()

    latest_df = df[
        df["SnapshotDate"] == latest_date
    ].copy()

    latest_df["Finish"] = pd.to_datetime(
        latest_df["Finish"],
        errors="coerce"
    )

    dates = sorted(
        pd.to_datetime(
            df["SnapshotDate"]
        ).dropna().unique()
    )

    baseline_date = dates[0]

    baseline_df = df[
        df["SnapshotDate"] == baseline_date
    ].copy()

    baseline_df["Finish"] = pd.to_datetime(
        baseline_df["Finish"],
        errors="coerce"
    )

    baseline_finish = baseline_df["Finish"].max()
    forecast_finish = latest_df["Finish"].max()

    variance = (
        forecast_finish -
        baseline_finish
    ).days

    if variance <= 7:
        health = "GREEN"
        colour = "#22c55e"

    elif variance <= 21:
        health = "AMBER"
        colour = "#f59e0b"

    else:
        health = "RED"
        colour = "#ef4444"

    total_float = pd.to_numeric(
        latest_df["Total Float"],
        errors="coerce"
    ).min()

    st.markdown(
        f"""
        <div style="
            background:#0b1730;
            border:1px solid #1e3a5f;
            border-radius:16px;
            padding:24px;
            margin-bottom:20px;
        ">
            <div style="
                display:flex;
                justify-content:space-between;
                gap:30px;
            ">

                <div style="flex:1;">

                    <div style="
                        color:#94a3b8;
                        font-size:12px;
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
                        margin-top:10px;
                    ">
                        Forecast completion has moved
                        <strong>{variance} days</strong>
                        against the approved baseline.
                    </div>

                </div>

                <div style="
                    flex:1;
                    border-left:1px solid #1e3a5f;
                    padding-left:24px;
                ">

                    <div style="
                        color:#60a5fa;
                        font-size:12px;
                        margin-bottom:10px;
                    ">
                        INSIGHT
                    </div>

                    <div style="
                        color:white;
                        line-height:1.6;
                    ">
                        Current programme forecast indicates
                        a variance of {variance} days against
                        the original baseline plan.
                    </div>

                    <div style="
                        color:#60a5fa;
                        margin-top:20px;
                        font-size:12px;
                    ">
                        RECOMMENDED ACTION
                    </div>

                    <div style="
                        color:white;
                        line-height:1.6;
                    ">
                        Review activities driving programme
                        completion and validate critical path
                        deliverables.
                    </div>

                </div>

                <div style="
                    flex:1;
                    border-left:1px solid #1e3a5f;
                    padding-left:24px;
                ">

                    <table style="
                        width:100%;
                        color:white;
                    ">
                        <tr>
                            <td>Current Stage</td>
                            <td><b>Outline Design</b></td>
                        </tr>

                        <tr>
                            <td>Next Gate</td>
                            <td><b>Scope Freeze</b></td>
                        </tr>

                        <tr>
                            <td>Baseline Finish</td>
                            <td>
                                <b>
                                    {baseline_finish.strftime('%d %b %Y')}
                                </b>
                            </td>
                        </tr>

                        <tr>
                            <td>Forecast Finish</td>
                            <td>
                                <b>
                                    {forecast_finish.strftime('%d %b %Y')}
                                </b>
                            </td>
                        </tr>

                        <tr>
                            <td>Variance</td>
                            <td style="color:{colour};">
                                <b>{variance} Days</b>
                            </td>
                        </tr>

                        <tr>
                            <td>Terminal Float</td>
                            <td>
                                <b>{int(total_float)} Days</b>
                            </td>
                        </tr>

                    </table>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )