import streamlit as st
import mysql.connector
from create import createbill
from database import create_table
from read import readbill
from delete import deletebill
from update import updatebill

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    Bill= ["Create Bill","View all Bills","Edit Bill","Delete Bill"] 
    choice = st.sidebar.selectbox("Bill Details", Bill)

    create_table()
    if choice == "Create Bill": 
        st.subheader("Create new Bill")
        createbill()

    elif choice == "View all Bills":
        st.subheader("View all the Bills")
        readbill()

    elif choice == "Edit Bill":
        st.subheader("Edit Bill Info")
        updatebill()

    elif choice == "Delete Bill":
        st.subheader("Delete all Bills")
        deletebill()
    
    else: 
        st.subheader("Invalid choice")


if __name__ == '__main__':
    main()