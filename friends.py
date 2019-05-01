from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, go_left, go_right, look_for_button
import pyautogui
import time
import settings


friend_currency = 'imgs/friend_currency.PNG'
friend_send = 'imgs/friend_send.PNG'
friend_gifts = 'imgs/friend_gifts.PNG'
friend_gift_send = 'imgs/friend_gift_send.PNG'
friend_collect = 'imgs/friend_collect.PNG'
friend_thank = 'imgs/friend_thank.PNG'
friend_gold = 'imgs/friend_gold.PNG'

facebook_send = 'imgs/facebook_send.PNG'


def check_friends():
    log("Checking friends")
    heart = pyautogui.locateOnScreen('imgs/friend_currency.PNG', confidence=0.88)
    if heart is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/friend_currency.png', "Friend Heart", give_friend_currency)
    else:
        click_on_box(heart)
        give_friend_currency()


def give_friend_currency():
    time.sleep(2)
    click_image(friend_send, "Send Button", wait)
    time.sleep(4)
    click_image(facebook_send, "Facebook send button", wait)


def wait():
    time.sleep(1)