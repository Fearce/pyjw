from helpers import delay_next_check, log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, \
    click, click_next, look_for_button
import pyautogui
import time
import settings
import datetime

last_castle = datetime.datetime.now()
last_castle = last_castle.replace(hour=last_castle.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_clan_castle():
    global last_castle
    if not settings.clan_castle:
        return
    if delay_next_check(2, last_castle):
        return
    last_castle = datetime.datetime.now()
    log("Checking Clan Castle.")
    clan_castle = pyautogui.locateOnScreen('imgs/clan_castle.png', confidence=0.85)
    if clan_castle is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/clan_castle.png', "Clan Castle", check_treasury)
    else:
        click_on_box(clan_castle)


last_treasury = datetime.datetime.now()
last_treasury = last_treasury.replace(hour=last_treasury.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_treasury)
def check_treasury():
    global last_treasury
    if not settings.treasury:
        return
    if delay_next_check(59, last_treasury):
        return
    last_treasury = datetime.datetime.now()
    log("Checking Treasury.")
    treasury = pyautogui.locateOnScreen('imgs/treasury.png', confidence=0.85)
    if treasury is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/treasury.png', "Treasury", treasury_donate)
    else:
        click_on_box(treasury)
        treasury_donate()


def treasury_donate():
    time.sleep(1)
    click(270, 640)
    time.sleep(1)
    click(270, 640)
    time.sleep(1)
    click(600, 640)
    time.sleep(1)
    click(270, 640)
    escape(1)


last_caravan = datetime.datetime.now()
last_caravan = last_caravan.replace(hour=last_caravan.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_caravan)
def check_caravan():
    log("TODO")


last_praises = datetime.datetime.now()
last_praises = last_praises.replace(hour=last_praises.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_praises)
def check_praises():
    log("TODO")


last_raids = datetime.datetime.now()
last_raids = last_raids.replace(hour=last_raids.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_raids)
def check_raids():
    log("TODO")


last_wheel = datetime.datetime.now()
last_wheel = last_wheel.replace(hour=last_wheel.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_wheel_of_fortune)
def check_wheel_of_fortune():
    global last_wheel
    if not settings.wheel:
        return
    if delay_next_check(59, last_wheel):
        return
    last_wheel = datetime.datetime.now()
    log("Checking Wheel of Fortune.")
    wheel_of_fortune = pyautogui.locateOnScreen('imgs/wheel_of_fortune.png', confidence=0.9)
    if wheel_of_fortune is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/wheel_of_fortune.png', "Wheel of Fortune", do_wheel_of_fortune)
    else:
        click_on_box(wheel_of_fortune)
        do_wheel_of_fortune()


def do_wheel_of_fortune():
    time.sleep(1)
    for x in range(0, 30):
        click(1020, 460)
        time.sleep(0.2)
    click(980, 600)
    time.sleep(2)
    escape(2)

last_altar = datetime.datetime.now()
last_altar = last_altar.replace(hour=last_altar.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_altar)
def check_altar():
    log("TODO")


last_store = datetime.datetime.now()
last_store = last_store.replace(hour=last_store.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_clan_store)
def check_clan_store():
    log("TODO")
