import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_Appointment,view_all_data_bill,view_all_data_doctor,view_all_data_Patient,view_all_data_Review,view_all_data_Treatment

def readpat():
    result = view_all_data_Patient()
    df = pd.DataFrame(result, columns=['Address','DOB','Patient_ID','First_name','Last_name','Gender','Email','Phone'])
    with st.expander("View all the Patients"):
        st.dataframe(df)

def readdoc():
    result1 = view_all_data_doctor()
    df1 = pd.DataFrame(result1, columns=['Doctor_ID','Job_type','First_name','Last_name','Street','Pincode','Anual_Salary'])
    with st.expander("View all the Doctors"):
        st.dataframe(df1)

def readapp():
    result = view_Appointment()
    df = pd.DataFrame(result, columns=['Appointment_Type','Date_of_Appointment','Patient_ID','END_time','Appointment_ID','Start_time','Doctor_ID'])
    with st.expander("View all the Appointments"):
        st.dataframe(df)

def readtreat():
    result = view_all_data_Treatment  ()
    df = pd.DataFrame(result, columns=['Treatment_ID','Tooth', 'Medication','Patient_ID','Appointment_ID','Doctor_ID'])
    with st.expander("View all the Treatments"):
        st.dataframe(df)

def readbill():
    result2 = view_all_data_bill()
    df2 = pd.DataFrame(result2, columns=['Bill_ID','Total_amount','Payment_Type','Patient_ID','Payment_status'])
    with st.expander("BILL"):
        st.dataframe(df2)

def readreview():
    result = view_all_data_Review()
    df = pd.DataFrame(result, columns=['Treatment_Description','Date_of_Review','Cleanliness','Communication','Professionalism','Review_ID','Treatment_ID','Doctor_ID'])
    with st.expander("View all the Reviews"):
        st.dataframe(df)

