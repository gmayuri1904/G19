import pandas as pd
import numpy as np
import pickle
import streamlit as st

model=pickle.load(open('insurance.pkl','rb'))

st.title('Insurance Cost Prediction')

age=st.number_input('Age',value=25,min_value=18,max_value=60,step=1)
gender = st.radio('Gender',('Male', 'Female'))

if gender == 'Male':
    gender_value = 0
else:
    gender_value=1

bmi=st.number_input('BMI',value=30,min_value=10,max_value=60,step=1)

children=st.number_input('Children',value=0,min_value=0,max_value=10,step=1)

smoker = st.selectbox(
    'Are you a smoker ?',
    ('Yes', 'No'))
if smoker=="Yes":
    smoke=1
else:
    smoke=0


result=model.predict([[age,gender_value,bmi,children,smoke]])
res='Insurance charge is '+str(int(result[0][0]))
st.success(res)