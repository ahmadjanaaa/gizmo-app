import streamlit as st
from PIL import Image

st.set_page_config(page_title="Gizmo Quiz", layout="centered")

st.title("📸 Gizmo Style Test Maker")

# 1. Фото жүктеу / Түсіру
uploaded_file = st.file_uploader("Сурет таңдаңыз немесе түсіріңіз", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Жүктелген сурет", use_container_width=True)
    
    if st.button("⚡ Тест құрастыру"):
        st.success("Сурет қабылданды! AI/OCR өңдеуді қосатын кезде айтыңыз.")

# 2. Флеш-карталар бөлімі
st.divider()
st.subheader("🎴 Флеш-карталар")
with st.expander("📌 Термин 1 (Басып ашыңыз)"):
    st.write("Бұл жерде анықтамасы немесе жауабы болады.")

# 3. Тест бөлімі
st.divider()
st.subheader("📝 Тест")
st.write("1. Мысал сұрақ?")
option = st.radio("Жауапты таңдаңыз:", ["А нұсқасы", "Б нұсқасы", "В нұсқасы"])
if st.button("Тексеру"):
    st.info("Жауап қабылданды.")
