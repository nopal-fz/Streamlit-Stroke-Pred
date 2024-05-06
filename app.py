import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model_stroke.sav', 'rb'))
st.title('Stroke Web Prediction')

col1, col2 = st.columns(2)

with col1:
    gender_select = st.selectbox('Gender', options=['Female', 'Male'])
    gender = 1 if gender_select == 'Male' else 0

with col2:
    age = st.number_input('Age', 5, 100)

with col1:
    hypertension_select = st.selectbox('Hypertension', options=['No', 'Yes'])
    hypertension = 1 if hypertension_select == 'Yes' else 0

with col2:
    heart_disease_select = st.selectbox('Heart Disease', options=['No', 'Yes'])
    heart_disease = 1 if heart_disease_select == 'Yes' else 0

with col1:
    ever_married_select = st.selectbox('Ever Married', options=['No', 'Yes'])
    ever_married = 1 if ever_married_select == 'Yes' else 0

with col2:
    residence_select = st.selectbox('Residence Type', options=['Urban', 'Rural'])
    Residence_type = 1 if residence_select == 'Urban' else 0

with col1:
    avg_glucose_level = st.number_input('Glucose', min_value=50.0, max_value=300.0, step=0.1)

with col2:
    bmi = st.number_input('Bmi',  min_value=10.0, max_value=100.0, step=0.1)

with col1:
    smoking_status_select = st.selectbox('Smoking Status', options=['No', 'Yes'])
    smoking_status = 1 if smoking_status_select == 'Yes' else 0

govt_job = 0
never_worked = 0
private = 0
self_employed = 0
children = 0

with col2:
    selected_work = st.selectbox('Select Work:', options=['Government', 'Never Worked', 'Private', 'Self Employed', 'Children'])

if selected_work == 'Government':
    govt_job = 1
elif selected_work == 'Never Worked':
    never_worked = 1
elif selected_work == 'Private':
    private = 1
elif selected_work == 'Self Employed':
    self_employed = 1
else:
    children = 1

if st.button('Stroke Prediction'):
    stroke_pred = model.predict([[gender, age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, smoking_status, govt_job, never_worked, private, self_employed, children]])

    if (stroke_pred)[0] == 1:
        stroke_diag = 'you had a stroke'
        st.error(stroke_diag)
    else:
        stroke_diag = "you didn't have a stroke"
        st.success(stroke_diag)