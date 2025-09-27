import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(layout="wide")

html_path = pathlib.Path("genoscene.html")

if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()

    auto_resize = f"""
    <script>
    function resize() {{
        var ifr = window.frameElement;
        if (ifr) {{
            ifr.style.height = document.body.scrollHeight + "px";
        }}
    }}
    window.onload = resize;
    window.onresize = resize;
    </script>
    {html_code}
    """

    components.html(auto_resize, height=0, scrolling=False)
else:
    st.error("❌ index.html مش موجود")
