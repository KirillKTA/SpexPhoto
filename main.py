import os
import requests
from pprint import pprint
from urllib.parse import urlparse
from os.path import splitext
from itertools import count
from datetime import datetime
import telegram

def download_image(url, image_path, params = None):
    response = requests.get(url, params = params)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)
def fetch_spacex_images():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    pprint(response.json()['links'] ['flickr'] ['original'])
    for number, link in enumerate(response.json()['links'] ['flickr'] ['original']):
        image_path = f'images/{number} spacex.jpg'
        download_image(link, image_path)
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

    os.makedirs("images",exist_ok=True)
    fetch_spacex_images()
    print(fetch_file_extension("https://apod.nasa.gov/apod/image/2211/LastRingPortrait_Cassini_4472.jpg"))
    apikey = "LvQvcg15Amfn3Pr6inxvdbjM5C5khv9sG9qJ1A78"
    fetch_nasa_opod_images(apikey)
    fetch_nasa_epic_images(apikey)
