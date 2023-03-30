import os
import requests
from urllib.parse import urlparse
from os.path import splitext
from itertools import count
from datetime import datetime
import telegram
from dotenv import load_dotenv

def download_image(url, image_path, params = None):
    response = requests.get(url, params = params)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)

def fetch_file_extension(url):
    parse_url = urlparse(url)
    url_path = parse_url.path
    return splitext(url_path)[1]
