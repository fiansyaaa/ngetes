import streamlit as st

st.set_page_config(page_title="Prediksi Alpukat", layout="wide")

st.title("🥑 Aplikasi Prediksi Kematangan Alpukat")
st.write("""
Selamat datang! Aplikasi ini digunakan untuk menganalisis dan memprediksi tingkat kematangan alpukat berdasarkan data fisik seperti berat, warna, dan kekerasan.
Gunakan menu di samping untuk:
- Melihat data alpukat
- Memprediksi tingkat kematangan (ripeness)
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Avocado_with_cross_section_edit.jpg/640px-Avocado_with_cross_section_edit.jpg", caption="Contoh Alpukat")
