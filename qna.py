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


uploaded =  st.session_state.uploaded_file_content
def app(uploaded):

    def agent_csv(uploaded):
        uploaded =  st.session_state.uploaded_file_content
        path_1 = str(uploaded[0].name)
        path_2 = str(uploaded[1].name)
        llm = AzureOpenAI(deployment_name="testing",token=100, model_name="text-davinci-003")
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
            """
                For the following query, if it requires drawing a table, reply as follows:
                {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

                If the query requires creating a bar chart, reply as follows:
                {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
                
                If the query requires creating a line chart, reply as follows:
                {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
                
                There can only be two types of chart, "bar" and "line".
                
                If it is just asking a question that requires neither, reply as follows:
                {"answer": "answer"}
                Example:
                {"answer": "The title with the highest rating is 'Gilead'"}
                
                If you do not know the answer, reply as follows:
                {"answer": "I do not know."}
                
                Return all output as a string.
                
                All strings in "columns" list and data list, should be in double quotes,
                
                For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}
                
                Lets think step by step.
                
                Below is the query.
                Query: 
                """
            + query
        )
        response = agent.run(prompt)
        return response.__str__()


    query = st.text_area("Insert your query")
    
    if st.button("Submit Query", type="primary"):
        # Create an agent from the CSV file.
        agent = agent_csv(uploaded)

        # Query the agent.
        response = query_agent(agent=agent, query=query)
        st.write(response)
