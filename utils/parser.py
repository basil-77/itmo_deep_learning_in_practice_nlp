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

# Define the function to extract key details from a PDF resume
def extract_resume_details(pdf_file):
    """Extracts key details from a PDF resume.

    Args:
        pdf_file: The path to the PDF resume file.

    Returns:
        A dictionary containing the extracted key details, including:
            category: The job role of the candidate.
            skills: A list of the candidate's skills.
            education: A list of the candidate's educational qualifications.
    """

    # Extract the text from the PDF file
    with open(pdf_file, "rb") as f:
        text = extract_text_from_pdf(pdf_file)

    # Parse the text to extract the key details
    role = text.split("\n")[0]
    
    search = r'Желаемая должность и зарплата((?:(?!Опыт работы|Ключевые навыки|Дополнительная информация|Образование).)+)'
    search_match = re.search(search, text, re.DOTALL | re.IGNORECASE)
    if search_match:
        search = search_match.group(1).strip()
    else:
        search = None
    
    expirience = r'Опыт работы((?:(?!Ключевые навыки|Дополнительная информация|Образование).)+)'
    expirience_match = re.search(expirience, text, re.DOTALL | re.IGNORECASE)
    if expirience_match:
        expirience = expirience_match.group(1).strip()
    else:
        expirience = None
        
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
    
    # Return the extracted key details
    return {
        #"text":text
        "role": role,
        "search": search,
        "expirience": expirience,
        "education": education,
        "skills": skills
    }