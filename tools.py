import requests
from urllib.parse import urlparse
from os.path import splitext
import os


def download_image(url, image_path, params = None):
    os.makedirs("images", exist_ok=True)
    full_name = os.path.join('images', image_path)
    response = requests.get(url, params = params)
    response.raise_for_status()
    with open(full_name, 'wb') as file:
        file.write(response.content)


def fetch_file_extension(url):
    parse_url = urlparse(url)
    url_path = parse_url.path
    return splitext(url_path)[1]
