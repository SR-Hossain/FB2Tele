from fb import wait_in_unread_for_new_posts
from login import login
from scrap import send_new_posts_to_telegram
# import time
from keep_alive import run


print('initiating..')
run()
login()


while True:
    while True:
        # print('sending to telegram...')
        send_new_posts_to_telegram()
        # print('sent to telegram...')
        wait_in_unread_for_new_posts()
