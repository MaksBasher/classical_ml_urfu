#import model
from numpy import double
import streamlit as st
import pickle

model = pickle.load(open("credit-final.pkl",'rb'))

st.set_page_config(layout='wide')
st.title('Credit evaluation application')

with st.container():
    st.text("Enter the numbers according to your current situation:")
    with st.form(key='credit_form'):
        
        checking_status = st.selectbox('Select your current checking account status', ['Negative balance',
                                                                                       'Checking account balance is between 0 and 200',
                                                                                       "Don't have an account select",
                                                                                       'Checking account balance exceeds 200'])
        if checking_status == "Negative balance":
            checking_status = 0
        elif checking_status == "Checking account balance is between 0 and 200":
            checking_status = 1
        elif checking_status == "Don't have an account select":
            checking_status = 2
        else:
            checking_status = 3
            
        duration = st.slider('Select credit duration in months', 0, 100)
        
        credit_history = st.selectbox('Select your current credit history status', ['Has critical/other existing credit',
                                                                                    'All existing credits are paid',
                                                                                    'Delayed credit previously',
                                                                                    'No credits/all paid',
                                                                                    'All paid'])
        if credit_history == "Have critical/other existing credits":
            credit_history = 0
        elif credit_history == "All existing credits are paid":
            credit_history = 1
        elif credit_history == "Delayed credits previously":
            credit_history = 2
        elif credit_history== "No credits/all paid":
            credit_history = 3
        else:
            credit_history = 4
            
        
        purpose = st.selectbox('Select the purpose of your credit', ['Radio/tv','Education','Furniture/equipment','New car','Used car',
                                                                     'Business','Domestic appliance','Repairs','Other','Retraining'])
        if purpose == "Radio/tv":
            purpose = 0
        elif purpose == "Education":
            purpose = 1
        elif purpose == "Furniture/equipment":
            purpose = 2
        elif purpose == "New car":
            purpose = 3
        elif purpose == "Used car":
            purpose = 4
        elif purpose == "Business":
            purpose = 5
        elif purpose == "Domestic appliance":
            purpose = 6
        elif purpose == "Repairs":
            purpose = 7
        elif purpose == "Other":
            purpose = 8
        else:
            purpose = 9
    
        
        credit_amount = st.slider('Select credit amount', 0, 100000,10000,500,)
        age = st.slider('Select your age', 18, 100)
        
        other_payment_plans = st.selectbox('Select if you have other payment plans', ['None','Bank','Stores'])
        if other_payment_plans == "None":
            other_payment_plans = 0
        elif other_payment_plans == "Bank":
            other_payment_plans = 1
        else:
            other_payment_plans = 2
        
        installment_commitment = st.slider('Installment rate in percentage of disposable income', 1., 4.)
        
        personal_status = st.selectbox('Select your current personal relationship status', ['Male - single',
                                                                                            'Female - div/dep/mar',
                                                                                            'Male - div/sep',
                                                                                            'Male - mar/wid'])
        if personal_status == "Male - single":
            personal_status = 0
        elif personal_status == "Female - div/dep/mar":
            personal_status = 1
        elif personal_status == "Male - div/sep":
            personal_status = 2
        else:
            personal_status = 3    
            
        submit = st.form_submit_button()
        
        if submit:
            st.write("Input:", checking_status,',',duration, ',',credit_history,',', purpose, ',',credit_amount, ',', age,',', other_payment_plans,',', installment_commitment,',', personal_status)

            output = model.predict([[float(checking_status),float(duration),float(credit_history),float(purpose),float(credit_amount),float(age),float(other_payment_plans),installment_commitment,float(personal_status)]])
            st.text ("Your credit is likely to turn out " +output)
            
            if output == "bad":
                st.image('https://www.thebalancemoney.com/thmb/gdvxx4u-WPB6pyL9Q3kiJtnmUY4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/notstonks-7d82ebccce6d4960b42b2bc6c1670463.jpeg')
            else:
                st.image('https://i.insider.com/601448566dfbe10018e00c5d?width=700')