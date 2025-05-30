# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Data Mining Iris",
    page_icon="🌸",
    layout="wide"
)

# Judul utama
st.title("🌸 Dashboard Data Mining: Dataset Iris")
st.write("""
Selamat datang di dashboard interaktif ini!
Dashboard ini dibuat untuk menjelajahi dataset Iris, melihat performa model,
dan melakukan prediksi spesies Iris berdasarkan fitur-fiturnya.
Pilih halaman dari sidebar di kiri.
""")

st.sidebar.success("Pilih halaman di atas.")

# Tentang dataset
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

st.info("Proyek ini menggunakan Streamlit untuk antarmuka pengguna dan Scikit-learn untuk model machine learning.")

# ======================
# Upload File CSV
# ======================
st.subheader("📁 Unggah Dataset CSV (Opsional)")

uploaded_file = st.file_uploader("Unggah file CSV Anda", type=["csv"])
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File berhasil dimuat.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        st.stop()
else:
    # Gunakan dataset Iris default
    iris = load_iris(as_frame=True)
    df = iris.frame

# ======================
# Cuplikan Data
# ======================
st.subheader("🧾 Cuplikan Dataset")
st.dataframe(df.head())

# ======================
# Visualisasi Histogram
# ======================
if all(col in df.columns for col in ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]):
    st.subheader("📊 Visualisasi Histogram Fitur")
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    sns.histplot(df["sepal length (cm)"], kde=True, ax=ax[0, 0], color="skyblue")
    ax[0, 0].set_title("Panjang Sepal")

    sns.histplot(df["sepal width (cm)"], kde=True, ax=ax[0, 1], color="salmon")
    ax[0, 1].set_title("Lebar Sepal")

    sns.histplot(df["petal length (cm)"], kde=True, ax=ax[1, 0], color="lightgreen")
    ax[1, 0].set_title("Panjang Petal")

    sns.histplot(df["petal width (cm)"], kde=True, ax=ax[1, 1], color="plum")
    ax[1, 1].set_title("Lebar Petal")

    st.pyplot(fig)

# ======================
# Prediksi Spesies
# ======================
st.subheader("🔍 Prediksi Spesies Iris")

sepal_length = st.slider("Panjang Sepal (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Lebar Sepal (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Panjang Petal (cm)", 1.0, 7.0, 4.35)
petal_width = st.slider("Lebar Petal (cm)", 0.1, 2.5, 1.3)

# Model hanya bisa jalan jika pakai struktur dataset asli
try:
    model = RandomForestClassifier()
    model.fit(df.iloc[:, :4], df.iloc[:, -1])
    pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    # Cek apakah nama target tersedia
    if uploaded_file is None:
        pred_species = iris.target_names[pred[0]]
    else:
        pred_species = str(pred[0])

    st.success(f"Prediksi spesies bunga Iris: **{pred_species}**")
except Exception as e:
    st.error(f"Gagal melakukan prediksi: {e}")
