# app.py
import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd

st.set_page_config(
    page_title="Dashboard Data Mining Iris",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 Dashboard Data Mining: Dataset Iris")

st.write("""
Selamat datang di dashboard interaktif ini!
Dashboard ini menjelajahi dataset Iris dan melakukan prediksi spesies berdasarkan fitur-fiturnya.
""")

st.subheader("Tentang Dataset Iris")
st.markdown("""
Dataset Iris adalah dataset klasik dalam machine learning dan statistik. Dataset ini berisi:
- 150 sampel bunga dari 3 spesies: *Iris setosa*, *Iris versicolor*, dan *Iris virginica*
- 4 fitur utama:
  - Panjang Sepal (cm)
  - Lebar Sepal (cm)
  - Panjang Petal (cm)
  - Lebar Petal (cm)
""")

# Tampilkan dataset
iris = load_iris(as_frame=True)
df = iris.frame
df["target_name"] = df["target"].apply(lambda x: iris.target_names[x])

st.subheader("📊 Dataset Lengkap Iris")
st.dataframe(df)
