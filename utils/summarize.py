# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:53:11 2023

@author: M
"""

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


MODEL_NAME = 'basil-77/rut5-base-absum-hh'
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)


def summarize_text(text, model, tokenizer, num_beams=5):
    # Preprocess the text
    inputs = tokenizer.encode(
        "summarize: " + text,
        return_tensors='pt',
        max_length=1024,
        truncation=True
    )
 
    # Generate the summary
    summary_ids = model.generate(
        inputs,
        max_length=64,
        num_beams=num_beams,
        # early_stopping=True,
    )
 
    # Decode and return the summary
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


def summarize_res(text):
    model_ = model.to('cpu')
    summary = summarize_text(text=text,
                  model=model_,
                  tokenizer=tokenizer) 
    return summary







