import telegram
import os
import random
import time
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    while True:
        images = os.listdir("images")
        random_image = random.choice(images)
        image_path = os.path.join("images", random_image)
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=os.environ['TELEGRAM_ID'], photo=photo)
        time.sleep(14400)



