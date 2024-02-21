import requests
import os
from dotenv import load_dotenv
import logging
import json

logging.basicConfig(level=logging.INFO)

api_key = os.getenv("RAPID_API_KEY")
