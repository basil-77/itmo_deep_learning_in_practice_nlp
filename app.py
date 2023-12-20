# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:23:55 2023

@author: M
"""

import streamlit as st
import os
import pandas as pd
from utils import api
from utils import parser
from utils import summarize



#TestModel = SignDetection(f"{os.getcwd()}\\utils_model\\best.pt", [], [],\
                          #f"{os.getcwd()}\\pngs\\drawable")

RESUME_PATH = 'resumes'

def main():

    st.set_page_config(
        page_title="demo",
        page_icon="🚘",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    column1, column2 = st.columns([5, 5])

    try:
        with st.sidebar:

            st.title("Загрузить файл")
 
            download_pdf = st.sidebar.file_uploader(
                label="Загрузка резюме (pdf)", type="pdf", accept_multiple_files=False
            )
            with open(
                os.path.join(f"{RESUME_PATH}", download_pdf.name), "wb"
            ) as f:
                f.write(download_pdf.getbuffer())
                
    except Exception as e:
        st.sidebar.error("Файл не выбран")
    
    with column1:
        start = st.button('start')
        if start:
            file_pdf = os.path.join(f'{RESUME_PATH}', download_pdf.name)
            parsed_pdf = parser.extract_resume_details(file_pdf)
            #st.write(parsed_pdf)
            res = summarize.summarize_res(parsed_pdf['experience'][:512]+parsed_pdf['skills'])
            st.write(res)
            
            data = api.get_json(res)
            st.dataframe(data)

if __name__ == "__main__":
    main()