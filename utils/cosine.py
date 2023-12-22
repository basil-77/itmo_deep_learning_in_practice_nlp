# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 14:45:36 2023

@author: M
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(comparing):
    
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(comparing)
    cosine = cosine_similarity(matrix)

    return cosine[0,1]

def compare_vac_cos(vac_name, vac_link, cos):
    names = {}
    links = {}
    cos_len = len(cos)
    for i in range(cos_len):
        names[vac_name[i]] = cos[i]
        links[vac_link[i]] = cos[i]
        
    sort_vac_names = dict(sorted(names.items(), \
                                 key=lambda kv: kv[1], reverse = True))
    sort_vac_links = dict(sorted(links.items(), \
                                 key=lambda kv: kv[1], reverse = True))
    
    return sort_vac_names, sort_vac_links
    