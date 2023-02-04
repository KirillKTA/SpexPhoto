import os
import requests
from main import download_image
from main import fetch_file_extension
from dotenv import load_dotenv


def fetch_nasa_opod_images(apikey):

    payload = {"api_key": apikey, "count": 30, }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    for number, link in enumerate(response.json()):
        if link ["media_type"]!="image":
            continue
        image_path = os.path.join('images', f'{number} nasa.jpg')
        download_image(link["hdurl"], image_path, params = payload)






if __name__ == '__main__':

    load_dotenv()
    os.makedirs("images",exist_ok=True)
    print(fetch_file_extension("https://apod.nasa.gov/apod/image/2211/LastRingPortrait_Cassini_4472.jpg"))
    apikey = os.getenv('NASA_APIKEY')
    fetch_nasa_opod_images(apikey)