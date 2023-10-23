import streamlit as st
import pandas as pd

def app():
    users = pd.read_csv("data/Users.csv")
    st.header("Users")
    st.dataframe(users, hide_index=True)

    timecodes = pd.read_csv("data/TimeCodes.csv")
    st.header("TimeCodes")
    st.dataframe(timecodes, hide_index=True)

    payrates = pd.read_csv("data/PayRates.csv")
    st.header("PayRates")
    st.dataframe(payrates, hide_index=True)

    timesheet = pd.read_csv("data/Timesheet.csv")
    st.header("Timesheet")
    st.dataframe(timesheet, hide_index=True)