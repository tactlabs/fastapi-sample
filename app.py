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

'''
    http://127.0.0.1:8000/
'''
@app.get("/")
async def abc():
    return {"fav_food": "Biryani"}

'''
    http://127.0.0.1:8000/city?name=chennai
'''
@app.get("/city")
def get_city(name: str):

    _dict = {
        "name" : name
    }

    return _dict


'''
    http://127.0.0.1:8000/city/chennai/
'''
@app.get("/city/{name}")
def get_city_pathvariable(name: str):

    _dict = {
        "path_name" : name
    }

    return _dict

# Post username


'''
    http://127.0.0.1:8000/city/xyz?name=hyd
    POST
'''
@app.post("/city/xyz")
def post_city_name(name: str):

    _dict = {
        "xyz_name" : name
    }

    return _dict