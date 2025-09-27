import streamlit as st
import pandas as pd
import os

# ✅ استيراد الدوال من ملفات المشروع
from src.phenotypicprediction import predict_phenotypes  # عدلي لو مكان الملف مختلف
from src.plotphenodc import plot_phenotypes  # مثال، لو عندك دالة للرسوم

st.set_page_config(page_title="GenoScene", layout="wide")

st.title("🧬 GenoScene - نظام التنبؤ بالسمات الوراثية")
st.write("مرحباً! ارفعي ملف CSV لبيانات **SNP** للتنبؤ بالسمات.")

# إدخال Sample ID
sample_id = st.text_input("أدخلي معرف العينة (Sample ID):")

# رفع ملف CSV
uploaded_file = st.file_uploader("📂 ارفعي ملف CSV لبيانات SNP", type="csv")

if uploaded_file is not None and sample_id:
    # حفظ نسخة مؤقتة من CSV
    df = pd.read_csv(uploaded_file)
    csv_path = f"{sample_id}_temp.csv"
    df.to_csv(csv_path, index=False)

    if st.button("🔮 تنبؤ بالسمات (Predict Phenotypes)"):
        with st.spinner("⏳ جاري التنبؤ..."):
            try:
                # ✅ استدعاء دالة التنبؤ من phenotypicprediction.py
                results = predict_phenotypes(sample_id, csv_path)

                st.success("✅ تم التنبؤ بنجاح!")
                st.subheader("نتائج التنبؤ")
                st.dataframe(results)

                # ✅ عرض الرسوم من plotphenodc.py (لو متولدة صور)
                st.subheader("📊 الرسوم البيانية للسمات")
                for trait in ["eye", "hair", "skin"]:  # غيّري القائمة حسب السمات اللي عندك
                    img_path = f"{sample_id}_DC_{trait}.jpg"
                    if os.path.exists(img_path):
                        st.image(img_path, caption=f"Distribution of {trait}")

                # ✅ خيار توليد الوجه
                if st.button("🖼️ توليد الوجه (Generate Face)"):
                    face_path = f"face_images/{sample_id}_face.png"  # غيّري حسب نتائجك
                    if os.path.exists(face_path):
                        st.image(face_path, caption="الصورة المُولدة")
                    else:
                        st.warning("⚠️ لم يتم العثور على صورة الوجه المُولدة.")
            except Exception as e:
                st.error(f"❌ حدث خطأ: {e}")

    # تنظيف الملف المؤقت
    if os.path.exists(csv_path):
        os.remove(csv_path)

st.info("ℹ️ ملاحظة: تأكدي من تجهيز البيانات أولاً باستخدام `vcftocsv.py` أو `mpileuptocsv.py`.")
