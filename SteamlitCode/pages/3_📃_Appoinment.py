import streamlit as st
import mysql.connector
from create import createapp
from database import create_table
from read import readapp
from delete import deleteapp
from update import updateapp

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    Appointment= ["Create Appointment","View all Appointments", "Edit Appointment","Cancel Appointment"]
    choice = st.sidebar.selectbox("Appointment Details", Appointment)

    create_table()
    if choice == "Create Appointment":
        st.subheader("Create an Appointment")
        createapp()

    elif choice == "View all Appointments":
        st.subheader("All Appointments")
        readapp()

    elif choice == "Edit Appointment":
        st.subheader("Edit Appointment")
        updateapp()

    elif choice == "Cancel Appointment":
        st.subheader("Cancel Appointment")
        deleteapp()

    else:
        st.subheader("Invalid choice")

if __name__ == '__main__':
    main()