import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="GenoScene", layout="wide")

st.title("GenoScene Web App")

# تحديد مكان ملف HTML
base_path = os.path.dirname(__file__)
html_file = os.path.join(base_path, "genoscene.html")

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_code = f.read()

    # تعديل الروابط لتشير لمجلد static
    html_code = html_code.replace("css/", "static/css/")
    html_code = html_code.replace("js/", "static/js/")
    html_code = html_code.replace("face_images/", "static/face_images/")

    # عرض الموقع
    components.html(html_code, height=1000, scrolling=True)
else:
    st.error("⚠️ ملف genoscene.html غير موجود")
