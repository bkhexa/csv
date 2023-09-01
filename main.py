import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import qna,dataprof,qualityindex
import streamlit as st
import os
from langchain.llms import AzureOpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
import json
from tempfile import NamedTemporaryFile
import json.decoder
import base64
from langchain.agents import create_csv_agent
from langchain.agents.agent_types import AgentType
#########################################################################
st.set_page_config(page_title="360 Insights")


##########################azure key#######################

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = "https://demo-kart.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "be87738133984fa8ba4b5458ce5b1af7"
########################### UPLOAD BUTTON
if 'uploaded_file_content' not in st.session_state:
    st.session_state.uploaded_file_content = None

Uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'],accept_multiple_files=True)
if Uploaded_file:
    st.session_state.uploaded_file_content = Uploaded_file

############################# FILE NAME
# path_1 = str(Uploaded_file[0].name)


####################### SECTION STATE
# Check if you've already initialized the data
# if 'df' not in st.session_state:
#     # Get the data if you haven't
#     df = pd.read_csv('.csv')
#     # Save the data to session state
#     st.session_state.df = df
#
# # Retrieve the data from session state
# df = st.session_state.df





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
                default_index=1,
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
