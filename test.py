from jwLogging import log
import pyautogui
import time
import os
import tkinter
import threading
import random
import datetime
import winsound
import sys
import pygubu
from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


# User settings
resolution_x = 1280  # Game window resolution width
resolution_y = 800  # Game window resolution height
wait_time = 20  # Amount of seconds to wait between each cycle

# Game variables
current_state = "Offline"
game_x = 0
game_y = 0

x_scaling = 1280 / resolution_x
y_scaling = 800 / resolution_y


# Use top bar to locate game start
def locate_game_window():
    memu_play = 'memu_play.PNG'
    img_box = pyautogui.locateOnScreen(memu_play, confidence=0.95)
    if img_box is not None:
        x, y = pyautogui.center(img_box)
        game_x_start = x - 47
        game_y_start = y + 13
        log("Game window found at " + str(game_x_start) + ", " + str(game_y_start))
        return game_x_start, game_y_start
    log("Game window not found")
    return 0, 0


def detect_game_state():
    global current_state
    daily_rewards = 'imgs\daily_rewards.PNG'
    daily_rewards_located = pyautogui.locateOnScreen(daily_rewards, confidence=0.95)
    if daily_rewards_located is not None:
        current_state = "Daily Rewards"

    escape_sign = 'imgs/escape1.PNG'
    heroes_button = 'imgs/herosbutton.png'
    heroes_button_located = pyautogui.locateOnScreen(heroes_button, confidence=0.95)
    escape_sign_located = pyautogui.locateOnScreen(escape_sign, confidence=0.95)
    if heroes_button_located is not None:
        if escape_sign_located is not None:
            current_state = "Clan Castle"
        else:
            current_state = "Home Screen"

    arena_available_battles = pyautogui.locateOnScreen('imgs/arena_available_battles.png', confidence=0.95)
    if arena_available_battles is not None:
        if escape_sign_located is not None:
            current_state = "Arena"


def escape():
    for x in range(0, 4):
        pyautogui.click(game_x + 1449 - 200, game_y + 150 - 118)
        time.sleep(0.2)


def click_daily_rewards():
    pyautogui.click(game_x + 320 - 138, game_y + 485 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 508 - 138, game_y + 410 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 686 - 138, game_y + 485 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 876 - 138, game_y + 416 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 1046 - 138, game_y + 485 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 1205 - 138, game_y + 423 - 126)
    time.sleep(0.5)
    escape()


def click_on_box(box):
    centerPoints = pyautogui.center(box)
    pyautogui.click(centerPoints)
    time.sleep(0.5)


def draw_value_from_rect(x1, y1, x2, y2):
    image = getRectAsImage((int(x1), int(y1), int(x2), int(y2)))
    # image.save('screencapture_256_256.png', format='png')
    config = '-l digits1+digits+digits_comma --psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    value = pytesseract.pytesseract.image_to_string(image, config=config)
    return value

def check_arena():
    arena_ready = pyautogui.locateOnScreen('imgs/arena_ready.PNG', confidence=0.95)
    if arena_ready is not None:
        log("Arena ready")
        click_on_box(arena_ready)
        time.sleep(5)
        pyautogui.click(game_x + 1095 - 33, game_y + 487 - 49)


def do_arena_battle():
    no_battles_ready = pyautogui.locateOnScreen('imgs/in_the_name_of_the_light.PNG', confidence=0.95)
    if no_battles_ready is None:
        log("Arena battles available. Doing Battle!")
        power1 = draw_value_from_rect(game_x+241-2, game_y+425-29+49, game_x+325-2, game_y+505-29)
        log(power1)
        power2 = draw_value_from_rect(game_x + 528 - 2, game_y + 425 - 29 + 49, game_x + 605 - 2, game_y + 505 - 29)
        log(power2)
        power3 = draw_value_from_rect(game_x + 818 - 2, game_y + 425 - 29 + 49, game_x + 890 - 2, game_y + 505 - 29)
        log(power3)

def check_trial_of_death():
    tod_ready = pyautogui.locateOnScreen('imgs/tod_ready.PNG', confidence=0.95)
    if tod_ready is not None:
        log("Trial of Death ready")
        click_on_box(tod_ready)


def do_work():
    if current_state == "Daily Rewards":
        click_daily_rewards()

    if current_state == "Home Screen":
        check_arena()
        check_trial_of_death()

    if current_state == "Arena":
        do_arena_battle()


def main_loop():
    global current_state
    current_state = "Working"

    # Detect game state
    detect_game_state()
    log("Current state is: " + current_state)

    # Act on game state
    do_work()

    # Wait wait_time sec and start over
    log("Checks done, waiting " + str(wait_time) + " seconds and restarting")
    current_state = "Waiting"
    time.sleep(wait_time)
    main_loop()


# Init
if __name__ == '__main__':
    try:
        log('Press Ctrl-C to quit.')
        game_x, game_y = locate_game_window()
        main_loop()
    except KeyboardInterrupt:
        print('\n')
