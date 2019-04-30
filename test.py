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
wait_time = 5  # Amount of seconds to wait between each cycle
tod_comp1 = ["Elf_Maiden_Alisia", "Ninja_Meego", "Tagath_the_Potionbrewer", "Norak_the_Virtuous", "General_Kurbatov"]
tod_comp2 = ["Nymph_Edera", "Naga_Kertana", "Drowned_Samara", "Beastborn_Raider_Miaba", "Master_Hideus"]
tod_comp3 = ["Arzgar_the_Herald_of_Death", "Hitay_the_Spirit_of_Flame", "Crystalloid_Vern", "Samurai_Yasi", "Guard_Langerd"]
tod_comp4 = ["Healer_Cassandra", "Necromancer_Khardur", "Ronald_the_Inquisitor", "Gorbakh_the_Tyrant", "Superslug_Caliban"]

# Game variables
current_state = "Offline"
game_x = 0
game_y = 0

x_scaling = 1280 / resolution_x
y_scaling = 800 / resolution_y


# Use top bar to locate game start
def locate_game_window():
    memu_play = 'memu_play.PNG'
    img_box = pyautogui.locateOnScreen(memu_play, confidence=0.95)  # locate top left corner
    if img_box is not None:
        x, y = pyautogui.center(img_box)
        game_x_start = x - 47
        game_y_start = y + 13
        log("Game window found at " + str(game_x_start) + ", " + str(game_y_start))
        return game_x_start, game_y_start
    log("Game window not found")
    return 0, 0


def escape(amount):
    for x in range(0, amount):
        pyautogui.click(game_x + 1449 - 200, game_y + 150 - 118)
        time.sleep(0.2)


def click_daily_rewards():
    pyautogui.click(game_x + 320 - 138, game_y + 485 - 126) # click each reward once
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
    escape(2)


def click_on_box(box):
    center_points = pyautogui.center(box)
    pyautogui.click(center_points)
    time.sleep(0.5)


def get_value_from_rect(x1, y1, x2, y2):
    image = getRectAsImage((int(x1), int(y1), int(x2), int(y2)))
    # image.save('screencapture_256_256.png', format='png')
    config = '-l digits1+digits+digits_comma --psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    value = pytesseract.pytesseract.image_to_string(image, config=config)
    return value


def check_arena():
    click_image('imgs/arena_ready.PNG', "Arena ready", do_arena_battle)
    #arena_ready = pyautogui.locateOnScreen('imgs/arena_ready.PNG', confidence=0.95)
    #if arena_ready is not None:
    #    log("Arena ready")
    #    click_on_box(arena_ready)
    #    time.sleep(3)
    #    pyautogui.click(game_x + 1095 - 33, game_y + 487 - 49)
    #    time.sleep(1)
    #    do_arena_battle()


def deselect_heroes():
    log("Deselecting heroes")
    wait = 0.1
    pyautogui.click(game_x + 335 - 2, game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 482 - 2, game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 636 - 2, game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 785 - 2, game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 952 - 2, game_y + 707 - 30)


drag_count = 0


def select_heroes(mode):
    global drag_count
    log("Selecting heroes for " + mode)
    if mode == "Arena":
        select_arena_heroes()

    if mode == "Trial 1":
        select_tod_heroes(tod_comp1)

    if mode == "Trial 2":
        select_tod_heroes(tod_comp2)

    if mode == "Trial 3":
        select_tod_heroes(tod_comp3)

    if mode == "Trial 4":
        select_tod_heroes(tod_comp4)


