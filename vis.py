import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My Project", layout="wide")

st.title("🚀 مشروع MARYAM على Streamlit")

st.sidebar.header("القائمة")

page = st.sidebar.selectbox("اختار صفحة:", ["الرئيسية", "تحميل بيانات", "تحليل"])

if page == "الرئيسية":
    st.write("أهلا بيكِ في المشروع 🌸")

elif page == "تحميل بيانات":
    uploaded_file = st.file_uploader("ارفع ملف CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

elif page == "تحليل":
    st.write("هنا ممكن نعرض أي شغل تحليلي أو رسومات")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    st.line_chart({"sin(x)": y})
