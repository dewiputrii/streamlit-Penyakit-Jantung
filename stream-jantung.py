import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open("penyakit_jantung.sav", "rb"))

# judul web
st.title("Prediksi Penyakit Jantung")

age = st.number_input("Umur")

sex = st.number_input("Jenis Kelamin")

cp = st.number_input("Jenis Nyeri Dada")

trestbps = st.number_input("Tekanan Darah")

chol = st.number_input("Nilai Kolesterol")

fbs = st.number_input("Gula Darah")

restecg = st.number_input("Hasil Elektrokadrografi")

thalach = st.number_input("Detak Jantung Maksimum")

exang = st.number_input("Induksi Angina")

oldpeak = st.number_input("ST Depresion")

slope = st.number_input("Slope")

ca = st.number_input("Nilai CA")

thal = st.number_input("Nilai Thal")

# code for prediction
heart_diagnosis = ""

# membuat tombol prediksi
if st.button("Prediksi Penyakit Jantung"):
    heart_prediction = model.predict(
        [
            [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            ]
        ]
    )

    if heart_prediction[0] == 1:
        heart_diagnosis = "Pasien Terkena Penyakit Jantung"
    else:
        heart_diagnosis = "Pasien Tidak Terkena Penyakit Jantung"

st.success(heart_diagnosis)
