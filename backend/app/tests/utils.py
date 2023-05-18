import json
import os
from dotenv import dotenv_values
from app import create_app

def login(app):
    response = login(app)
    data = json.loads(response.data)
    TOKEN = data['token']
    API_KEY = dotenv_values('.env')['API_KEY']

    return (TOKEN, API_KEY)