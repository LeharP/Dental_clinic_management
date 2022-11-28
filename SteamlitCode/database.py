import mysql.connector
import pandas as pd
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dental_clinic_database"
    #database="bleh"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS patient_556( Address varchar(50) not null,DOB date not null,Patient_ID varchar(10) not null,First_Name varchar(20) not null,Last_Name varchar(20) not null,Gender varchar(10) not null,Email varchar(50) not null, Phone bigint(10) not null,Primary key(Patient_ID));')
    c.execute('CREATE TABLE IF NOT EXISTS doctor_556(Doctor_ID varchar(10) not null,Job_type varchar(20) not null,First_Name varchar(20) not null, Last_Name varchar(20) not null,Street varchar(50) not null,Pincode int(6) not null,Annual_salary int(10) not null,Primary key (Doctor_ID));')
    c.execute('CREATE TABLE IF NOT EXISTS appointment_556(Appointment_type varchar(40) not null,Date_of_Appointment date not null,Patient_ID varchar(10) not null,End_time varchar(10) not null,Appointment_ID varchar(10) not null,Start_time varchar(10) not null,Doctor_ID varchar(10) not null,Primary key (Appointment_ID));')
    c.execute('CREATE TABLE IF NOT EXISTS treatment_556(Treatment_ID varchar(10) not null,Tooth int(4) not null,Medication varchar(50),Patient_ID varchar(10) not null,Appointment_ID varchar(10) not null,Doctor_ID varchar(10) not null,Primary key (Treatment_ID));')
    c.execute('CREATE TABLE IF NOT EXISTS review_556(Treatment_description varchar(100) not null,Date_of_review date not null,Cleanliness int(2) not null,Communication int(2) not null,Professionalism int(2) not null,Review_ID varchar(7) not null,Treatment_ID varchar(10) not null,Doctor_ID varchar(10) not null,Primary key (Review_ID));')
    c.execute('CREATE TABLE IF NOT EXISTS billing_556(Bill_ID varchar(10) not null,Total_amount int(10) not null,Payment_Type varchar(10) not null,Patient_ID varchar(10) not null,Payment_status varchar(20) not null,Primary key (Bill_ID));')

