import pandas as pd
import streamlit as st
from database import view_Appointment, view_only_Appointment_ID, delete_data_app ,view_all_data_Patient, view_only_Patient_ID, delete_data_pat,view_all_data_doctor, view_only_Doctor_ID, delete_data_doc
from database import  view_all_data_Treatment, view_only_Treatment_ID,delete_data_treat, view_all_data_Review, view_only_review_ID, delete_data_review, view_all_data_bill, view_only_bill_ID, delete_data_bill

def deleteapp():
    result = view_Appointment()
    df = pd.DataFrame(result, columns=['Appointment_Type', 'Date_of_Appointment', 'Patient_ID', 'END_time', 'Appointment_ID','Start_time','Doctor_ID'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_Appointments = [i[0] for i in view_only_Appointment_ID ()]
    selected_Appointment = st.selectbox("Appointment to Cancel", list_of_Appointments)
    st.warning("Do you want to delete ::{}".format(selected_Appointment))
    if st.button("Cancel Appointment"):
        delete_data_app(selected_Appointment)
        st.success("Appointment has been Cancelled successfully")
    new_result = view_Appointment()
    df2 = pd.DataFrame(new_result, columns=['Appointment_Type', 'Date_of_Appointment', 'Patient_ID', 'END_time', 'Appointment_ID','Start_time','Doctor_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def deletepat():
    result = view_all_data_Patient()
    df = pd.DataFrame(result, columns=['Address', 'DOB', 'Patient_ID', 'First_name',' Last_name','Gender','Email','Phone'])
    with st.expander("Admitted Patients"):
        st.dataframe(df)

    list_of_patients = [i[0] for i in view_only_Patient_ID ()]
    selected_patients = st.selectbox("Discharge the patient", list_of_patients)
    st.warning("Do you want to delete ::{}".format(selected_patients))
    if st.button("Discharge Patients"):
        delete_data_pat(selected_patients)
        st.success("Patient has been discharged successfully")
    new_result = view_all_data_Patient()
    df2 = pd.DataFrame(new_result, columns=['Address', 'DOB', 'Patient_ID', 'First_name',' Last_name','Gender','Email','Phone'])
    with st.expander("Remaining Patients"):
        st.dataframe(df2)

def deletedoc():
    result = view_all_data_doctor()
    df = pd.DataFrame(result, columns=['Doctor_ID','Job_type', 'First_name', 'Last_name', 'Street', 'Pincode' ,'Anual_Salary'])
    with st.expander("All Doctors"):
        st.dataframe(df)

    list_of_doc = [i[0] for i in view_only_Doctor_ID ()]
    selected_doc = st.selectbox("Remove Doctor", list_of_doc)
    st.warning("Do you want to remove ::{}".format(selected_doc))
    if st.button("Remove Doctor"):
        delete_data_doc(selected_doc)
        st.success("Doctor has been removed successfully")
    new_result = view_all_data_doctor()
    df2 = pd.DataFrame(new_result, columns=['Doctor_ID','Job_type', 'First_name', 'Last_name', 'Street', 'Pincode' ,'Anual_Salary'])
    with st.expander("Remaining Doctors"):
        st.dataframe(df2)

def deletetreat():
    result = view_all_data_Treatment()
    df = pd.DataFrame(result, columns=['Treatment_ID', 'Tooth', 'Medication', 'Patient_ID','Appointment_ID' ,'Doctor_ID'])
    with st.expander("All Treatments"):
        st.dataframe(df)

    list_of_treat = [i[0] for i in view_only_Treatment_ID ()]
    selected_Treat = st.selectbox("Cancel Treatments", list_of_treat)
    st.warning("Do you want to Cancel::{}".format(selected_Treat))
    if st.button("Cancel Treatments"):
        delete_data_treat(selected_Treat)
        st.success("Tretment cancelled successfully")
    new_result = view_all_data_Treatment()
    df2 = pd.DataFrame(new_result, columns=['Treatment_ID', 'Tooth', 'Medication', 'Patient_ID','Appointment_ID' ,'Doctor_ID'])
    with st.expander("Treatments Remaining"):
        st.dataframe(df2)

def deletereview():
    result = view_all_data_Review()
    df = pd.DataFrame(result, columns=['Treatment_Description', 'Date_of_Review','Cleanliness','Communication','Professionalism','Review_ID','Treatment_ID','Doctor_ID'])
    with st.expander("All Reviews"):
        st.dataframe(df)

    list_of_review = [i[0] for i in view_only_review_ID()]
    selected_review = st.selectbox("Cancel Treatments", list_of_review)
    st.warning("Do you want to Cancel::{}".format(selected_review))
    if st.button("Remove Review"):
        delete_data_review(selected_review)
        st.success("Removed Review successfully")
    new_result = view_all_data_Review()
    df2 = pd.DataFrame(new_result, columns=['Treatment_Description', 'Date_of_Review','Cleanliness','Communication','Professionalism','Review_ID','Treatment_ID','Doctor_ID'])
    with st.expander("Review Remaining"):
        st.dataframe(df2)

def deletebill():
    result = view_all_data_bill()
    df = pd.DataFrame(result, columns=['Bill_ID', 'Total_amount', 'Payment_Type',' Patient_ID','Payment_status'])
    with st.expander("All Bills"):
        st.dataframe(df)

    list_of_bill = [i[0] for i in view_only_bill_ID()]
    selected_bill = st.selectbox("Cancel Treatments", list_of_bill)
    st.warning("Do you want to Cancel::{}".format(selected_bill))
    if st.button("Cancel Bill"):
        delete_data_bill(selected_bill)
        st.success("Cancelled bill successfully")
    new_result = view_all_data_bill()
    df2 = pd.DataFrame(new_result, columns=['Bill_ID', 'Total_amount', 'Payment_Type',' Patient_ID','Payment_status'])
    with st.expander("Bills remaining"):
        st.dataframe(df2)