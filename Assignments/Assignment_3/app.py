#import model
from numpy import double
import streamlit as st
import pickle

#load model

model = pickle.load(open("E:\Учеба\Магистратура 2 семестр\Методы машинного обучения\lectures\classical_ml_urfu\Assignments\Assignment_3\diabetes.pkl",'rb'))


st.set_page_config(layout='wide')
st.title('diabetesMed')

with st.container():
    st.text('Indicates if there was any diabetic medication prescribed. Values: “yes|1” and “no|0')

    with st.form(key='diabetes_form'):
        st.text('Enter the Details Below')

        race = st.text_input(label="Pacient's race")
        gender = st.text_input(label="Pacient's gender")
        age = st.text_input(label="Pacient's age")
        time_in_hospital = st.text_input(label="Time in hospital")
        medical_specialty  =  st.text_input(label="medical_specialty")      
        num_lab_procedures  =   st.text_input(label="num_lab_procedures")   
        num_procedures      =   st.text_input(label="num_procedures")   
        num_medications      =  st.text_input(label="num_medications")  
        number_outpatient   =    st.text_input(label=" number_outpatient")  
        number_emergency     =   st.text_input(label="number_emergency") 
        number_inpatient   =     st.text_input(label="number_inpatient")
        diag_1     =             st.text_input(label="diag_1")   
        diag_2     =  st.text_input(label="diag_2")              
        diag_3       = st.text_input(label="diag_3")             
        number_diagnoses = st.text_input(label="number_diagnoses")      
        max_glu_serum   = st.text_input(label="max_glu_serum")          
        A1Cresult       = st.text_input(label="A1Cresult")          
        metformin       = st.text_input(label="metformin")          
        repaglinide     =  st.text_input(label="repaglinide")         
        nateglinide      =  st.text_input(label="nateglinide")        
        chlorpropamide      = st.text_input(label="chlorpropamide")      
        glimepiride       = st.text_input(label="glimepiride")        
        acetohexamide   =  st.text_input(label="acetohexamide")         
        glipizide      =  st.text_input(label="glipizide")          
        glyburide       = st.text_input(label="glyburide")          
        tolbutamide    = st.text_input(label="tolbutamide")           
        pioglitazone   = st.text_input(label="pioglitazone")           
        rosiglitazone  = st.text_input(label="rosiglitazone")          
        acarbose      =  st.text_input(label="acarbose")          
        miglitol       =  st.text_input(label="miglitol")          
        troglitazone    =  st.text_input(label="troglitazone")         
        tolazamide      =  st.text_input(label="tolazamide")         
        examide         = st.text_input(label="examide")          
        citoglipton    =  st.text_input(label="citoglipton")          
        insulin         =  st.text_input(label="insulin")         
        #glyburide-metformin  == st.text_input(label="glyburide-metformin")     
        #glipizide-metformin     == st.text_input(label="glipizide-metformin")  
        #glimepiride-pioglitazone ==  st.text_input(label="glimepiride-pioglitazone")
        #metformin-rosiglitazone   == st.text_input(label="metformin-rosiglitazone")
        #metformin-pioglitazone   ==  st.text_input(label="metformin-pioglitazone")
        change             =  st.text_input(label="change")     
        diabetesMed          =  st.text_input(label="diabetesMed")   
        readmitted= st.text_input(label="readmitted")

        submit = st.form_submit_button()

        output = model.predict([[0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1]])
        
        st.text('prediction is: '+str(output))