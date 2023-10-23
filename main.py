import streamlit as st
from streamlit_option_menu import option_menu
import home, tables

st.set_page_config(
    page_title="Home"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title='Pages',
                options=['Home','Tables']           
            )
        
        if app == "Home":
            home.app()
        if app == 'Tables':
            tables.app()    
                         
    run()        