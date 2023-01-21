import os
import requests
from pprint import pprint
from urllib.parse import urlparse
from os.path import splitext
from main import download_image


def fetch_nasa_opod_images(apikey):

    payload = {"api_key": apikey, "count": 30, }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    pprint(response.json())
    for number, link in enumerate(response.json()):
        if link ["media_type"]!="image":
            continue
        image_path = f'images/{number} nasa.jpg'
        download_image(link["hdurl"], image_path, params = payload)
def fetch_file_extension(url):
    parse_url = urlparse(url)
    url_path = parse_url.path
    return splitext(url_path)[1]





if __name__ == '__main__':

    os.makedirs("images",exist_ok=True)
    print(fetch_file_extension("https://apod.nasa.gov/apod/image/2211/LastRingPortrait_Cassini_4472.jpg"))
    apikey = "LvQvcg15Amfn3Pr6inxvdbjM5C5khv9sG9qJ1A78"
    fetch_nasa_opod_images(apikey)