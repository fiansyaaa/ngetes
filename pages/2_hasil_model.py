# pages/1_📝_Input_Prediksi.py
import streamlit as st
import time

st.title("📝 Input Data untuk Prediksi")

st.write("Masukkan nilai-nilai fitur bunga Iris:")

# Input
sepal_length = st.number_input("Panjang Sepal (cm)", 4.0, 8.0, 5.8)
sepal_width = st.number_input("Lebar Sepal (cm)", 2.0, 4.5, 3.0)
petal_length = st.number_input("Panjang Petal (cm)", 1.0, 7.0, 4.35)
petal_width = st.number_input("Lebar Petal (cm)", 0.1, 2.5, 1.3)

if st.button("Prediksi Sekarang"):
    st.session_state["input_data"] = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    st.success("Data disimpan! Mengarahkan ke halaman hasil...")
    time.sleep(1)
    st.experimental_rerun()  # rerun untuk redirect

    # Redirect ke halaman hasil prediksi (halaman 3)
    st.switch_page("pages/2_📈_Hasil_Prediksi.py")
