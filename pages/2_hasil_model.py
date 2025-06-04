import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("🧠 Prediksi Kematangan Alpukat")

# Load dataset
df = pd.read_csv("data/avocado_ripeness_dataset.csv")
df.dropna(inplace=True)

# Pastikan kolom ada
required_cols = ["Berat", "Warna", "Kekerasan", "Ripeness"]
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset harus memiliki kolom: {required_cols}")
    st.stop()

# Siapkan data
X = df[["Berat", "Warna", "Kekerasan"]]
y = df["Ripeness"]

# Latih model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Input pengguna
st.subheader("🛠️ Masukkan Parameter")
berat = st.number_input("Berat (gram)", 50.0, 500.0, 150.0)
warna = st.slider("Warna (0 = Hijau, 1 = Cokelat)", 0.0, 1.0, 0.5)
kekerasan = st.slider("Kekerasan (0 = Lembek, 1 = Keras)", 0.0, 1.0, 0.5)

# Prediksi otomatis
prediksi = model.predict([[berat, warna, kekerasan]])[0]
st.subheader("📌 Hasil Prediksi")
st.success(f"Tingkat Kematangan (Ripeness): **{prediksi:.2f}**")
