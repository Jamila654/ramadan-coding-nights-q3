#type: ignore
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


st.set_page_config(page_title="Time Zone Converter", page_icon=":clock:", layout="centered")

TIME_ZONES = [
    "UTC",
    "US/Eastern",
    "US/Central",
    "US/Mountain",
    "US/Pacific",
    "Europe/London",
    "Europe/Paris",
    "Asia/Karachi",
    "Asia/Shanghai",
    "Australia/Sydney",
    "Pacific/Auckland",
    "Africa/Johannesburg",
    "America/Caracas",
    "America/Santiago",
    "America/Buenos_Aires",
    "America/Lima",
    "America/Mexico_City",
    "America/Toronto",
    "America/Chicago",
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC","Asia/Karachi"])

st.subheader("Selected Time Zones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between Time Zones")
current_time = st.time_input("Enter the current time", datetime.now().time())
from_tz = st.selectbox("From Time Zone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Time Zone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time: {converted_time}")

st.write("---")
st.write("Made with :heart: by Jam")