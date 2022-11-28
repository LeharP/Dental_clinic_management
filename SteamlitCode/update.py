import pandas as pd
import streamlit as st
from database import view_Appointment, view_only_Appointment_ID ,view_all_data_Patient, view_only_Patient_ID, view_all_data_doctor, view_only_Doctor_ID
from database import  view_all_data_Treatment, view_only_Treatment_ID, view_all_data_Review, view_only_review_ID,  view_all_data_bill, view_only_bill_ID
from database import get_details_app,get_details_pat,get_details_doc, get_details_treat, get_details_review, get_details_bill
from database import edit_details_app,edit_details_pat,edit_details_doc, edit_details_Treat, edit_details_review, edit_details_bill

list3 = ['Endodontist','Orthodontist','Pedodontist','Prosthodontist','Oral Pathologist']
list10 = ['Midazolam','Anesthesia','Ibuprofen']
list6 = ['Cash','Card','UPI',]
list7 =['Pending','Paid']
list5=["Male","Female","others"]
def updateapp():
    result = view_Appointment()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Appointment_Type','Date_of_appointment','Patient_ID','END_time','Appointment_ID','Start_time','Doctor_ID'])
    with st.expander("Current Appointments"):
        st.dataframe(df)
    list_of_Appointments = [i[0] for i in view_only_Appointment_ID()]
    selected_appointment = st.selectbox("Appointment to Change", list_of_Appointments)
    selected_result = get_details_app(selected_appointment)
    # st.write(selected_result)
    if selected_result:
        Appointment_Type= selected_result[0][0]
        Date_of_appointment = selected_result[0][1]
        Patient_ID = selected_result[0][2]
        END_time = selected_result[0][3]
        Appointment_ID = selected_result[0][4]
        Start_time = selected_result[0][5]
        Doctor_ID = selected_result[0][6]

        col1, col2 = st.columns(2)
        with col1:
            new_Appointment_ID = st.text_input("Appointment ID",Appointment_ID)
            #Doctor_ID  =  st.selectbox("Select the Doctor ID",list)
            new_Doctor_ID  =  st.text_input("Doctor ID",Doctor_ID)
            new_Patient_ID = st.text_input("Patient ID",Patient_ID)
        
        with col2:
            new_Start_time   = st.text_input("Appointment start time",Start_time)
            new_END_time   = st.text_input("Ending time",END_time)
            new_Appointment_Type = st.text_input("Type of Appointment",Appointment_Type)
            new_Date_of_appointment = st.text_input("Date of Apointment",Date_of_appointment)

        if st.button("Change Appointment"):
            edit_details_app(new_Appointment_Type, new_Date_of_appointment,new_Appointment_ID, new_Doctor_ID, new_Patient_ID, new_END_time,new_Start_time, Appointment_Type, Date_of_appointment, Appointment_ID, Doctor_ID, Patient_ID, END_time,Start_time)
            st.success("Successfully updated :: {} to ::{}".format(Appointment_ID, new_Appointment_ID))

    result2 = view_Appointment()
    df2 = pd.DataFrame(result2, columns=['Appointment_Type','Date_of_appointment','Patient_ID','END_time','Appointment_ID','Start_time','Doctor_ID'])
    with st.expander("Changed Appointment"):
        st.dataframe(df2)

def updatepat():
    result = view_all_data_Patient()
    df = pd.DataFrame(result, columns=['Address','DOB','Patient_ID','First_name','Last_name','Gender','Email','Phone'])
    with st.expander("Admitted Patients"):
        st.dataframe(df)
    list_of_Appointments = [i[0] for i in view_only_Patient_ID()]
    selected_appointment = st.selectbox("Patient whose information to be edited", list_of_Appointments)
    selected_result = get_details_pat(selected_appointment)
 
    if selected_result:
        Address= selected_result[0][0]
        DOB = selected_result[0][1]
        Patient_ID = selected_result[0][2]
        First_name= selected_result[0][3]
        Last_name = selected_result[0][4]
        Gender = selected_result[0][5]
        Email = selected_result[0][6]
        Phone = selected_result[0][7]

        col1, col2 = st.columns(2)
        with col1:
            new_First_name   = st.text_input("First Name of the Patient",First_name)
            new_Last_name = st.text_input("Last Name of the Patient",Last_name)       
            new_DOB = st.date_input("Date of Birth of the Patient",DOB)
            new_Address = st.text_input("Address of Patient",Address)
        
        
        with col2:

            new_Patient_ID = st.text_input("Patient ID",Patient_ID)
            new_Gender   = st.text_input("Gender of the Patient",Gender)
            new_Email  =st.text_input("Email of the Patient",Email)
            new_Phone = st.number_input("Phone Number of the Patient",Phone)

        if st.button("Change Patient"):
            edit_details_pat(new_Address, new_DOB, new_Patient_ID, new_First_name,new_Last_name,new_Gender,new_Email,new_Phone, Address, DOB, Patient_ID, First_name, Last_name,Gender,Email,Phone)
            st.success("Successfully updated :: {} to ::{}".format(Patient_ID, new_Patient_ID))

    result2 = view_all_data_Patient()
    df2 = pd.DataFrame(result2, columns=['Address','DOB','Patient_ID','First_name',' Last_name','Gender','Email','Phone'])
    with st.expander("Changed Patient info"):
        st.dataframe(df2)

