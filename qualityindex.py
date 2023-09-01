import streamlit as st
import pandas as pd


def app(uploaded_files):
    # try:
       
      st.markdown("<h1 style='text-align: center; color: white;'>:: CSV Data Quality Index :: </h1>", unsafe_allow_html=True)

      def index_comple():
        for j in range(2):
          path_1 = str(uploaded_files[j].name)
          df = pd.read_csv(path_1)
          total_column = len(df.columns)
          count = 0
          for i in df.columns:
            if df[i].isnull().sum() == 0:
              pass
            else:
              count = count + 1
          comp_index_cal = round((count / total_column) * 100,2)

          ### DUPLICATE INDEX
          path_1 = str(uploaded_files[j].name)
          df = pd.read_csv(path_1)
          duplicate_value = df.duplicated(keep=False).sum()
          total_rows = df.shape[0]
          dupli_index = round((duplicate_value / total_rows) * 100,2)


          st.markdown(f'<span style="font-size:30px ;"> **》 Index for {str(uploaded_files[j].name)}** </span>',unsafe_allow_html=True)
          st.markdown(f'<span style="font-size:25px ;"> Completness Index : **:violet[{comp_index_cal} %]**</span>',
                      unsafe_allow_html=True)
          st.markdown(f'<span style="font-size:17px ;"> _(Defination: It quantifies the proportion of complete data points in relation to the total expected data points)_</span>',
                      unsafe_allow_html=True)
          st.markdown(f'<span style="font-size:25px ;"> Duplicate Index : **:violet[{dupli_index} %]**</span>',
                      unsafe_allow_html=True)
          st.markdown(
              f'<span style="font-size:17px ;"> _(Defination: It calculates the ratio of duplicate records to the total number of records in the datset)_</span>',
              unsafe_allow_html=True)
          st.markdown("***")

        return 
      try:
        if st.button('Check Index'):
          index_comple()
      except:
        st.info('Please Upload file to process', icon="ℹ️")
    # st.write('Sucessfully Completed')
