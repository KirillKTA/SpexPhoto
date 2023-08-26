import requests
from tools import download_image
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id',
                        default="5eb87d47ffd86e000604b38a",
                        help='свой launch_id')
    args = parser.parse_args()
    launch_id = args.launch_id
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}/'
    response = requests.get(url)
    response.raise_for_status()
    for number, link in enumerate(response.json()['links']
                                  ['flickr']['original']):
        image_path = f'{number} spacex.jpg'
        download_image(link, image_path)


if __name__ == '__main__':
    main()