def updatedoc():
    
    result = view_all_data_doctor()
    df = pd.DataFrame(result, columns=['Doctor_ID','Job_type','First_name','Last_name','Street','Pincode','Anual_Salary'])
    with st.expander("Current Doctors"):
        st.dataframe(df)
    list_of_Appointments = [i[0] for i in view_only_Doctor_ID()]
    selected_appointment = st.selectbox("Doctor whose information to be edited", list_of_Appointments)
    selected_result = get_details_doc(selected_appointment)
 
    if selected_result:
        Doctor_ID= selected_result[0][0]
        Job_Type = selected_result[0][1]
        First_name = selected_result[0][2]
        Last_name= selected_result[0][3]
        Street = selected_result[0][4]
        Pincode = selected_result[0][5]
        Annual_Salary = selected_result[0][6]

        col1, col2 = st.columns(2)
        with col1:
            new_Doctor_ID = st.text_input("Doctor ID of the Doctor",Doctor_ID)
            new_Job_Type = st.selectbox("Method of Payment",list3)
            new_First_name = st.text_input("First name of the Doctor",First_name)
            new_Last_name = st.text_input("Last name of the Doctor",Last_name)
        
        with col2:
            new_Street = st.text_input("Street of the Doctor",Street)
            new_Pincode = st.number_input("Pincode of the Doctor",Pincode)
            new_Annual_Salary=st.number_input("Annual Salary of the Doctor",Annual_Salary)
    
        if st.button("Change Doctor info"):
            edit_details_doc(new_Doctor_ID,new_Job_Type,new_First_name,new_Last_name,new_Street ,new_Pincode,new_Annual_Salary,Doctor_ID ,Job_Type, First_name, Last_name, Street, Pincode ,Annual_Salary)
            st.success("Successfully updated :: {} to ::{}".format(Doctor_ID, new_Doctor_ID))

    result2 = view_all_data_doctor()
    df2 = pd.DataFrame(result2, columns=['Doctor_ID','Job_type','First_name','Last_name','Street','Pincode','Anual_Salary'])
    with st.expander("Changed Doctor info"):
        st.dataframe(df2)

def updatetreat():
    result = view_all_data_Treatment()
    df = pd.DataFrame(result, columns=['Treatment_ID','Tooth','Medication','Patient_ID','Appointment_ID','Doctor_ID'])
    with st.expander("Current Treatments"):
        st.dataframe(df)
    list_of_Appointments = [i[0] for i in view_only_Treatment_ID()]
    selected_appointment = st.selectbox("Change Treatment Details", list_of_Appointments)
    selected_result = get_details_treat(selected_appointment)
 
    if selected_result:
        Treatment_ID= selected_result[0][0]
        Tooth = selected_result[0][1]
        Medication = selected_result[0][2]
        Patient_ID= selected_result[0][3]
        Appointment_ID = selected_result[0][4]
        Doctor_ID = selected_result[0][5]

        col1, col2 = st.columns(2)
        with col1:
            new_Treatment_ID = st.text_input("Treatment ID of the patient",Treatment_ID)
            new_Patient_ID = st.text_input("Patient ID",Patient_ID)
            new_Appointment_ID = st.text_input("Appointment ID",Appointment_ID)
            new_Doctor_ID =st.text_input("Doctor ID",Doctor_ID)
        with col2:
            new_Tooth = st.number_input("Total no. of Teeth of the Patient",Tooth)
            new_Medication = st.selectbox("Type of Medication ",list10)
        

        if st.button("Change Treatment"):
            edit_details_Treat(new_Treatment_ID, new_Tooth, new_Medication, new_Patient_ID, new_Appointment_ID , new_Doctor_ID, Treatment_ID, Tooth, Medication, Patient_ID,Appointment_ID ,Doctor_ID)
            st.success("Successfully updated :: {} to ::{}".format(Patient_ID, new_Patient_ID))

    result2 = view_all_data_Treatment()
    df2 = pd.DataFrame(result2, columns=['Treatment_ID','Tooth','Medication','Patient_ID','Appointment_ID','Doctor_ID'])
    with st.expander("Changed Treatment"):
        st.dataframe(df2)

