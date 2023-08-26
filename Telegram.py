import telegram
import os
import random
import time
from dotenv import load_dotenv
import argparse


if __name__ == '__main__':
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    telegram_id = os.environ['TELEGRAM_ID']
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=int,
                        help="Вставьте с какой периодичностью "
                             "отправлять фотографии (в секундах)",
                        default='14400')
    folder = os.getenv("FOLDER")
    args = parser.parse_args()

    while True:
        all_files = os.walk(folder)

        for array_of_files in all_files:
            folder_name, nested_folder, files = array_of_files
            random.shuffle(files)
            for image in files:
                path = os.path.join(folder_name, image)
                try:
                    with open(path, 'rb') as file:
                        bot.send_document(chat_id=telegram_id, document=file)
                except telegram.error.NetworkError:
                    print("соединение прервано")
                    time.sleep(5)
        time.sleep(args.time)
