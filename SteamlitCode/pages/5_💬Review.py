import streamlit as st
import mysql.connector
from create import createreview
from database import create_table
from read import readreview
from delete import deletereview
from update import updatereview

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def main():
    Review= ["New Review","View all Reviews","Edit Review","Delete Review"]
    choice = st.sidebar.selectbox("Review Details",Review)

    create_table()
    if choice == "New Review":
        st.subheader("Add a Review")
        createreview()

    elif choice == "View all Reviews":
        st.subheader("All Reviews")
        readreview()

    elif choice == "Edit Review":
        st.subheader("Edit Review")
        updatereview()

    elif choice == "Delete Review":
        st.subheader("Delete Review")
        deletereview()

    else: 
        st.subheader("Invalid choice")

if __name__ == '__main__':
    main()