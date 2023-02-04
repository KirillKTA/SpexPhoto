import os
import requests
from main import download_image


def fetch_spacex_images():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    for number, link in enumerate(response.json()['links'] ['flickr'] ['original']):
        image_path = os.path.join('images', f'{number} spacex.jpg')
        download_image(link, image_path)






if __name__ == '__main__':

    os.makedirs("images", exist_ok=True)
    fetch_spacex_images()