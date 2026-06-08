import streamlit as st
import edge_tts
import asyncio
st.title("app_sound")
text = st.text_area("اكتب النص")
lang = st.selectbox("choose a lang",["عربي","إنجليزي"])
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
voice_label = st.selectbox("Choose Voice",list(VOICES[lang].keys()))
voice_id = VOICES[lang][voice_label]  
async def genaret_audio(text,voice):
    Communicate = edge_tts.Communicate(text= text,voice= voice)
    audio_chunk = []
    async for chunk in communicate.stream():
         if chunk ["type"]=="audio":
             audio_chunk.append(chunk["date"])
         return b"".join(audio_chunk)
if st.button("Play"):
    if text:
        audio_bytes = asyncio.run(generate_audio(text,voice_id))
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("اكتب كلام اكتر")
             
    
