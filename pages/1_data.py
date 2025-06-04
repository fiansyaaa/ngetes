import streamlit as st
import pandas as pd

st.title("Data Pasien")
df = pd.read_csv("anemia_dataset.csv")
st.dataframe(df)
