# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:38:42 2023

@author: M
"""
import pandas as pd
import requests
import json
import time
from utils import parser

def get_page(vacancy, page = 0):
        
        params = {
                'text':f'NAME:{vacancy}',
                'page':page,
                'per_page':100
            }
        
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        
        return data



def get_req_from_json(vacancy):
    
    js_list = []
    
    for page in range(0, 20):
        
        js_obj = json.loads(get_page(vacancy, page))
        
        js_list.extend(js_obj['items'])
    
        if (js_obj['pages'] - page) <= 1:
            break
        
        time.sleep(0.25)
        
    df = pd.DataFrame(js_obj)
    items = df['items']
    items_len = len(items)
    
    req = []
    for i in range(items_len):
        req.append(parser.rem_tags(items[i]['snippet']['requirement'] + ' '+ \
                          items[i]['snippet']['responsibility']))
    
    link = []
    for i in range(items_len):
        link.append(parser.rem_tags(items[i]['alternate_url']))
    
    names = []
    for i in range(items_len):
        names.append(parser.rem_tags(items[i]['name']))
                     
          
    return {
            'reqs':req,
             'link':link,
             'names':names
             }
    
    