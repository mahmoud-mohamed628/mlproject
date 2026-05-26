import streamlit as st
import pandas as pd
import pickle

# 1. Loading l-model (li hda app.py)
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. Interface (Zwaq)
st.set_page_config(page_title="Diabetes Predictor", layout="centered")
st.title("🩺 Prediction de Diabète")
st.write("Dkhl m3loumat l-marid:")

# 3. Inputs (Slider o Number Input)
age = st.slider("Âge", 0, 100, 25)
glucose = st.number_input("Taux de Glucose", 0, 300, 100)
bmi = st.number_input("IMC (BMI)", 0.0, 70.0, 25.0)
bp = st.number_input("Pression Artérielle", 0, 150, 70)
insuline = st.number_input("Insuline", 0, 800, 30)
grossesses = st.number_input("Grossesses", 0, 20, 0)
skin = st.number_input("Epaisseur de la peau", 0, 100, 20)
pedigree = st.number_input("Indice d'hérédité", 0.0, 3.0, 0.5)

# 4. Button dial Prediction
if st.button("Lancer la prédiction"):
    # Organiser les données (Darouri nefs tartib l-dataset l'asli)
    data = pd.DataFrame([[grossesses, glucose, bp, skin, insuline, bmi, pedigree, age]], 
                        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
    
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error("⚠️ L-model kigoul: Had l-personne fiha Diabète.")
    else:
        st.success("✅ L-model kigoul: Ma-fiha walou, Labass.")