import datetime
import time

import pyautogui

import settings
from helpers import log, click_image, delay_next_check, click_on_box
from heroselection import select_hero

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_tournament():
    global last_check
    if not settings.tournament:
        return
    if delay_next_check(2, last_check):
        return
    click_image('imgs/tournament_ready.png', "Checking tournament", do_tournament)

def do_tournament():
    time.sleep(3)
    click_image('imgs/tournament_battle.PNG', "To battle!", doing)
    click_image('imgs/tournament_battle2.PNG', "To battle!", doing)

def doing():
    # log("Waiting while tournament battle plays out.")
    # Wait for battle to start
    arena_waiting = pyautogui.locateOnScreen('imgs/arena_waiting.png', confidence=0.9)
    arena_hero_needed = pyautogui.locateOnScreen('imgs/arena_hero_needed.png', confidence=0.9)
    while arena_waiting is None and arena_hero_needed is None:
        log("Waiting for opponent.")
        arena_waiting = pyautogui.locateOnScreen('imgs/arena_waiting.png', confidence=0.95)
        arena_hero_needed = pyautogui.locateOnScreen('imgs/arena_hero_needed.png', confidence=0.95)
        time.sleep(3)
    arena_ok = pyautogui.locateOnScreen('imgs/arena_ok.png', confidence=0.9)
    while arena_ok is None:
        auto_on = pyautogui.locateOnScreen('imgs/auto_on.png', confidence=0.95)
        if auto_on is not None:
            log("In Battle")
            break
        select_hero('promo_hero')
        arena_ok = pyautogui.locateOnScreen('imgs/arena_ok.png', confidence=0.9)
        time.sleep(2)
    click_on_box(arena_ok)
