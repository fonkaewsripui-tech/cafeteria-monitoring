import streamlit as st
import pandas as pd

# =========================
# ตั้งค่าหน้าเว็บ
# =========================

st.set_page_config(
    page_title="AI Cafeteria Monitoring",
    layout="wide"
)

st.title("🍽️ AI Cafeteria Monitoring System")

# =========================
# อ่าน CSV
# =========================

df = pd.read_csv("people_data.csv")

# =========================
# ดึงข้อมูลล่าสุด
# =========================

latest = df.iloc[-1]

people_in = latest["people_in"]
people_out = latest["people_out"]
current_people = latest["current_people"]

# =========================
# Dashboard
# =========================

col1, col2, col3 = st.columns(3)

col1.metric("People In", people_in)
col2.metric("People Out", people_out)
col3.metric("Current People", current_people)

# =========================
# กราฟ
# =========================

st.subheader("📈 Current People Graph")

st.line_chart(df["current_people"])

# =========================
# ตารางข้อมูล
# =========================

st.subheader("📋 Data Table")

st.dataframe(df)