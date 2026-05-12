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

logo = Image.open(logo.png")

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
# ดึงข้อมูลล่าสุด
# ======================================================

latest = df.iloc[-1]

people_in = latest["people_in"]
people_out = latest["people_out"]
current_people = latest["current_people"]

# ======================================================
# Dashboard Metrics
# ======================================================

st.write("## 📊 Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "People Entered",
    people_in
)

col2.metric(
    "People Exited",
    people_out
)

col3.metric(
    "Current Occupancy",
    current_people
)

# ======================================================
# กราฟ
# ======================================================

st.write("## 📈 People Count Trend")

fig = px.line(
    df,
    y="current_people",
    markers=True,
    title="Current People Trend"
)

fig.update_layout(
    xaxis_title="Detection Sequence",
    yaxis_title="People Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================================================
# ตารางข้อมูล
# ======================================================

st.write("## 📋 Data Table")

st.dataframe(
    df,
    use_container_width=True
)

# ======================================================
# Footer
# ======================================================

st.write("---")
st.write("Developed using YOLO + Streamlit")
