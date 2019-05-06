from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
from dailyrewards import click_daily_rewards
from caves import check_cave
from missions import check_missions
from portal import check_portal
from skillpoints import check_skill_points
from tournament import check_tournament
from trialofdeath import check_trial_of_death, do_trial_of_death, finish_trial
from coliseum import check_coliseum, do_coliseum
from arena import check_arena, do_arena_battle
from chests import check_chests
from friends import check_friends
from mailbox import check_mailbox
from events import check_events
import settings
from heroselection import select_heroes, deselect_heroes, select_arena_heroes, select_tod_heroes, select_hero, enter_lowest
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
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def detect_game_state():
    add_close_located = pyautogui.locateOnScreen('imgs/add_close.PNG', confidence=0.95)
    if add_close_located is not None:
        settings.current_state = "Advertisement"
        escape(1)
        return

    daily_rewards = 'imgs\daily_rewards.PNG'
    daily_rewards_located = pyautogui.locateOnScreen(daily_rewards, confidence=0.95)
    if daily_rewards_located is not None:
        settings.current_state = "Daily Rewards"
        return

    heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
    escape_sign_located = pyautogui.locateOnScreen('imgs/escape1.PNG', confidence=0.95)
    if heroes_button_located is not None:
        if escape_sign_located is not None:
            settings.current_state = "Clan Castle"
            return
        else:
            settings.current_state = "Home Screen"
            return

    tod_win = pyautogui.locateOnScreen('imgs/tod_win.png', confidence=0.95)
    if tod_win is not None:
        if escape_sign_located is not None:
            settings.current_state = "Trial Win"
            return

    arena_available_battles = pyautogui.locateOnScreen('imgs/arena_available_battles.png', confidence=0.95)
    if arena_available_battles is not None:
        if escape_sign_located is not None:
            settings.current_state = "Arena"
            return

    walk_through_tod = pyautogui.locateOnScreen('imgs/walk_through_tod.png', confidence=0.95)
    if walk_through_tod is not None:
        if escape_sign_located is not None:
            settings.current_state = "Trial of Death"
            return

    power = pyautogui.locateOnScreen('imgs/power.png', confidence=0.95)
    battle_start = pyautogui.locateOnScreen('imgs/battle_start.png', confidence=0.95)
    if power is not None and battle_start is not None:
        settings.current_state = "Hero Select"
        return

    next_button = pyautogui.locateOnScreen('imgs/next.png', confidence=0.95)
    if next_button is not None:
        settings.current_state = "Victory"
        return

    auto_on = pyautogui.locateOnScreen('imgs/auto_on.png', confidence=0.95)
    if auto_on is not None:
        settings.current_state = "In Battle"
        return


def home_screen_func(func):
    detect_game_state()
    if settings.current_state != "Home Screen":
        do_work()
    else:
        func()


def do_work():
    if settings.current_state == "Trial Win":
        finish_trial()

    if settings.current_state == "Daily Rewards":
        click_daily_rewards()

    if settings.current_state == "Clan Castle":
        escape(1)

    if settings.current_state == "Arena":
        do_arena_battle()

    if settings.current_state == "Trial of Death":
        do_trial_of_death()

    if settings.current_state == "Hero Select":
        escape(2)

    if settings.current_state == "Victory":
        click_next()

    if settings.current_state == "Home Screen":
        if settings.arena:
            home_screen_func(check_arena)
        if settings.trial_of_death:
            home_screen_func(check_trial_of_death)
        if settings.skill_points:
            home_screen_func(check_skill_points)
        if settings.coliseum:
            home_screen_func(check_coliseum)
        if settings.tournament:
            home_screen_func(check_tournament)
        if settings.events:
            home_screen_func(check_events)
        if settings.caves:
            home_screen_func(check_cave)
        if settings.chests:
            home_screen_func(check_chests)
        if settings.mailbox:
            home_screen_func(check_mailbox)
        if settings.missions:
            home_screen_func(check_missions)
        if settings.friends:
            home_screen_func(check_friends)
        if settings.portal:
            home_screen_func(check_portal)
        # check trial
        # check otherworld
        # missions
        # upgrade heroes

    if settings.current_state == "Working":
        log("Unknown game state, trying to correct")
        escape(1)


def main_loop(args):
    settings.current_state = "Working"

    # Detect game state
    detect_game_state()
    log("Current state is: " + settings.current_state)

    # Act on game state
    do_work()

    # Wait wait_time sec and start over
    log("Cycle done, waiting " + str(settings.wait_time) + " seconds and restarting")
    #settings.current_state = "Waiting"
    if settings.current_state == "Home Screen":
        time.sleep(settings.wait_time)
    else:
        time.sleep(1)
    return main_loop, (args,)


# Init
if __name__ == '__main__':
    try:
        log('Press Ctrl-C to quit.')
        settings.game_x, settings.game_y = locate_game_window()
        main_loop, args = main_loop("Start")
        while True:
            main_loop, args = main_loop(*args)
    except KeyboardInterrupt:
        print('\n')
    except pyautogui.FailSafeException:
        log("Stopping")
