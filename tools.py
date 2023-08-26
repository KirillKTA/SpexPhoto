import requests
from urllib.parse import urlparse
from os.path import splitext
import os
from dotenv import load_dotenv


def download_image(url, image_path, params=None):
    folder = os.getenv("FOLDER")
    os.makedirs(folder, exist_ok=True)
    full_name = os.path.join(folder, image_path)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(full_name, 'wb') as file:
        file.write(response.content)


def fetch_file_extension(url):
    persed_url = urlparse(url)
    url_path = persed_url.path
    return splitext(url_path)[1]

if __name__ == '__main__':
    load_dotenv()