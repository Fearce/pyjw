from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, go_left, go_right, look_for_button
import pyautogui
import time
import settings


def check_chests():
    log("Checking chests")
    chest = pyautogui.locateOnScreen('imgs/chestavailable.png', confidence=0.88)
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
    chest = pyautogui.locateOnScreen('imgs/freewoodchest.png', confidence=0.75)
    if chest is not None:
        log("Opening wooden chest")
        click_on_box(chest)
        time.sleep(4)
        escape(2)
    else:
        log("No chests available")
        escape(1)
