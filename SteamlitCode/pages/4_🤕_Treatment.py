import streamlit as st
import mysql.connector
from create import createtreat
from database import create_table
from read import readtreat
from delete import deletetreat
from update import updatetreat

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    Treatment= ["New Treatment","View all Treatments","Change Treatment","Cancel Treatment"]
    choice = st.sidebar.selectbox("Treatment Details",Treatment)

    create_table()
    if choice == "New Treatment":
        st.subheader("New Treatment")
        createtreat()

    elif choice == "View all Treatments":
        st.subheader("All Treatments")
        readtreat()

    elif choice == "Change Treatment":
        st.subheader("Change Treatment")
        updatetreat()

    elif choice == "Cancel Treatment":
        st.subheader("Cancel Treatment")
        deletetreat()

    else: 
        st.subheader("Invalid Choice")

if __name__ == '__main__':
    main()