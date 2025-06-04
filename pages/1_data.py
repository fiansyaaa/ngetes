import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Alpukat")

df = pd.read_csv("data/avocado_ripeness_dataset.csv")
st.dataframe(df)

# Visualisasi distribusi berat
st.subheader("Histogram Berat")
if "Berat" in df.columns:
    fig, ax = plt.subplots()
    df["Berat"].hist(bins=20, color="green", edgecolor="black", ax=ax)
    st.pyplot(fig)
else:
    st.error("Kolom 'Berat' tidak ditemukan dalam dataset.")
