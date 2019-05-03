import datetime

from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check
import pyautogui
import time
import settings

mailbox_receive = 'imgs/mailbox_receive.PNG'

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run


def check_mailbox():
    global last_check
    if delay_next_check(5, last_check):
        return
    last_check = datetime.datetime.now()
    log("Checking mail")
    mailbox = pyautogui.locateOnScreen('imgs/mailbox_available.png', confidence=0.85)
    if mailbox is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/mailbox_available.png', "Mailbox", open_mailbox)
    else:
        click_on_box(mailbox)
        open_mailbox()


def open_mailbox():
    time.sleep(1)
    reward = pyautogui.locateOnScreen('imgs/mailbox_receive.png', confidence=0.75)
    if reward is not None:
        log("Receiving mail")
        click_on_box(reward)
        time.sleep(1)
        escape(2)
    else:
        log("No mail available")
        escape(1)