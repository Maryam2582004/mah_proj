  import streamlit as st
  import pandas as pd
  import os
  from phenotypicprediction import predict_phenotypes  # استيراد الدالة الرئيسية (عدلي حسب الكود الحقيقي)
  # استيراد باقي الوظائف زي plotphenodc إلخ

  st.title("GenoScene - نظام التنبؤ بالسمات الوراثية")
  st.write("مرحباً! ارفعي ملف CSV لبيانات SNP للتنبؤ بالسمات.")

  # إدخال معرف العينة
  sample_id = st.text_input("أدخلي معرف العينة (Sample ID):")

  # رفع ملف CSV
  uploaded_file = st.file_uploader("ارفعي ملف CSV لبيانات SNP", type="csv")

  if uploaded_file is not None and sample_id:
      # حفظ الملف مؤقتاً
      df = pd.read_csv(uploaded_file)
      csv_path = f"{sample_id}_temp.csv"
      df.to_csv(csv_path, index=False)

      if st.button("تنبؤ بالسمات (Predict Phenotypes)"):
          with st.spinner("جاري التنبؤ..."):
              # استدعاء الدالة الرئيسية (عدلي الاسم حسب phenotypicprediction.py)
              results = predict_phenotypes(sample_id, csv_path)
              st.success("تم التنبؤ بنجاح!")
              st.dataframe(results)  # عرض النتائج في جدول

              # عرض الرسوم البيانية
              if os.path.exists(f"{sample_id}_DC_eye.jpg"):
                  st.image(f"{sample_id}_DC_eye.jpg", caption="لون العينين")
              if os.path.exists(f"{sample_id}_DC_hair.jpg"):
                  st.image(f"{sample_id}_DC_hair.jpg", caption="لون الشعر")
              if os.path.exists(f"{sample_id}_DC_skin.jpg"):
                  st.image(f"{sample_id}_DC_skin.jpg", caption="لون البشرة")

              # توليد الوجه
              if st.button("توليد الوجه (Generate Face)"):
                  # كود لتحميل صورة الوجه من face_images/ بناءً على النتائج
                  # مثال: افترضي النتائج تحدد hair='black', eye='blue', skin='dark'
                  face_path = "face_images/face_black_blue_dark.png"  # عدلي حسب النتائج
                  if os.path.exists(face_path):
                      st.image(face_path, caption="صورة الوجه المُولدة")
                  else:
                      st.write("استخدام SVG احتياطي")  # نظام الاحتياطي

      # حذف الملف المؤقت
      if os.path.exists(csv_path):
          os.remove(csv_path)

  st.info("ملاحظة: تأكدي من تحضير البيانات أولاً باستخدام vcftocsv.py أو mpileuptocsv.py إذا كان الملف VCF أو mpileup.")
  
