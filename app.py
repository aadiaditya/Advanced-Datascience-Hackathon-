
"""
@author: Advanced Datascience Hackathon -- Aditya
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Home Page'
                            'Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','activity','heart'],
                          default_index=0)
    
#Home Page
if (selected == 'Home Page'):
    
    # page title
    st.title('Heart and Diabetes Disease Prediction using ML')  
    st.image('teampic.jpg')
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Times Pregnant')
        
    with col2:
        Glucose = st.text_input('Glucose Level(0-199)')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value(0-140)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value(0-99)')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic!Please consult Doctor'
        else:
          diab_diagnosis = 'The person is not diabetic.Please take Healthy Diet ,taking care of your body can prevent from diabetes'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        
        age = st.text_input('Age')
        
    with col2:
        sex_options=["Male","Female"]
        sex_selected=st.selectbox("choose sex of person", options=sex_options)
        if sex_selected=="Male":
            sex=1
        else:
            sex=0
        #sex = st.text_input('Sex(1=Male,0=Female)')
        
    with col3:
        cp_types = ["typical angina","atypical angina","non-anginal pain","asymptomatic patient"]
        cp_selected =st.selectbox("choose chestpain type", options=cp_types)
        if cp_selected=="typical angina":
            cp=0
        elif cp_selected=="atypical angina":
            cp=1
        elif cp_selected=="non-anginal pain":
            cp=2
        else:
            cp=3
        #cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure(94-200)')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl(126-564')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar in mg/dl(>120 True(1) else False(0))')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(normal=0,Having ST-T=1,Hypertrophy=2)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved(220-age)')
        
        
    with col3:
        exang = st.text_input('Exercise Induced Angina(Yes=1,No=0)')

        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope_types=['Upsloping','Flat','Downsloping']
        slope_selected =st.selectbox("choose slope type", options=slope_types)
        if slope_selected=="Upsloping":
            slope=0
        elif slope_selected=="Flat":
            slope=1
        else:
            slope=2
        
        #slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(Presence=1,Absence=0)')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease!Please Consult Doctor'
        else:
          heart_diagnosis = "The person does not have any heart disease. Follow these measures to prevent Heart Disease 1.Eat a Healthy Diet  2.Be a physically Active 3.Control Blood Sugar 4.Monitor Blood Pressure 5.Quit Smoking"          
          
                               
                             
        
    st.success(heart_diagnosis)
        
    
    


   
        
   


