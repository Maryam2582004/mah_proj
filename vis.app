import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="GenoScene", layout="wide")

st.title("GenoScene Web App")

# تحميل كود HTML
html_file = "genoscene.html"

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_code = f.read()

    # نعدل روابط CSS و JS لو محتاج
    html_code = html_code.replace('href="css/', 'href="./css/')
    html_code = html_code.replace('src="js/', 'src="./js/')

    # نعرضه
    components.html(html_code, height=900, scrolling=True)
else:
    st.error(f"⚠️ ملف {html_file} مش موجود في المشروع")
