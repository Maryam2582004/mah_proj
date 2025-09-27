import streamlit as st

with open("genoscene.html") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)