def add_data(Address,DOB,Patient_ID,First_name,Last_name,Gender,Email,Phone):
    c.execute('INSERT INTO patient_556 (Address,DOB,Patient_ID,First_name,Last_name,Gender,Email,Phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (Address,DOB,Patient_ID,First_name,Last_name,Gender,Email,Phone))
    mydb.commit()

def add_data1(Doctor_ID,Job_type,First_name,Last_name,Street,Pincode,Annual_Salary):
    c.execute('INSERT INTO doctor_556 (Doctor_ID,Job_type,First_name,Last_name,Street,Pincode,Annual_Salary) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (Doctor_ID,Job_type,First_name,Last_name,Street,Pincode,Annual_Salary))
    mydb.commit()

def add_data2(Appointment_Type,Date_of_Appointment,Patient_ID,END_time,Appointment_ID,Start_time,Doctor_ID):
    c.execute('INSERT INTO appointment_556 (Appointment_Type,Date_of_Appointment,Patient_ID,END_time,Appointment_ID,Start_time,Doctor_ID) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (Appointment_Type,Date_of_Appointment,Patient_ID,END_time,Appointment_ID,Start_time,Doctor_ID))
    mydb.commit()

def add_data3(Treatment_ID,Tooth,Medication,Patient_ID,Appointment_ID,Doctor_ID):
    c.execute('INSERT INTO treatment_556 (Treatment_ID,Tooth,Medication,Patient_ID,Appointment_ID,Doctor_ID) VALUES (%s,%s,%s,%s,%s,%s);',
              (Treatment_ID,Tooth,Medication,Patient_ID,Appointment_ID,Doctor_ID))
    mydb.commit()

def add_data4(Treatment_Description,Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID):
    c.execute('INSERT INTO review_556 (Treatment_Description,Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (Treatment_Description,Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID))
    mydb.commit()

def add_data5(Bill_ID,Total_amount,Payment_Type,Patient_ID,Payment_status):
    c.execute('INSERT INTO billing_556 (Bill_ID,Total_amount,Payment_Type,Patient_ID,Payment_status) VALUES (%s,%s,%s,%s,%s);',
              (Bill_ID,Total_amount,Payment_Type,Patient_ID,Payment_status))
    mydb.commit()

def view_only_Patient_ID():
    c.execute('SELECT Patient_ID from  patient_556')
    data = c.fetchall()
    return data

def view_only_Doctor_ID():
    c.execute('SELECT Doctor_ID from  doctor_556')
    data = c.fetchall()
    return data

def view_only_Appointment_ID():
    c.execute('SELECT Appointment_ID from  appointment_556')
    data = c.fetchall()
    return data

def view_only_Treatment_ID():
    c.execute('SELECT Treatment_ID from  treatment_556')
    data = c.fetchall()
    return data
    
def view_only_review_ID():
    c.execute('SELECT review_ID from review_556')
    data = c.fetchall()
    return data

def view_only_bill_ID():
    c.execute('SELECT Bill_ID from billing_556')
    data = c.fetchall()
    return data

def view_all_data_Patient():
    c.execute('SELECT * FROM patient_556')
    data = c.fetchall()
    return data

def view_all_data_doctor():
    c.execute('SELECT * FROM doctor_556')
    data = c.fetchall()
    return data

def view_Appointment():
    c.execute('SELECT * FROM appointment_556')
    data1 = c.fetchall()
    return data1

def view_all_data_Treatment():
    c.execute('SELECT * FROM Treatment_556')
    data = c.fetchall()
    return data

def view_all_data_Review():
    c.execute('SELECT * FROM review_556')
    data = c.fetchall()
    return data

def view_all_data_bill():
   c.execute('SELECT * FROM billing_556')
   data = c.fetchall()
   return data
    
def get_details_app(Appointment_ID):
    c.execute('SELECT * FROM appointment_556 WHERE Appointment_ID="{}"'.format(Appointment_ID))
    data = c.fetchall()
    return data

def get_details_pat(Patient_ID):
    c.execute('SELECT * FROM patient_556 WHERE Patient_ID="{}"'.format(Patient_ID))
    data = c.fetchall()
    return data

def get_details_doc(Doctor_ID):
    c.execute('SELECT * FROM Doctor_556 WHERE Doctor_ID="{}"'.format(Doctor_ID))
    data = c.fetchall()
    return data

def get_details_treat(Treatment_ID):
    c.execute('SELECT * FROM treatment_556 WHERE Treatment_ID="{}"'.format(Treatment_ID))
    data = c.fetchall()
    return data

def get_details_review(Review_ID):
    c.execute('SELECT * FROM review_556 WHERE Review_ID="{}"'.format(Review_ID))
    data = c.fetchall()
    return data

def get_details_bill(Bill_ID):
    c.execute('SELECT * FROM billing_556 WHERE Bill_ID="{}"'.format(Bill_ID))
    data = c.fetchall()
    return data

def edit_details_app(new_Appointment_Type,new_Date_of_appointment,new_Appointment_ID,new_Doctor_ID,new_Patient_ID,new_END_time,new_Start_time,Appointment_Type,Date_of_appointment,Appointment_ID,Doctor_ID,Patient_ID,END_time,Start_time):
    c.execute("UPDATE appointment_556 SET Appointment_Type=%s,Date_of_appointment=%s,Appointment_ID=%s,Doctor_ID=%s,Patient_ID=%s,END_time=%s,Start_time=%s WHERE Appointment_Type=%s and Date_of_appointment=%s and Appointment_ID=%s and Doctor_ID=%s and Patient_ID=%s and END_time=%s and Start_time=%s", (new_Appointment_Type, new_Date_of_appointment,new_Appointment_ID,new_Doctor_ID,new_Patient_ID,new_END_time,new_Start_time,Appointment_Type,Date_of_appointment,Appointment_ID,Doctor_ID,Patient_ID,END_time,Start_time))
    mydb.commit()


def edit_details_pat(new_Address, new_DOB, new_Patient_ID, new_First_name,new_Last_name,new_Gender,new_Email,new_Phone,Address,DOB,Patient_ID,First_name,Last_name,Gender,Email,Phone):
    c.execute("UPDATE patient_556 SET Address=%s,DOB=%s,Patient_ID=%s,First_name=%s,Last_name=%s,Gender=%s,Email=%s,phone=%s WHERE Address=%s and DOB=%s and Patient_ID=%s and First_name=%s and Last_name=%s and Gender=%s and Email=%s and phone=%s", (new_Address,new_DOB,new_Patient_ID,new_First_name,new_Last_name,new_Gender,new_Email,new_Phone,Address,DOB,Patient_ID,First_name,Last_name,Gender,Email,Phone))
    mydb.commit()

def edit_details_doc(new_Doctor_ID,new_Job_Type,new_First_name,new_Last_name,new_Street,new_Pincode,new_Annual_Salary,Doctor_ID,Job_type,First_name,Last_name,Street,Pincode,Annual_Salary):
    c.execute("UPDATE Doctor_556 SET Doctor_ID=%s,Job_Type=%s,First_name=%s,Last_name=%s,Street=%s,Pincode=%s,Annual_Salary=%s WHERE  Doctor_ID=%s and Job_Type=%s and First_name=%s and Last_name=%s and Street=%s and Pincode=%s and Annual_Salary=%s", (new_Doctor_ID,new_Job_Type,new_First_name,new_Last_name,new_Street,new_Pincode,new_Annual_Salary,Doctor_ID,Job_type,First_name,Last_name,Street,Pincode,Annual_Salary))
    mydb.commit()


def edit_details_Treat(new_Treatment_ID,new_Tooth,new_Medication,new_Patient_ID,new_Appointment_ID,new_Doctor_ID,Treatment_ID,Tooth,Medication,Patient_ID,Appointment_ID,Doctor_ID):
    c.execute("UPDATE Treatment_556 SET Treatment_ID=%s,Tooth=%s,Medication=%s,Patient_ID=%s,Appointment_ID=%s,Doctor_ID=%s WHERE Treatment_ID=%s and Tooth=%s and Medication=%s and Patient_ID=%s and Appointment_ID=%s and Doctor_ID=%s ", (new_Treatment_ID,new_Tooth,new_Medication,new_Patient_ID,new_Appointment_ID,new_Doctor_ID,Treatment_ID,Tooth,Medication,Patient_ID,Appointment_ID,Doctor_ID))
    mydb.commit()


def edit_details_review(new_Treatment_Description,new_Date_of_Review,new_Cleanliness,new_Communication,new_Professionalism,new_Review_ID,new_Treatment_ID,new_Doctor_ID,Treatment_Description,Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID):
    c.execute("UPDATE review_556 SET Treatment_Description=%s,Date_of_Review=%s,Cleanliness=%s,Communication=%s,Professionalism=%s,Review_ID=%s,Treatment_ID=%s,Doctor_ID=%s WHERE "
    "Treatment_Description=%s and Date_of_Review=%s and Cleanliness=%s and Communication=%s and Professionalism=%s and Review_ID=%s and Treatment_ID=%s and Doctor_ID=%s", (new_Treatment_Description,new_Date_of_Review,new_Cleanliness,new_Communication,new_Professionalism,new_Review_ID,new_Treatment_ID,new_Doctor_ID,Treatment_Description, Date_of_Review,Cleanliness,Communication,Professionalism,Review_ID,Treatment_ID,Doctor_ID))
    mydb.commit()
    

def edit_details_bill(new_Bill_ID,new_Total_amount,new_Payment_Type,new_Patient_ID,new_Payment_status,Bill_ID,Total_amount,Payment_Type,Patient_ID,Payment_status):
    c.execute("UPDATE billing_556 SET Bill_ID=%s,Total_amount=%s,Payment_Type=%s,Patient_ID=%s,Payment_status=%s WHERE Bill_ID=%s and Total_amount=%s and Payment_Type=%s and Patient_ID=%s and Payment_status=%s", (new_Bill_ID,new_Total_amount,new_Payment_Type,new_Patient_ID,new_Payment_status,Bill_ID,Total_amount,Payment_Type,Patient_ID,Payment_status))
    mydb.commit()


def delete_data_app(Appointment_ID):
    c.execute('DELETE FROM appointment_556 WHERE Appointment_ID="{}"'.format(Appointment_ID),'SET FOREIGN_KEY_CHECKS=0;')
    mydb.commit()

def delete_data_pat(Patient_ID):
    c.execute('DELETE FROM patient_556 WHERE Patient_ID="{}"'.format(Patient_ID))
    mydb.commit()

def delete_data_doc(Doctor_ID):
    c.execute('DELETE FROM doctor_556 WHERE Doctor_ID="{}"'.format(Doctor_ID),'SET FOREIGN_KEY_CHECKS=0;')
    mydb.commit()

def delete_data_treat(Treatment_ID):
    c.execute('DELETE FROM Treatment_556 WHERE Treatment_ID="{}"'.format(Treatment_ID),'SET FOREIGN_KEY_CHECKS=0;')
    mydb.commit()

def delete_data_review(Review_ID):
    c.execute('DELETE FROM review_556 WHERE Review_ID="{}"'.format(Review_ID),'SET FOREIGN_KEY_CHECKS=0;')
    mydb.commit()

def delete_data_bill(Bill_ID):
    c.execute('DELETE FROM billing_556 WHERE Bill_ID="{}"'.format(Bill_ID),'SET FOREIGN_KEY_CHECKS=0;')
    mydb.commit()

def execute_query(query1):
    try:
        x=query1.split(' ')[0].lower()
        c.execute(query1)
        if x in ['delete','update','insert']:
            mydb.commit()
        if x=='select':
            x=c.fetchall()
            df = pd.DataFrame(x) 
            with st.expander("View Info"):
                st.dataframe(df)
        st.subheader("Query run successfully")
    except:
        st.subheader("Sorry invalid query")
