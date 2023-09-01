import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
from pandas_profiling import ProfileReport



def app(uploaded_files):
    try:

        st.markdown("<h1 style='text-align: center; color: white;'> ▤  Data Profiling </h1>",
                    unsafe_allow_html=True)

        st.markdown(
            f'''
            <div style="display: inline-block; text-align: left width: 33%;">
                <span style="font-size: 40px; font-weight: bold;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;90%&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;80%&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MLF</span><br>
                <span style="font-size: 20px;">Data Quality Index&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ML Readiness&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

        tab1, tab2 = st.tabs([uploaded_files[0].name, uploaded_files[1].name ])
        with tab1:
            path_1 = str(uploaded_files[0].name)
            df = pd.read_csv(path_1)
            st.write(df.head())
            profile = ProfileReport(df)
            st_profile_report(profile,key=0)
            st.write(df.describe())
            st.write('sucessfully Completed first file')

        st_profile_report(profile)

        with tab2:
            path_2 = str(uploaded_files[1].name)
            df = pd.read_csv(path_2)
            st.write(df.head())
            profile = ProfileReport(df)
            st_profile_report(profile,key=1)
            st.write('sucessfully Completed second file')
        st_profile_report(profile)
    except:
        st.warning("Upload file to work on...")

