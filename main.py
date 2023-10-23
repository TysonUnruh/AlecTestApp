# Import required libraries and modules
import streamlit as st
from streamlit_option_menu import option_menu
import home, tables

# Set the configuration for the Streamlit page
st.set_page_config(
    page_title="Home"  # Set the browser title bar
)

# Define a class to manage multiple Streamlit apps/pages
class MultiApp:
    def __init__(self):
        self.apps = []  # Initialize an empty list to store apps

    # Method to add a new app/page to the list
    def add_app(self, title, func):
        self.apps.append({
            "title": title,  # Page title
            "function": func  # Corresponding function to run the app/page
        })

    # Define a method to run the selected app/page
    def run():
        # Create an option menu in the Streamlit sidebar
        with st.sidebar:        
            app = option_menu(
                menu_title='Pages',  # Sidebar menu title
                options=['Home','Tables']  # List of pages/apps available
            )
        
        # Check which page/app is selected and run the corresponding function
        if app == "Home":
            home.app()
        if app == 'Tables':
            tables.app()    

    # Execute the run method to display the selected app/page
    run()  
