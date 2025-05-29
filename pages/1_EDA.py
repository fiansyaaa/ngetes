# pages/1_EDA.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Data Eksploratif", page_icon="📊")

st.markdown("# 📊 Analisis Data Eksploratif (EDA)")
st.sidebar.header("EDA")
st.write(
    """Halaman ini menampilkan analisis dasar dari dataset Iris.
    Kita akan melihat data mentah, statistik deskriptif, dan beberapa visualisasi."""
)

# Fungsi untuk memuat data (menggunakan cache agar lebih cepat)
@st.cache_data
def load_data(path_data):
    try:
        df = pd.read_csv(path_data)
        return df
    except FileNotFoundError:
        st.error(f"File dataset di '{path_data}' tidak ditemukan. Pastikan file ada.")
        return None

# Ganti 'data/iris.csv' dengan path dataset Anda jika berbeda
df_iris = load_data('data/iris.csv')

if df_iris is not None:
    st.subheader("Tampilan Sebagian Data Iris")
    st.dataframe(df_iris.head())

    st.subheader("Informasi Dasar Dataset")
    st.write(f"Jumlah Baris: {df_iris.shape[0]}")
    st.write(f"Jumlah Kolom: {df_iris.shape[1]}")

    st.subheader("Statistik Deskriptif")
    st.dataframe(df_iris.describe())

    st.subheader("Visualisasi Data")

    # 1. Distribusi Kelas/Spesies
    st.write("**Distribusi Spesies Bunga Iris**")
    fig_species, ax_species = plt.subplots()
    # sns.countplot(x='variety', data=df_iris, ax=ax_species, palette="viridis") # Palette alternatif
    if 'variety' in df_iris.columns:
        sns.countplot(x='variety', data=df_iris, ax=ax_species)
        ax_species.set_title("Jumlah Sampel per Spesies Iris")
        st.pyplot(fig_species)
    else:
        st.warning("Kolom 'variety' tidak ditemukan untuk plot distribusi spesies.")


    # 2. Scatter plot untuk melihat hubungan antar fitur (contoh)
    st.write("**Hubungan Antara Panjang dan Lebar Sepal (Scatter Plot)**")
    if {'sepal_length', 'sepal_width', 'variety'}.issubset(df_iris.columns):
        fig_scatter, ax_scatter = plt.subplots()
        sns.scatterplot(data=df_iris, x='sepal_length', y='sepal_width', hue='variety', ax=ax_scatter)
        ax_scatter.set_title("Panjang Sepal vs Lebar Sepal")
        st.pyplot(fig_scatter)
    else:
        st.warning("Kolom 'sepal_length', 'sepal_width', atau 'variety' tidak ditemukan untuk scatter plot.")


    # 3. Boxplot untuk melihat sebaran fitur per spesies
    st.write("**Sebaran Panjang Petal per Spesies (Box Plot)**")
    if {'petal_length', 'variety'}.issubset(df_iris.columns):
        fig_boxplot, ax_boxplot = plt.subplots()
        sns.boxplot(x='variety', y='petal_length', data=df_iris, ax=ax_boxplot)
        ax_boxplot.set_title("Sebaran Panjang Petal untuk Setiap Spesies Iris")
        st.pyplot(fig_boxplot)
    else:
        st.warning("Kolom 'petal_length' atau 'variety' tidak ditemukan untuk box plot.")

else:
    st.warning("Dataset tidak dapat dimuat. Silakan periksa path dan file dataset Anda.")
