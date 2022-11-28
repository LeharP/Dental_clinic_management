import streamlit as st
import mysql.connector
from create import createpat
from database import create_table
from read import readpat
from delete import deletepat
from update import updatepat

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    st.title("Dental clinic Management system")
    Patient= ["Admit Patient","View all patients","Edit Patient Info","Discharge Patients" ]
    choice = st.sidebar.selectbox("Patient Details", Patient)

    create_table()
    if choice == "Admit Patient":
        st.subheader("Admit Patient")
        createpat()

    elif choice == "View all patients":
        st.subheader("All Patients")
        readpat()

    elif choice == "Edit Patient Info":
        st.subheader("Edit Patient Info")
        updatepat()

    else: 
        st.subheader("Discharge Patients")
        deletepat()


if __name__ == '__main__':
    main()