import telegram
import os
import random
import time
from dotenv import load_dotenv
import argparse


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    telegram_id=os.environ['TELEGRAM_ID']
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", help="Вставьте с какой переодичностью отпрвлять фотографии (в секундах)",
                        default='14400')
    args = parser.parse_args()
    periodicity = int(args.time)

    while True:

        all_files = os.walk("images")

        for array_of_files in all_files:
            folder, nested_folder, files = array_of_files
            random.shuffle(files)
            for image in files:
                path = os.path.join('images', image)
                with open(path, 'rb') as file:
                    bot.send_document(chat_id=telegram_id, document=file)
                time.sleep(5)
        time.sleep(periodicity)