def select_arena_heroes():
    wait = 0.1
    pyautogui.click(game_x + 167 - 2, game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 355 - 2, game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 481 - 2, game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 651 - 2, game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(game_x + 795 - 2, game_y + 315 - 30)


def select_tod_heroes(comp):
    for x in comp:
        select_hero(x)
    time.sleep(1)
    pyautogui.click(game_x + 1100, game_y + 670)
    time.sleep(1)


def select_hero(hero):
    global drag_count
    log("Looking for " + hero)
    hero_found = pyautogui.locateOnScreen('imgs/heroes/'+hero+'.PNG', confidence=0.95)
    if hero_found is not None:
        log(hero + " found.")
        click_on_box(hero_found)
        time.sleep(1)
    else:

        pyautogui.moveTo(game_x+630, game_y+350)
        time.sleep(0.3)
        if drag_count < 8:
            pyautogui.drag(0, -90, 0.2, button='left')
        else:
            pyautogui.drag(0, 90, 0.2, button='left')
        if drag_count > 15:
            drag_count = 0
        else:
            drag_count += 1
        time.sleep(1)
        select_hero(hero)


def enter_lowest(power1, power2, power3, select):
    lowest = power1
    if power2 < lowest:
        lowest = power2
        pyautogui.click(game_x + 526, game_y + 520)
    if power3 < lowest:
        lowest = power3
        pyautogui.click(game_x + 816, game_y + 520)
    if lowest == power1:
        pyautogui.click(game_x + 239, game_y + 520)
    log("Lowest power found: " + str(lowest) + ". Entering hero select.")
    time.sleep(2)
    if select is True:
        deselect_heroes()
        time.sleep(0.5)
        select_heroes(mode="Arena")
        time.sleep(0.5)
    log("Entering battle")
    pyautogui.click(game_x + 1100, game_y + 670)


def do_arena_battle():
    no_battles_ready = pyautogui.locateOnScreen('imgs/no_battles_ready.PNG', confidence=0.97)
    waiting = pyautogui.locateOnScreen('imgs/dont_wait.PNG', confidence=0.97)
    if no_battles_ready is None and waiting is None:
        log("Arena battles available. Doing Battle!")
        power1 = get_value_from_rect(game_x+241-2, game_y+425-29+49, game_x+325-2, game_y+505-29)
        power2 = get_value_from_rect(game_x + 528 - 2, game_y + 425 - 29 + 49, game_x + 605 - 2, game_y + 505 - 29)
        power3 = get_value_from_rect(game_x + 818 - 2, game_y + 425 - 29 + 49, game_x + 890 - 2, game_y + 505 - 29)
        enter_lowest(power1, power2, power3, True)
    else:
        log("Not ready for arena battle")
        escape(1)


def click_image(img, msg, func):
    img_ready = pyautogui.locateOnScreen(img, confidence=0.95)
    if img_ready is not None:
        log(msg)
        click_on_box(img_ready)
        time.sleep(3)
        pyautogui.click(game_x + 1095 - 33, game_y + 487 - 49)
        time.sleep(1)
        func()


def check_coliseum():
    click_image('imgs/coliseum_ready.PNG', "Coliseum ready", do_coliseum)
    #coliseum_ready = pyautogui.locateOnScreen('imgs/coliseum_ready.PNG', confidence=0.95)
    #if coliseum_ready is not None:
    #    log("Coliseum ready")
    #    click_on_box(coliseum_ready)
    #    time.sleep(1)
    #    do_coliseum()


def do_coliseum():
    power1 = get_value_from_rect(game_x + 245, game_y + 425 - 29 + 49, game_x + 325 - 2, game_y + 505 - 29)
    power2 = get_value_from_rect(game_x + 528 - 2, game_y + 425 - 29 + 49, game_x + 605 - 2, game_y + 505 - 29)
    power3 = get_value_from_rect(game_x + 818 - 2, game_y + 425 - 29 + 49, game_x + 890 - 2, game_y + 505 - 29)
    enter_lowest(power1, power2, power3, False)


def check_trial_of_death():
    click_image('imgs/tod_ready.PNG', "Trial of Death ready", do_trial_of_death)


def do_trial_of_death():
    trial_number = 1
    if pyautogui.locateOnScreen('imgs/3.PNG', confidence=0.95) is not None:
        log("3/3 trials left, entering hero select")
    elif pyautogui.locateOnScreen('imgs/2.PNG', confidence=0.95) is not None:
        log("2/3 trials left, entering hero select")
        trial_number = 2
    elif pyautogui.locateOnScreen('imgs/1.PNG', confidence=0.95) is not None:
        log("1/3 trials left, entering hero select")
        trial_number = 3

    hit_the_road = pyautogui.locateOnScreen('imgs/hit_the_road.PNG', confidence=0.95)
    if hit_the_road is not None:
        click_on_box(hit_the_road)
        time.sleep(1)
        pyautogui.click(game_x+901, game_y+721)

        time.sleep(2)
        select_heroes("Trial " + str(trial_number))
    else:
        log("Trial not ready, escaping")
        escape(1)


def click_next():
    pyautogui.click(game_x+1163, game_y+585)
    time.sleep(1)


def refresh_cave():
    pyautogui.click(game_x+905, game_y+544)  # click cave
    time.sleep(1.5)
    pyautogui.click(game_x+370, game_y+419)  # click gold
    time.sleep(1.5)
    pyautogui.click(game_x+780, game_y+124)  # accept gold
    time.sleep(1)
    pyautogui.click(game_x+780, game_y+124)  # click tantalum cave
    time.sleep(1)
    pyautogui.click(game_x + 370, game_y + 419)  # click xp
    time.sleep(1)
    pyautogui.click(game_x+780, game_y+124)  # accept xp
    time.sleep(1)
    pyautogui.click(game_x + 370, game_y + 419)  # click xp
    time.sleep(1)
    pyautogui.click(game_x+1012, game_y+725)  # set up all
    time.sleep(1)
    escape(3)


def finish_trial():
    pyautogui.click(game_x+580, game_y+725)
    time.sleep(1.5)
    pyautogui.click(game_x+770, game_y+430)
    time.sleep(1)


def detect_game_state():
    global current_state
    daily_rewards = 'imgs\daily_rewards.PNG'
    daily_rewards_located = pyautogui.locateOnScreen(daily_rewards, confidence=0.95)
    if daily_rewards_located is not None:
        current_state = "Daily Rewards"
        return

    cave_ready = pyautogui.locateOnScreen('imgs/cave_ready.png', confidence=0.95)
    if cave_ready is not None:
        current_state = "Refreshing Cave"
        return

    escape_sign = 'imgs/escape1.PNG'
    heroes_button = 'imgs/herosbutton.png'
    heroes_button_located = pyautogui.locateOnScreen(heroes_button, confidence=0.95)
    escape_sign_located = pyautogui.locateOnScreen(escape_sign, confidence=0.95)
    if heroes_button_located is not None:
        if escape_sign_located is not None:
            current_state = "Clan Castle"
            return
        else:
            current_state = "Home Screen"
            return

    tod_win = pyautogui.locateOnScreen('imgs/tod_win.png', confidence=0.95)
    if tod_win is not None:
        if escape_sign_located is not None:
            current_state = "Trial Win"
            return

    arena_available_battles = pyautogui.locateOnScreen('imgs/arena_available_battles.png', confidence=0.95)
    if arena_available_battles is not None:
        if escape_sign_located is not None:
            current_state = "Arena"
            return

    walk_through_tod = pyautogui.locateOnScreen('imgs/walk_through_tod.png', confidence=0.95)
    if walk_through_tod is not None:
        if escape_sign_located is not None:
            current_state = "Trial of Death"
            return

    power = pyautogui.locateOnScreen('imgs/power.png', confidence=0.95)
    battle_start = pyautogui.locateOnScreen('imgs/battle_start.png', confidence=0.95)
    if power is not None and battle_start is not None:
        current_state = "Hero Select"
        return

    next_button = pyautogui.locateOnScreen('imgs/next.png', confidence=0.95)
    if next_button is not None:
        current_state = "Victory"
        return

    auto_on = pyautogui.locateOnScreen('imgs/auto_on.png', confidence=0.95)
    if auto_on is not None:
        current_state = "In Battle"
        return


def do_work():
    global current_state
    if current_state == "Trial Win":
        finish_trial()

    if current_state == "Daily Rewards":
        click_daily_rewards()

    if current_state == "Home Screen":
        check_arena()
        check_trial_of_death()
        check_coliseum()

    if current_state == "Clan Castle":
        escape(1)

    if current_state == "Arena":
        do_arena_battle()

    if current_state == "Trial of Death":
        do_trial_of_death()

    if current_state == "Hero Select":
        escape(2)

    if current_state == "Victory":
        click_next()

    if current_state == "Refreshing Cave":
        refresh_cave()

    if current_state == "Working":
        log("Unknown game state, trying to correct")
        escape(1)


def main_loop():
    global current_state
    current_state = "Working"

    # Detect game state
    detect_game_state()
    log("Current state is: " + current_state)

    # Act on game state
    do_work()

    # Wait wait_time sec and start over
    log("Cycle done, waiting " + str(wait_time) + " seconds and restarting")
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
    except pyautogui.FailSafeException:
        log("Stopping")
