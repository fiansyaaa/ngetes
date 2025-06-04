import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Alpukat")

df = pd.read_csv("data/avocado_ripeness_dataset.csv")
st.write("🔍 Cuplikan Data")
st.dataframe(df.head())

st.subheader("Histogram Berat")
fig1, ax1 = plt.subplots()
df['weight'].hist(bins=20, color='green', edgecolor='black', ax=ax1)
ax1.set_xlabel("Berat (gram)")
ax1.set_ylabel("Jumlah")
st.pyplot(fig1)

st.subheader("Scatter Plot Warna vs Kematangan")
fig2, ax2 = plt.subplots()
ax2.scatter(df['color_score'], df['ripeness'], color='orange')
ax2.set_xlabel("Skor Warna")
ax2.set_ylabel("Tingkat Kematangan")
st.pyplot(fig2)
