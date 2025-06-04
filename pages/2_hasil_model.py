import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("🧠 Prediksi Sederhana Magnitudo Gempa")

df = pd.read_csv("data/gempa.csv")
df.dropna(subset=["Tanggal", "Magnitudo", "Kedalaman"], inplace=True)

# Ubah tanggal jadi ordinal untuk regresi
df["Tanggal"] = pd.to_datetime(df["Tanggal"])
df["Tanggal_ordinal"] = df["Tanggal"].map(lambda date: date.toordinal())

X = df[["Tanggal_ordinal", "Kedalaman"]]
y = df["Magnitudo"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

st.subheader("Prediksi dari Input Manual")
tanggal_input = st.date_input("Tanggal", value=pd.to_datetime("2024-01-01"))
kedalaman_input = st.slider("Kedalaman (km)", 0, 700, 10)

prediksi = model.predict([[tanggal_input.toordinal(), kedalaman_input]])
st.write(f"🎯 Prediksi Magnitudo: `{prediksi[0]:.2f}`")
