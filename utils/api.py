# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:38:42 2023

@author: M
"""
import pandas as pd
import requests
import json
import time
import streamlit as st

def get_page(page = 0):
        
        params = {
                'text':'NAME:Аналитик',
                'page':page,
                'per_page':100
            }
        
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        
        return data



def get_json():
    
    js_list = []
    
    for page in range(0, 20):
        
        js_obj = json.loads(get_page(page))
        
        js_list.extend(js_obj['items'])
    
        if (js_obj['pages'] - page) <= 1:
            break
        
        time.sleep(0.25)
        
    df = pd.DataFrame(js_obj)
    return df
    
    