def updatereview():
    result = view_all_data_Review()
    df = pd.DataFrame(result, columns=['Treatment_Description','Date_of_Review','Cleanliness','Communication','Professionalism','Review_ID','Treatment_ID','Doctor_ID'])
    with st.expander("Reviews"):
        st.dataframe(df)
    list_of_Appointments = [i[0] for i in view_only_review_ID()]
    selected_appointment = st.selectbox("Change Review Details", list_of_Appointments)
    selected_result = get_details_review(selected_appointment)
 
    if selected_result:
        Treatment_Description= selected_result[0][0]
        Date_of_Review = selected_result[0][1]
        Cleanliness = selected_result[0][2]
        Communication= selected_result[0][3]
        Professionalism= selected_result[0][4]
        Review_ID = selected_result[0][5]
        Treatment_ID = selected_result[0][6  ]
        Doctor_ID = selected_result[0][7]

        col1, col2 = st.columns(2)
        with col1:
            new_Treatment_Description = st.text_input("Treatment Description",Treatment_Description)
            new_Date_of_Review = st.text_input("Date of review",Date_of_Review) 
            new_Cleanliness = st.number_input("Cleanliness",Cleanliness)
            new_Communication = st.number_input("Communication",Communication)
            new_Professionalism = st.number_input("Professionalism",Professionalism)
        with col2:
            new_Review_ID= st.text_input("Review ID ",Review_ID)
            new_Treatment_ID= st.text_input("Treatement ID",Treatment_ID)
            new_Doctor_ID= st.text_input("Doctor ID",Doctor_ID)
             
        if st.button("Change Review"):
            edit_details_review(new_Treatment_Description,new_Date_of_Review,new_Cleanliness,new_Communication,new_Professionalism,new_Review_ID,new_Treatment_ID,new_Doctor_ID,Treatment_Description,Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID)
            st.success("Successfully updated :: {} to ::{}".format(Review_ID,new_Review_ID))

    result3 = view_all_data_Review()
    df3 = pd.DataFrame(result3, columns=['Treatment_Description','Date_of_Review','Cleanliness','Communication','Professionalism','Review_ID','Treatment_ID','Doctor_ID'])
    with st.expander("Changed Review"):
        st.dataframe(df3)

def updatebill():
    result = view_all_data_bill()
    df = pd.DataFrame(result, columns=['Bill_ID','Total_amount','Payment_Type','Patient_ID','Payment_status'])
    with st.expander("Current Bills"):
        st.dataframe(df)
    list_of_Appointments = [i[0] for i in view_only_bill_ID()]
    selected_appointment = st.selectbox("Change Bills Details", list_of_Appointments)
    selected_result = get_details_bill(selected_appointment)
 
    if selected_result:
        Bill_ID= selected_result[0][0]
        Total_amount = selected_result[0][1]
        Payment_Type= selected_result[0][2]
        Patient_ID= selected_result[0][3]
        Payment_status= selected_result[0][4]

        col1, col2 = st.columns(2)
        with col1:
            new_Bill_ID = st.text_input("Bill ID of the patient",Bill_ID)
            new_Patient_ID = st.text_input("Patient ID",Patient_ID)
        
        with col2:
            new_Total_amount = st.number_input("Total amount of the bill",Total_amount)
            new_Payment_Type = st.selectbox("Method of Payment",list6)
            new_Payment_status = st.selectbox("Payment Status",list7)

        if st.button("Change Bill Details"):
            edit_details_bill(new_Bill_ID, new_Total_amount, new_Payment_Type, new_Patient_ID,new_Payment_status, Bill_ID, Total_amount, Payment_Type, Patient_ID,Payment_status)
            st.success("Successfully updated :: {} to ::{}".format(Bill_ID, new_Bill_ID))

    result2 = view_all_data_bill()
    df2 = pd.DataFrame(result2, columns=['Bill_ID','Total_amount','Payment_Type','Patient_ID','Payment_status'])
    with st.expander("New Bill"):
        st.dataframe(df2)
