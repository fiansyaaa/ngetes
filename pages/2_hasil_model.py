# pages/2_Hasil_Model.py
import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Hasil Pelatihan Model", page_icon="⚙️")

st.markdown("# ⚙️ Hasil Pelatihan Model")
st.sidebar.header("Hasil Model")
st.write(
    """Halaman ini menampilkan performa model Decision Tree yang telah dilatih
    pada dataset Iris."""
)

# Fungsi untuk memuat model dan data tes (cache agar lebih cepat)
@st.cache_resource # Gunakan cache_resource untuk model atau objek non-data
def load_model_and_data(model_path, features_path, x_test_path, y_test_path):
    try:
        model = joblib.load(model_path)
        feature_names = joblib.load(features_path)
        X_test = joblib.load(x_test_path)
        y_test = joblib.load(y_test_path)
        return model, feature_names, X_test, y_test
    except FileNotFoundError as e:
        st.error(f"Error memuat file model/data: {e}. Pastikan Anda sudah menjalankan skrip 'simpan_model_dummy.py'.")
        return None, None, None, None
    except Exception as e:
        st.error(f"Terjadi kesalahan lain saat memuat: {e}")
        return None, None, None, None


model_path = 'model/model_iris.joblib'
features_path = 'model/nama_fitur_model_iris.joblib'
x_test_path = 'model/X_test_iris.joblib'
y_test_path = 'model/y_test_iris.joblib'

model_iris, nama_fitur, X_test_iris, y_test_iris = load_model_and_data(model_path, features_path, x_test_path, y_test_path)

if model_iris and X_test_iris is not None and y_test_iris is not None:
    st.subheader("Informasi Model")
    st.write(f"**Model yang digunakan:** {type(model_iris).__name__}") # Menampilkan nama kelas model
    # Anda bisa menambahkan parameter model di sini jika mau
    # st.write(f"**Parameter Model:** {model_iris.get_params()}")

    # Lakukan prediksi pada data tes
    try:
        y_pred_iris = model_iris.predict(X_test_iris)

        st.subheader("Metrik Evaluasi")
        accuracy = accuracy_score(y_test_iris, y_pred_iris)
        st.write(f"**Akurasi Model:** {accuracy:.4f}")

        st.subheader("Laporan Klasifikasi")
        # Dapatkan nama kelas dari model atau dari y_test unik jika model tidak punya .classes_
        target_names = model_iris.classes_ if hasattr(model_iris, 'classes_') else sorted(y_test_iris.unique())
        report = classification_report(y_test_iris, y_pred_iris, target_names=target_names, output_dict=False) # output_dict=True jika mau dataframe
        st.text_area("Laporan Detail:", value=report, height=250)
        # Untuk output_dict=True:
        # report_df = pd.DataFrame(classification_report(y_test_iris, y_pred_iris, target_names=target_names, output_dict=True)).transpose()
        # st.dataframe(report_df)


        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_test_iris, y_pred_iris, labels=target_names)
        fig_cm, ax_cm = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax_cm,
                    xticklabels=target_names, yticklabels=target_names)
        plt.xlabel("Prediksi Label")
        plt.ylabel("Label Sebenarnya")
        st.pyplot(fig_cm)

    except Exception as e:
        st.error(f"Error saat evaluasi model: {e}")
        st.error("Pastikan data tes (X_test_iris) memiliki fitur yang sama dengan saat training.")
else:
    st.warning("Model atau data tes tidak dapat dimuat. Silakan periksa kembali.")

