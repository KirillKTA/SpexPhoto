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







if __name__ == '__main__':

    load_dotenv()
    os.makedirs("images",exist_ok=True)
    fetch_spacex_images()
    apikey =  os.getenv('NASA_APIKEY')
    fetch_nasa_opod_images(apikey)
    fetch_nasa_epic_images(apikey)
