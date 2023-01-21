import os
import requests
from pprint import pprint
from urllib.parse import urlparse
from os.path import splitext
from main import download_image

def fetch_spacex_images():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    pprint(response.json()['links'] ['flickr'] ['original'])
    for number, link in enumerate(response.json()['links'] ['flickr'] ['original']):
        image_path = f'images/{number} spacex.jpg'
        download_image(link, image_path)
def fetch_file_extension(url):
    parse_url = urlparse(url)
    url_path = parse_url.path
    return splitext(url_path)[1]





if __name__ == '__main__':

    os.makedirs("images", exist_ok=True)
    fetch_spacex_images()