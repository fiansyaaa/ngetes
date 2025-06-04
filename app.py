import streamlit as st

st.set_page_config(page_title="Aplikasi Gempa", layout="wide")

st.title("📊 Aplikasi Pemantauan dan Prediksi Gempa Bumi")
st.write("""
Selamat datang di aplikasi Streamlit untuk analisis dan prediksi gempa bumi di Indonesia.
Gunakan menu di samping untuk melihat data gempa dan mencoba fitur prediksi.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Indonesia_earthquake_map.jpg/640px-Indonesia_earthquake_map.jpg", caption="Peta Gempa Indonesia")
