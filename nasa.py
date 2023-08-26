import os
import requests
from dotenv import load_dotenv
from tools import download_image
from urllib.parse import urlparse
from os.path import splitext
import argparse


def fetch_file_extension(url):
    parse_url = urlparse(url)
    url_path = parse_url.path
    return splitext(url_path)[1]


def main():
    nasa_api_token = os.environ['NASA_APIKEY']
    parser = argparse.ArgumentParser(description='Скачивает'
                                                 ' картинки с nasa_apod в'
                                                 ' папку images.')
    parser.add_argument('--count', help='количество', type=int, default=5)

    args = parser.parse_args()
    count = args.count
    payload = {
        "api_key": nasa_api_token,
        "count": count
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for number, api_response in enumerate(response.json(), start=1):
        link = api_response['url']
        extension = fetch_file_extension(link)
        if extension:
            full_name = f'nasa_{number}{extension}'
            download_image(link, full_name)


if __name__ == '__main__':
    main()
