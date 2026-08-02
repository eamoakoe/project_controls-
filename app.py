import streamlit as st
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="UU Project Controls Hub",
    layout="wide"
)

framework, asset, page = render_sidebar()

st.title("UU Project Controls Hub")

st.write(f"Framework: {framework}")
st.write(f"Asset: {asset}")
st.write(f"Page: {page}")