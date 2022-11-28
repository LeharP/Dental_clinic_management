import streamlit as st
from database import add_data2,add_data5,add_data,add_data1,add_data3,add_data4

list5=["M","F","O"]
def createpat():
    col1, col2 = st.columns(2)
    with col1:
        First_name   = st.text_input("First Name of the Patient")
        Last_name = st.text_input("Last Name of the Patient")        
        DOB = st.date_input("Date of Birth of the Patient")
        Address = st.text_input("Address of Patient")
        
        
    with col2:

        Patient_ID = st.text_input("Patient ID")
        Gender   = st.selectbox("Gender of the Patient",list5)
        Email  =st.text_input("Email of the Patient")
        Phone = st.number_input("Phone Number of the Patient" )
        
    if st.button("Patient Details"):
        add_data(Address,DOB,Patient_ID,First_name,Last_name,Gender,Email,Phone)
        st.success("Successfully added Patient: {}".format(Patient_ID))

        
list3 = ['Endodontist','Orthodontist','Pedodontist','Prosthodontist','Oral Pathologist']
#list1 =['Pending','Paid']

def createdoc():
    col1, col2 = st.columns(2)
    with col1:
        Doctor_ID = st.text_input("Doctor ID of the Doctor")
        Job_type = st.selectbox("Job Type of the Doctor",list3)
        First_name = st.text_input("First name of the Doctor")
        Last_name = st.text_input("Last name of the Doctor")
        
    with col2:
        Street = st.text_input("street of the Doctor")
        Pincode = st.number_input("Pincode of the Doctor",min_value=560000)
        Annual_Salary=st.number_input("Annual Salary of the Doctor",min_value=0)
    
    if st.button("Enter Doctor Details"):
        add_data1(Doctor_ID,Job_type,First_name,Last_name,Street,Pincode,Annual_Salary)
        st.success("Successfully added a Doctor: {}".format(Doctor_ID))



#list = ['D01','D02','D03','D04','D05']

def createapp():
    col1, col2 = st.columns(2)
    with col1:
        Appointment_ID = st.text_input("Appointment ID")
        #Doctor_ID  =  st.selectbox("Select the Doctor ID",list)
        Doctor_ID  =  st.text_input("Doctor ID")
        Patient_ID = st.text_input("Patient ID")
        
    with col2:
        Start_time   = st.text_input("Appointment start time")
        END_time   = st.text_input("Ending time")
        Appointment_Type = st.text_input("Type of Appointment")
        Date_of_appointment = st.date_input("Date of Apointment")

    if st.button("Make an appointment"):
        add_data2(Appointment_Type,Date_of_appointment,Patient_ID,END_time,Appointment_ID,Start_time,Doctor_ID)
        st.success("Successfully added Appointment: {}".format(Appointment_ID))

list = ['Midazolam','Anesthesia','Ibuprofen','Null']
def createtreat():
    col1, col2 = st.columns(2)
    with col1:
        Treatment_ID = st.text_input("Treatment ID of the patient")
        Patient_ID = st.text_input("Patient ID")
        Tooth = st.number_input("Total no. of Teeth of the Patient",min_value=0)
        Medication = st.selectbox("Type of Medication ",list)
        
    with col2:
        Appointment_ID = st.text_input("Appointment ID")
        Doctor_ID =st.text_input("Doctor ID")
        
    if st.button("Treatment Details"):
        add_data3(Treatment_ID,Tooth,Medication,Patient_ID,Appointment_ID,Doctor_ID)
        st.success("Successfully added Treatment Details: {}".format(Treatment_ID))


#list4 = ['TID001','TID002','TID003','TID004','TID005']
#list1 =['Pending','Paid']

def createreview():
    col1, col2 = st.columns(2)
    with col1:
        Treatment_Description = st.text_input("Treatment Description")
        Date_of_Review = st.text_input("Date of review")
        Cleanliness = st.number_input("Cleanliness",min_value=0)
        Communication = st.number_input("Communication",min_value=0)
        Professionalism = st.number_input("Professionalism",min_value=0)
        
    with col2:
        Review_ID= st.text_input("Review ID ")
        Treatment_ID= st.text_input("Treatement ID")
        Doctor_ID= st.text_input("Doctor ID")
        

    
    if st.button("Review Details"):
        add_data4(Treatment_Description,Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID)
        st.success("Successfully added a Review: {}".format(Review_ID))
    

list6 = ['Cash','Card','UPI',]
list7 =['Pending','Paid']

def createbill():
    col1, col2 = st.columns(2)
    with col1:
        Bill_ID = st.text_input("Bill ID of the patient")
        Total_amount = st.number_input("Total amount of the bill")
        Payment_Type = st.selectbox("Method of Payment",list6)
        
    with col2:
        Patient_ID = st.text_input("Patient ID")
        Payment_status = st.selectbox("Payment Status",list7)
    
    if st.button("Make an Bill"):
        add_data5(Bill_ID,Total_amount,Payment_Type,Patient_ID,Payment_status)
        st.success("Successfully added a BILL: {}".format(Bill_ID))
    