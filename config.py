# config.py
from dotenv import load_dotenv
import os

load_dotenv()

def load_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not found in .env")
    return key
