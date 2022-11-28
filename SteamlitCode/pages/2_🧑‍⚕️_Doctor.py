import streamlit as st
import mysql.connector
from update import updatedoc
from create import createdoc
from database import create_table
from read import readdoc
from delete import deletedoc
from update import updatedoc

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    Doctor= ["NEW Doctor","View all Doctor","Edit Doctor Info","Remove Doctor"]
    choice = st.sidebar.selectbox("Doctor Details",Doctor)

    create_table()
    if choice == "NEW Doctor":
        st.subheader("NEW Doctor")
        createdoc()

    elif choice == "View all Doctor":
        st.subheader("All Doctors")
        readdoc()

    elif choice == "Edit Doctor Info":
        st.subheader("Edit Doctor Info")
        updatedoc()

    elif choice == "Remove Doctor":
        st.subheader("Remove Doctor")
        deletedoc()
    
    else:
        st.subheader("invalid Choice")

if __name__ == '__main__':
    main()