import telegram
import os
import random
import time
bot = telegram.Bot(token='5823784180:AAHL1T2FzO4wmGG_2KJD4_C-6f24MMb8U10')
while True:
    images = os.listdir("images")
    random_image = random.choice(images)
    image_path = os.path.join("images",random_image)
    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id='-1001501906446', photo=photo)
    time.sleep(14400)

