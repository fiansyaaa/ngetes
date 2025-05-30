# pages/2_📈_Hasil_Prediksi.py
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

st.title("📈 Hasil Prediksi Spesies Iris")

# Periksa apakah ada data di session state
if "input_data" not in st.session_state:
    st.warning("Silakan isi data terlebih dahulu di halaman 'Input Prediksi'.")
    st.stop()

# Ambil data
data = st.session_state["input_data"]

# Load model
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target
model = RandomForestClassifier()
model.fit(X, y)

# Prediksi
X_new = pd.DataFrame([[
    data["sepal_length"],
    data["sepal_width"],
    data["petal_length"],
    data["petal_width"]
]], columns=X.columns)

prediction = model.predict(X_new)[0]
probs = model.predict_proba(X_new)[0]

# Hasil
st.markdown("### Data yang Dimasukkan")
st.write(X_new)

st.markdown("### Prediksi")
st.success(f"Spesies bunga Iris diprediksi sebagai **{iris.target_names[prediction]}**")

st.markdown("### Probabilitas Klasifikasi")
for i, class_name in enumerate(iris.target_names):
    st.write(f"- {class_name}: {probs[i]:.2%}")
