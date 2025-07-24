
import streamlit as st
from PIL import Image

# Load banner and logo
st.set_page_config(page_title="Yamaima", layout="wide")

banner = Image.open("assets/banner.jpg")
logo = Image.open("assets/logo.png")

st.image(banner, use_column_width=True)
st.markdown(
    f'<div style="position:absolute; top:25px; left:50%; transform:translateX(-50%);">'
    f'<img src="assets/logo.png" width="80"></div>',
    unsafe_allow_html=True
)

# Language selection
language = st.selectbox("🌐 Language", ["English", "日本語"])
st.session_state.language = language

# Chat intro
st.markdown("### 🧭 Welcome to Yamaima — Your Japan Hiking Concierge")
st.markdown("Ask me to help you plan your hike!")

# Placeholder for chat UI
with st.chat_message("assistant", avatar="assets/logo.png"):
    st.markdown("Hi! Where in Japan would you like to hike?")
