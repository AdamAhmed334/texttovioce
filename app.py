import streamlit as st
import edge_tts
import asyncio
st.title("textovoice")
text = st.text_area("اكتب النص")
lang = st.selectbox("choose language",["عربي","انجلزي"])
VOICES = {
    "عربي": {
        
        " زارية (امرأة - السعودية)": "ar-SA-ZariyahNeural",
        " شاكر (رجل - مصر)":         "ar-EG-ShakirNeural",
        " سلمى (امرأة - مصر)":       "ar-EG-SalmaNeural",
    },
    "إنجليزي": {
        " غاي (رجل - أمريكا)":       "en-US-GuyNeural",
        " جيني (امرأة - أمريكا)":    "en-US-JennyNeural",
        " رايان (رجل - بريطانيا)":   "en-GB-RyanNeural",
        " ليبي (امرأة - بريطانيا)": "en-GB-LibbyNeural",
    },
}
lang = st.selectbox("choose lang voice",list(VOICES[lang].keys()))
