import os
import requests
from datetime import datetime
from tools import download_image
from dotenv import load_dotenv


def fetch_nasa_epic_images(apikey):

    payload = {"api_key": apikey, }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payload)
    response.raise_for_status()
    for number, link in enumerate(response.json()):
        image_path = f'{number} epic.jpg'
        date = datetime.fromisoformat(link["date"])
        date = date.strftime("%Y/%m/%d")
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{link['image']}.png"
        download_image(image_link, image_path, params=payload)


if __name__ == '__main__':

    load_dotenv()
    apikey = os.environ['NASA_APIKEY']
    fetch_nasa_epic_images(apikey)
