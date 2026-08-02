import streamlit as st


FRAMEWORKS = {

    "UU DD&B Framework": [
        "Ferry PS",
        "Flass Lane",
        "Tally Ho",
        "Rossall Outfall",
        "Eccleston Bridge"
    ],

    "UU Enterprise Framework": [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]
}


def render_sidebar():

    with st.sidebar:

        # ==================================================
        # LOGO
        # ==================================================

        st.image(
            "assets/logo.png",
            width=180
        )

        st.markdown("### FRAMEWORK")

        framework = st.radio(
            label="",
            options=list(FRAMEWORKS.keys())
        )

        st.markdown("---")

        st.markdown("### ASSET")

        asset = st.radio(
            label="",
            options=FRAMEWORKS[framework]
        )

        st.markdown("---")

        st.markdown("### NAVIGATION")

        page = st.radio(
            label="",
            options=[
                "Overview",
                "Framework Roadmap",
                "Delivery & Programme",
                "Communications",
                "Documents",
                "Reports",
                "Settings"
            ]
        )

    return framework, asset, page