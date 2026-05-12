import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# ======================================================
# ตั้งค่าหน้าเว็บ
# ======================================================

st.set_page_config(
    page_title="AI Cafeteria Monitoring",
    layout="wide"
)

# ======================================================
# โหลดโลโก้
# ======================================================

logo = Image.open("logo.png")

# ======================================================
# Header
# ======================================================

col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo, width=120)

with col2:
    st.title("🍽️ AI Cafeteria Monitoring System")
    st.write("AI-based people counting dashboard")

# ======================================================
# อ่านข้อมูล CSV
# ======================================================

df = pd.read_csv("people_data.csv")

# ======================================================
# ลบคอลัมน์เวลา
# ======================================================

if "time" in df.columns:
    df_display = df.drop(columns=["time"])
else:
    df_display = df.copy()

# ======================================================
# ดึงข้อมูลล่าสุด
# ======================================================

latest = df.iloc[-1]

people_in = latest["people_in"]
people_out = latest["people_out"]

# ======================================================
# Dashboard
# ======================================================

st.write("## 📊 Dashboard")

col1, col2 = st.columns(2)

col1.metric(
    "People In",
    people_in
)

col2.metric(
    "People Out",
    people_out
)

# ======================================================
# กราฟเส้น
# ======================================================

st.write("## 📈 People Detection Graph")

fig = px.line(
    df_display,
    y=["people_in", "people_out"],
    markers=True,
    title="People In / Out"
)

fig.update_layout(
    xaxis_title="Detection Sequence",
    yaxis_title="People Count",
    template="plotly_white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================================================
# กราฟแท่ง
# ======================================================

st.write("## 📊 People In vs People Out")

fig_bar = px.bar(
    df_display,
    y=["people_in", "people_out"],
    barmode="group",
    title="People Detection Comparison"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# ======================================================
# ตารางข้อมูล
# ======================================================

st.write("## 📋 Data Table")

st.dataframe(
    df_display,
    use_container_width=True
)

# ======================================================
# Footer
# ======================================================

st.write("---")
st.write("Developed using YOLO + Streamlit")
