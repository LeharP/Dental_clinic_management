import streamlit as st
import mysql.connector
import pandas as pd
from database import execute_query 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()

def run():
    query1=st.text_input('Enter a Query')
    if st.button("Run query"):
        execute_query(query1)

def main():
    run()

if __name__ == '__main__':
    main()