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
from utils import cosine

RESUME_PATH = 'resumes'

def main():

    st.set_page_config(
        page_title="demo",
        page_icon="🚘",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    column1, column2 = st.columns([9,1])

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
                
    
        with column1:
            start = st.button('start')
            if start:
                file_pdf = os.path.join(f'{RESUME_PATH}', download_pdf.name)
                parsed_pdf = parser.extract_resume_details(file_pdf)
                #st.write(parsed_pdf)
                resume_compare_info = parsed_pdf['experience'] \
                                                [:512]+parsed_pdf['skills']
                res = summarize.summarize_res(resume_compare_info)
                
                
                st.write('Подходящая должность: ' + res)
                
                vac_info = api.get_req_from_json(res)
                
                cos = []
                
                for req in vac_info['reqs']:
                    cos.append(cosine.vectorize([resume_compare_info, req]))
                names, links = cosine.compare_vac_cos(vac_info['names'], \
                                               vac_info['link'],cos)
                vacancy = []
                for key, value in names.items():
                    vacancy.append(key)
                    
                vac_links = []
                for key, value in links.items():
                    vac_links.append(key)
                    
                vacancy_len = len(vacancy)
                
                
                
                table = {
                        'Название вакансии':vacancy,
                        'Ссылка':vac_links[:vacancy_len],
                        'Score':list(map(lambda x: "{:.2%}".format(x),\
                                         names.values()))
                    }
                
                result = pd.DataFrame(table)
                
                

                del names
                del links
                
                st.write('Вакансии с hh.ru:')
                st.dataframe(result, \
                             column_config=
                             {"Ссылка":st.column_config.LinkColumn()}
                             )
                
    except Exception as e:
        st.sidebar.error('Файл не выбран')

if __name__ == "__main__":
    main()