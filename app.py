#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def abc():
    return {"fav_food": "Biryani"}