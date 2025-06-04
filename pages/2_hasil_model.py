import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("🧠 Prediksi Kematangan Alpukat")

# Load dan latih model
df = pd.read_csv("data/avocado_ripeness_dataset.csv")
df.dropna(inplace=True)

X = df[["weight", "color_score", "firmness"]]
y = df["ripeness"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Input pengguna
st.subheader("🛠️ Masukkan Parameter Alpukat")
col1, col2, col3 = st.columns(3)

with col1:
    berat = st.number_input("Berat (gram)", 50.0, 500.0, 150.0)

with col2:
    warna = st.slider("Skor Warna (0 = Hijau, 1 = Cokelat)", 0.0, 1.0, 0.5)

with col3:
    kekerasan = st.slider("Kekerasan (0 = Lembek, 1 = Keras)", 0.0, 1.0, 0.5)

# Prediksi otomatis
prediksi = model.predict([[berat, warna, kekerasan]])[0]

st.subheader("📌 Hasil Prediksi")
st.success(f"Prediksi Tingkat Kematangan: **{prediksi:.2f}** (0 = mentah, 1 = matang)")
