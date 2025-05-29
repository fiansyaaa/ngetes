# pages/3_Prediksi.py
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Spesies Iris", page_icon="🔮")

st.markdown("# 🔮 Prediksi Spesies Iris")
st.sidebar.header("Prediksi")
st.write(
    """Masukkan nilai fitur bunga Iris untuk mendapatkan prediksi spesiesnya
    menggunakan model Decision Tree yang telah dilatih."""
)

# Fungsi untuk memuat model dan nama fitur (cache agar lebih cepat)
@st.cache_resource
def load_model_and_features(model_path, features_path):
    try:
        model = joblib.load(model_path)
        feature_names = joblib.load(features_path)
        return model, feature_names
    except FileNotFoundError as e:
        st.error(f"Error memuat file model/fitur: {e}. Pastikan Anda sudah menjalankan skrip 'simpan_model_dummy.py'.")
        return None, None
    except Exception as e:
        st.error(f"Terjadi kesalahan lain saat memuat: {e}")
        return None, None

model_path = 'model/model_iris.joblib'
features_path = 'model/nama_fitur_model_iris.joblib' # File yang menyimpan list nama fitur

model_iris_predict, nama_fitur_model = load_model_and_features(model_path, features_path)

if model_iris_predict and nama_fitur_model:
    st.subheader("Masukkan Nilai Fitur Bunga Iris:")

    # Membuat input fields secara dinamis berdasarkan nama_fitur_model
    # Ini lebih fleksibel jika model Anda punya banyak fitur
    input_values = {}
    # Tentukan min, max, default values (bisa didapat dari df.describe() di EDA)
    # Contoh default values (sesuaikan dengan data Anda)
    defaults = {'sepal_length': 5.4, 'sepal_width': 3.4, 'petal_length': 1.5, 'petal_width': 0.2}
    min_vals = {'sepal_length': 4.3, 'sepal_width': 2.0, 'petal_length': 1.0, 'petal_width': 0.1}
    max_vals = {'sepal_length': 7.9, 'sepal_width': 4.4, 'petal_length': 6.9, 'petal_width': 2.5}

    cols = st.columns(len(nama_fitur_model)) # Buat kolom sebanyak jumlah fitur

    for i, feature in enumerate(nama_fitur_model):
        with cols[i]: # Masukkan setiap input ke kolomnya masing-masing
            # Menggunakan nama fitur sebagai label, mengganti _ dengan spasi dan kapitalisasi
            label = feature.replace("_", " ").title()
            input_values[feature] = st.number_input(
                label=label + " (cm)",
                min_value=float(min_vals.get(feature, 0.0)), # default 0.0 jika tidak ada di min_vals
                max_value=float(max_vals.get(feature, 10.0)),# default 10.0 jika tidak ada di max_vals
                value=float(defaults.get(feature, (min_vals.get(feature, 0.0) + max_vals.get(feature, 10.0)) / 2)), # default rata-rata min/max
                step=0.1,
                key=f"input_{feature}" # Kunci unik untuk setiap input
            )

    if st.button("🌸 Prediksi Spesies"):
        # Buat DataFrame dari input pengguna dengan urutan kolom yang benar
        input_df = pd.DataFrame([input_values], columns=nama_fitur_model)

        st.write("Data yang Anda masukkan:")
        st.dataframe(input_df)

        try:
            # Lakukan prediksi
            prediction = model_iris_predict.predict(input_df)
            prediction_proba = model_iris_predict.predict_proba(input_df)

            # Menampilkan hasil
            predicted_species = prediction[0]
            st.success(f"**Hasil Prediksi Spesies Iris:** {predicted_species}")

            st.write("**Probabilitas Prediksi:**")
            # Dapatkan nama kelas dari model
            class_names = model_iris_predict.classes_
            proba_df = pd.DataFrame(prediction_proba, columns=class_names, index=["Probabilitas"])
            st.dataframe(proba_df)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
            st.error("Pastikan model telah dimuat dengan benar dan input data sesuai.")
else:
    st.warning("Model atau nama fitur tidak dapat dimuat. Halaman prediksi tidak dapat ditampilkan.")

