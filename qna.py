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



os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = "https://demo-kart.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "be87738133984fa8ba4b5458ce5b1af7"

try:
        
    # uploaded =  st.session_state.uploaded_file_content
    def app(uploaded):

        def agent_csv():
            # uploaded =  st.session_state.uploaded_file_content
            path_1 = str(uploaded[0].name)
            path_2 = str(uploaded[1].name)
            llm = AzureOpenAI(deployment_name="testing", model_name="text-davinci-003")
            csv_agent = create_csv_agent(llm, [path_1, path_2], verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True)
            return csv_agent



        def query_agent(agent, query):
            """
            Query an agent and return the response as a string.

            Args:
                agent: The agent to query.
                query: The query to ask the agent.

            Returns:
                The response from the agent as a string.
            """

            prompt = (
                """Given two uploaded CSV files, file1.csv and file2.csv, it is imperative that you accurately retrieve the answer to the query. Follow these steps meticulously:

                Thorough Column Identification:

                Begin by scanning every header in both file1.csv and file2.csv.
                Identify all column names that are common to both files. Ensure you account for variations in case, spacing, or special characters.
                Exhaustive Search in the First File:

                Using each of the common columns identified in step 1, systematically search for the query's answer in file1.csv.
                Examine every row, ensuring no data is overlooked.
                If the answer is located, extract and return the relevant rows from file1.csv immediately.
                Comprehensive Search in the Second File:

                Only if the answer was not located in file1.csv, proceed to file2.csv.
                Again, using each of the common columns, search every row in file2.csv for the query's answer.
                If found, extract and return the relevant rows.
                Validation:

                After searching both files, cross-check to ensure no rows were missed or overlooked.
                Validate that the data extracted aligns with the query's requirements.
                Final Response:

                If the answer is located in either file, present it clearly and concisely.
                If, after thorough searching, the answer is not found in either file, explicitly state: 'The answer to the query is not present in the provided files after exhaustive search.'
                """
                
                # """
                #     step 1: look for common column name in both uploaded files 
                #     step 2: search for the answer in first file and so on 
                #     step 3: if answer is not there in first file then search for the same in second file using common column
                #     """
                + query
            )
            response = agent.run(prompt)
            return response.__str__()

        
        query = st.text_area("Insert your query")
           
        if st.button("Submit Query", type="primary"):
            if query: 
                # Create an agent from the CSV file.
                agent = agent_csv()

                # Query the agent.
                response = query_agent(agent=agent, query=query)
                st.write(response)
            else:
                st.info('Please shoot up with your question', icon="ℹ️")

except:
    st.info('Please Upload a file before shooting with query', icon="ℹ️")