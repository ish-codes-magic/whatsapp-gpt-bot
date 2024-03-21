import logging
from flask import current_app, jsonify
import json
import requests

# from app.services.openai_service import generate_response
import re
import os

from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
print(ACCESS_TOKEN)
VERSION = os.getenv("VERSION")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/media/"

data = {"file": "./property.jpeg",
        "type": "image/jpeg",
        "messaging_product": "whatsapp"
        }

response = requests.post(url=url, data=data, headers=headers, timeout=10)# 10 seconds timeout as an example

response.json()