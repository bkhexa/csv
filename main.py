import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import qna,dataprof,qualityindex


st.set_page_config(page_title="360 Insights")

if 'uploaded_file_content' not in st.session_state:
    st.session_state.uploaded_file_content = None

Uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'],accept_multiple_files=True)
if Uploaded_file:
    st.session_state.uploaded_file_content = Uploaded_file

class MultiApp:
    def __init__(self):
        self.apps =[]
    def add_app(self, title, func):
        self.apps.append({
            "title" : title,
            "function":func
        })
    def menu():
        with st.sidebar:
            app = option_menu(
                menu_title='Section',
                options=['Quality Index', 'Data Profiling', 'CSV Chat' ],
                icons=['bi bi-clipboard2-data-fill', 'bi bi-database-fill-gear', 'bi bi-filetype-csv'],
                menu_icon='bi bi-menu-button-wide-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": '#252629'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "black"},
                    "nav-link-selected": {"background-color": "#43316D"}, }
            )
        if app=='Quality Index':
            qualityindex.app(st.session_state.uploaded_file_content)
        if app=='Data Profiling':
            dataprof.app(st.session_state.uploaded_file_content)
        if app=='CSV Chat':
            qna.app(st.session_state.uploaded_file_content)

    menu()
