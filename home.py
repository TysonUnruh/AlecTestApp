# Import required libraries
import streamlit as st
import pandas as pd
import datetime
import csv

# Function to generate time chunks of 15 minutes between start and end times
def generate_time_chunks(start_time, end_time):
    current_time = start_time
    chunks = []

    # Continue to generate chunks until current time is less than end time
    while current_time < end_time:
        # Calculate the next chunk's time, 15 minutes ahead
        next_time = (datetime.datetime.combine(datetime.date.today(), current_time) + datetime.timedelta(minutes=15)).time()
        # Append the chunk to the list
        chunks.append((current_time, min(next_time, end_time)))
        current_time = next_time

    return chunks

# Main app function
def app():
    # Load Users data from CSV and set columns
    users = pd.read_csv("data/Users.csv")
    users.columns = ["UserID", "Name", "UserName", "Password", "Access"]

    # Load TimeCodes data from CSV and set columns
    timecodes = pd.read_csv("data/TimeCodes.csv")
    timecodes.columns = ["Code", "Description", "Merged"]

    # Create tabs for Single and Multi time block
    single, multi = st.tabs(["Single", "Multi"])

    # Define the Single Time Block tab
    with single:
        st.header("Single Time Block")
        selected_date_single = st.date_input("Date", key=1)
        selected_time = st.time_input("Time", step=900)  # 900 seconds is 15 minutes
        selected_user_single = st.selectbox("User", options=users["Name"], key=2)
        selected_code_single = st.selectbox("Code", options=timecodes["Merged"], key=3)

        # When the Submit button is clicked
        if st.button("Submit", use_container_width=True, key=7):
            user_id_single = f"{users[users['UserName'] == selected_user_single]['UserID'].iloc[0]:03}"
            code_single = selected_code_single.split('-')[0]

            # Append the selected values to the Timesheet.csv
            with open('data/Timesheet.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([selected_date_single, selected_time, code_single, user_id_single])

            st.write(f"{selected_date_single}, {selected_time}, {selected_code_single}, {selected_user_single}")

    # Define the Multi Time Block tab
    with multi:
        st.header("Multi Time Block")
        selected_date = st.date_input("Date", key=4)
        start_time = st.time_input("Start Time", step=900)
        end_time = st.time_input("End Time", step=900)

        # Check if the end time is before the start time and show an error
        if end_time <= start_time:
            st.error("End Time should be greater than Start Time!")
        else:
            selected_user = st.selectbox("Person", options=users["UserName"], key=5)
            selected_code = st.selectbox("Code", options=timecodes["Merged"], key=6)

            # When the Submit button is clicked
            if st.button("Submit", use_container_width=True, key=9):
                # Generate the time chunks for the given range
                time_chunks = generate_time_chunks(start_time, end_time)

                # Append each time chunk to the Timesheet.csv
                with open('data/Timesheet.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for chunk in time_chunks:
                        time = chunk[1]
                        code = selected_code.split('-')[0]
                        user_id = f"{users[users['UserName'] == selected_user]['UserID'].iloc[0]:03}"
                        writer.writerow([selected_date, time, code, user_id])

                # Display each chunk on the streamlit app
                for chunk in time_chunks:
                   st.write(f"{selected_date}, {chunk[1]}, {selected_code}, {selected_user}")
