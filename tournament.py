import datetime
import time

import pyautogui

from helpers import log, click_image, delay_next_check
from heroselection import select_hero

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run

def check_tournament():
    global last_check
    if delay_next_check(2, last_check):
        return
    click_image('imgs/tournament_ready.png', "Checking tournament", do_tournament)

def do_tournament():
    time.sleep(3)
    click_image('imgs/tournament_battle.PNG', "To battle!", doing)
    click_image('imgs/tournament_battle2.PNG', "To battle!", doing)

def doing():
    # log("Waiting while tournament battle plays out.")
    for x in range(0, 20):
        auto_on = pyautogui.locateOnScreen('imgs/auto_on.png', confidence=0.95)
        if auto_on is not None:
            log("In Battle")
            break
        select_hero('promo_hero')
        time.sleep(5)
    time.sleep(120)
