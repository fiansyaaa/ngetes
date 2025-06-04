import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Data Gempa Indonesia")

df = pd.read_csv("data/gempa.csv")

st.subheader("🔍 Tinjauan Data")
st.dataframe(df)

st.subheader("📊 Visualisasi Magnitudo")
fig, ax = plt.subplots()
df['Magnitudo'].hist(bins=30, edgecolor='black', ax=ax)
ax.set_xlabel("Magnitudo")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)
