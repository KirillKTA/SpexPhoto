import os
import requests
from pprint import pprint
from urllib.parse import urlparse
from os.path import splitext
from itertools import count
from datetime import datetime
from main import download_image

def fetch_nasa_epic_images(apikey):

    payload = {"api_key": apikey,}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payload)
    response.raise_for_status()
    pprint(response.json())
    for number, link in enumerate(response.json()):
        image_path = f'images/{number} epic.png'
        date = datetime.fromisoformat(link["date"])
        date = date.strftime("%Y/%m/%d")
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{link['image']}.png"
        download_image(image_link, image_path, params=payload)
def fetch_file_extension(url):
    parse_url = urlparse(url)
    url_path = parse_url.path
    return splitext(url_path)[1]





if __name__ == '__main__':

    os.makedirs("images", exist_ok=True)
    apikey = "LvQvcg15Amfn3Pr6inxvdbjM5C5khv9sG9qJ1A78"
    fetch_nasa_epic_images(apikey)