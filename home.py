import streamlit as st
import pandas as pd

def app():
    users = pd.read_csv("data/Users.csv")
    users.columns = ["UserID", "Name", "UserName", "Password", "Access"]

    timecodes = pd.read_csv("data/TimeCodes.csv")
    timecodes.columns = ["Code", "Description", "Merged"]
    
    single, multi = st.tabs(["Single", "Multi"])

    with single:
        st.header("Single Time Block")
        st.date_input("Date", key=1)
        st.time_input("Time", step=900)
        st.selectbox("User", options=users["Name"], key=2)
        st.selectbox("Code", options=timecodes["Merged"], key=3)
        st.button("Submit", use_container_width=True, key=7)
        st.button("Clear", use_container_width=True, key=8)

    with multi:
        st.header("Multi Time Block")
        st.date_input("Date", key=4)
        st.time_input("Start Time", step=900)
        st.time_input("End Time", step=900)
        st.selectbox("User", options=users["Name"], key=5)
        st.selectbox("Code", options=timecodes["Merged"], key=6)
        st.button("Submit", use_container_width=True, key=9)
        st.button("Clear", use_container_width=True, key=10)