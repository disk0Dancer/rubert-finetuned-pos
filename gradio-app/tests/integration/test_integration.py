import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
headers = {"Authorization": f"Bearer {AUTH_TOKEN}"} 


def test_api():
    responce = requests.post(API_URL, headers=headers, json='{"существительное"}')
    assert responce.status_code > 0

