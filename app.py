import streamlit as st
import edge_tts
import asyncio
st.title("textovoice")
text = st.text_area("اكتب النص")
lang = st.selectbox("choose language",["عربي","انجلزي"])
