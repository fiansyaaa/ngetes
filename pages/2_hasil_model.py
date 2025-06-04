import streamlit as st
import pandas as pd

st.set_page_config(page_title="Prediksi Kematangan Alpukat", layout="wide")

st.title("🧠 Prediksi Kematangan Alpukat")

# Upload file CSV
uploaded_file = st.file_uploader("Upload dataset CSV kamu", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Rename kolom supaya sesuai dengan format yang dibutuhkan model
    df = df.rename(columns={
        'berat_buah': 'Berat',
        'warna_buah': 'Warna',
        'kekerasan_buah': 'Kekerasan',
        'kematangan': 'Ripeness'
    })

    # Cek apakah semua kolom yang dibutuhkan tersedia
    required_columns = ['Berat', 'Warna', 'Kekerasan', 'Ripeness']
    if all(col in df.columns for col in required_columns):
        st.success("Dataset berhasil dimuat! Menampilkan data:")
        st.dataframe(df)

        # Kode prediksi atau visualisasi bisa dilanjutkan di sini...
        # Contoh placeholder:
        st.write("✅ Data siap digunakan untuk prediksi model!")
    else:
        st.error(f"Dataset harus memiliki kolom: {required_columns}")
else:
    st.info("Silakan upload file CSV terlebih dahulu.")
