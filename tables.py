# Import required libraries
import streamlit as st
import pandas as pd

# Main app function to display various datasets
def app():
    # Load and display Users data
    users = pd.read_csv("data/Users.csv")  # Read Users data from CSV
    st.header("Users")  # Display a header for Users data
    st.dataframe(users, hide_index=True)  # Display the Users dataframe and hide the index

    # Load and display TimeCodes data
    timecodes = pd.read_csv("data/TimeCodes.csv")  # Read TimeCodes data from CSV
    st.header("TimeCodes")  # Display a header for TimeCodes data
    st.dataframe(timecodes, hide_index=True)  # Display the TimeCodes dataframe and hide the index

    # Load and display PayRates data
    payrates = pd.read_csv("data/PayRates.csv")  # Read PayRates data from CSV
    st.header("PayRates")  # Display a header for PayRates data
    st.dataframe(payrates, hide_index=True)  # Display the PayRates dataframe and hide the index

    # Load and display Timesheet data
    timesheet = pd.read_csv("data/Timesheet.csv")  # Read Timesheet data from CSV
    st.header("Timesheet")  # Display a header for Timesheet data
    st.dataframe(timesheet, hide_index=True)  # Display the Timesheet dataframe and hide the index