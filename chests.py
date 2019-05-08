import datetime
from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check
import pyautogui
import time
import settings

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_chests():
    global last_check
    if not settings.chests:
        return
    if delay_next_check(5, last_check):
        return
    last_check = datetime.datetime.now()
    log("Checking Chests")
    chest = pyautogui.locateOnScreen('imgs/chestavailable.png', confidence=0.85)
    if chest is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/chestavailable.png', "Chest", open_chests)
    else:
        click_on_box(chest)
        open_chests()


def open_chests():
    time.sleep(1)
    wood_chest = pyautogui.locateOnScreen('imgs/freewoodchest.png', confidence=0.75)
    precious_chest = pyautogui.locateOnScreen('imgs/free_precious.png', confidence=0.75)
    if wood_chest is not None:
        log("Opening wooden chest")
        click_on_box(wood_chest)
        time.sleep(4)
        escape(1)
        open_chests()
    elif precious_chest is not None:
        log("Opening precious chest")
        click_on_box(precious_chest)
        time.sleep(4)
        escape(2)
    else:
        log("No chests available")
        escape(1)
