# App.py
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Data Mining Iris",
    page_icon="🌸", # Bisa ganti emoji atau path ke file gambar
    layout="wide" # 'centered' atau 'wide'
)

st.title("🌸 Dashboard Data Mining: Dataset Iris")
st.write("""
Selamat datang di dashboard interaktif ini!
Dashboard ini dibuat untuk menjelajahi dataset Iris, melihat performa model,
dan melakukan prediksi spesies Iris berdasarkan fitur-fiturnya.
Pilih halaman dari sidebar di kiri.
""")

st.sidebar.success("Pilih halaman di atas.")

st.subheader("Tentang Dataset Iris")
st.markdown("""
Dataset Iris adalah dataset klasik dalam machine learning dan statistik.
Ini berisi 150 sampel dari tiga spesies bunga Iris (Iris setosa, Iris versicolor, dan Iris virginica).
Untuk setiap sampel, empat fitur diukur (dalam sentimeter):
- Panjang Sepal (`sepal_length`)
- Lebar Sepal (`sepal_width`)
- Panjang Petal (`petal_length`)
- Lebar Petal (`petal_width`)
""")

# Anda bisa menambahkan gambar bunga Iris di sini jika mau
# st.image("path/ke/gambar_iris.jpg")

st.info("Proyek ini menggunakan Streamlit untuk antarmuka pengguna dan Scikit-learn untuk model machine learning.")
