import streamlit as st
import requests
import time
from datetime import datetime
import winsound
st.set_page_config(page_title="Prayer Alarm App", page_icon="🕌", layout="centered")
# Get prayer times
url = "https://api.aladhan.com/v1/timingsByCity?city=Dubai&country=UAE&method=2"
response = requests.get(url)

data = response.json()
timings = data['data']['timings']

important_prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

st.title("Prayer Alarm App")

for prayer in important_prayers:
    st.write(f"{prayer}: {timings[prayer]}")

# Alarm checker
while True:
    current_time = datetime.now().strftime("%H:%M")

    for prayer in important_prayers:
        if current_time == timings[prayer][:5]:

            st.warning(
                f"It's {prayer} time! Remember to read Ayatul Kursi 🤲"
            )

            winsound.beep(1000, 1000)

            time.sleep(60)

    time.sleep(1)