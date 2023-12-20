# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:33:20 2023

@author: M
"""

import PyPDF2 
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


def extract_resume_details(pdf_file):
   

    
    with open(pdf_file, "rb") as f:
        text = extract_text_from_pdf(pdf_file)

    
    role = text.split("\n")[0]
    
    search = r'Желаемая должность и зарплата((?:(?!Опыт работы|Ключевые навыки|Дополнительная информация|Образование).)+)'
    search_match = re.search(search, text, re.DOTALL | re.IGNORECASE)
    if search_match:
        search = search_match.group(1).strip()
    else:
        search = None
    
    experience = r'Опыт работы((?:(?!Ключевые навыки|Дополнительная информация|Образование).)+)'
    experience_match = re.search(experience, text, re.DOTALL | re.IGNORECASE)
    if experience_match:
        experience = experience_match.group(1).strip()
    else:
        experience = None
        
    education = r'Образование((?:(?!Ключевые навыки|Навыки).)+)'
    education_match = re.search(education, text, re.DOTALL | re.IGNORECASE)
    if education_match:
        education = education_match.group(1).strip()
    else:
        education = None
        
    skills = r'Ключевые навыки((?:(?!Дополнительная информация).)+)'
    skills_match = re.search(skills, text, re.DOTALL | re.IGNORECASE)
    if skills_match:
        skills = skills_match.group(1).strip()
    else:
        skills = None
    
    
    return {
        #"text":text
        "role": role,
        "search": search,
        "experience": experience,
        "education": education,
        "skills": skills
    }