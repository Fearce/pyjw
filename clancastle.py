from helpers import delay_next_check, log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, \
    click, click_next, look_for_button, go_down, wait_on_img
import pyautogui
import time
import settings
import datetime

from heroselection import select_raid_heroes

last_castle = datetime.datetime.now()
if last_castle.hour == 0:
    last_castle = last_castle.replace(minute=0)
else:
    last_castle = last_castle.replace(hour=last_castle.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_clan_castle():
    global last_castle
    if not settings.clan_castle:
        return
    if delay_next_check(1, last_castle):
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
if last_treasury.hour == 0:
    last_treasury = last_treasury.replace(minute=0)
else:
    last_treasury = last_treasury.replace(hour=last_treasury.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_treasury)
def check_treasury():
    global last_treasury
    if not settings.treasury:
        return
    if delay_next_check(2, last_treasury):
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
        time.sleep(1.5)
        treasury_none = pyautogui.locateOnScreen('imgs/treasury_none.png', confidence=0.95)
        if treasury_none is not None:
            log("Treasury already done")
            escape(1)
            return
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
if last_caravan.hour == 0:
    last_caravan = last_caravan.replace(minute=0)
else:
    last_caravan = last_caravan.replace(hour=last_caravan.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_caravan)
def check_caravan():
    global last_caravan
    if not settings.caravan:
        return
    if delay_next_check(2, last_caravan):
        return
    last_caravan = datetime.datetime.now()
    log("Checking Caravan.")
    caravan = pyautogui.locateOnScreen('imgs/caravan.png', confidence=0.85)
    if caravan is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/caravan.png', "Caravan", join_caravan)
    else:
        click_on_box(caravan)
        join_caravan()


def join_caravan():
    time.sleep(2)
    click(1100, 291-129)
    time.sleep(2)
    caravan_join = pyautogui.locateOnScreen('imgs/caravan_join.png', confidence=0.9)
    if caravan_join is not None:
        click_on_box(caravan_join)
        time.sleep(1)
    escape(1)


last_praises = datetime.datetime.now()
if last_praises.hour == 0:
    last_praises = last_praises.replace(minute=0)
else:
    last_praises = last_praises.replace(hour=last_praises.hour - 1)  # Remove 1 hour to make sure it checks first run





# clan_castle_func(check_praises)
def check_praises():
    global last_praises
    if not settings.praises:
        return
    if delay_next_check(2, last_praises):
        return
    last_praises = datetime.datetime.now()
    log("Checking Praises.")
    praises = pyautogui.locateOnScreen('imgs/praises.png', confidence=0.85)
    if praises is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/praises.png', "Praises", give_praises)
    else:
        click_on_box(praises)
        give_praises()


def give_praises():
    wait_on_img('imgs/praises_members.png', 0.8,60)
    click(1165, 440)  # Click members
    wait_on_img('imgs/praise_ready.png', 0.8,60)
    praises_none = pyautogui.locateOnScreen('imgs/praises_none.png', confidence=0.999)
    praise_ready = pyautogui.locateOnScreen('imgs/praise_ready.png', confidence=0.85)
    if praises_none is not None:
        log("lul no praises")
    while praises_none is None:
        log("Praises ready")
        if praise_ready is not None:
            log("Found praise")
            click_on_box(praise_ready)
            time.sleep(2)
            praise_two = pyautogui.locateOnScreen('imgs/praise_two.png', confidence=0.85)
            if praise_two is not None:
                click_on_box(praise_two)
                time.sleep(3)
                escape(1)
                time.sleep(1)
            praise_ready = pyautogui.locateOnScreen('imgs/praise_ready.png', confidence=0.85)
        else:
            go_down()
            time.sleep(2)
            praise_ready = pyautogui.locateOnScreen('imgs/praise_ready.png', confidence=0.85)
        praises_none = pyautogui.locateOnScreen('imgs/praises_none.png', confidence=0.999)
    escape(1)

last_raids = datetime.datetime.now()
if last_raids.hour == 0:
    last_raids = last_raids.replace(minute=0)
else:
    last_raids = last_raids.replace(hour=last_raids.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_raids)
def check_raids():
    global last_raids
    if not settings.raids:
        return
    if delay_next_check(2, last_raids):
        return
    last_raids = datetime.datetime.now()
    log("Checking Battle Cave.")
    battle_cave = pyautogui.locateOnScreen('imgs/battle_cave.png', confidence=0.9)
    if battle_cave is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/battle_cave.png', "Battle Cave", do_raids)
    else:
        click_on_box(battle_cave)
        do_raids()

def do_raids():
    global last_raids
    # no raids todo
    time.sleep(1.5)
    battle_cave_go = pyautogui.locateOnScreen('imgs/battle_cave_go.png', confidence=0.9)
    for x in range(0, 11):
        no_clan_attempts = pyautogui.locateOnScreen('imgs/no_clan_attempts.png', confidence=0.99)
        if no_clan_attempts is not None:
            log("No more clan attempts")
            last_raids = datetime.datetime.now()
            escape(1)
            return
        if battle_cave_go is None:
            go_down()
            time.sleep(1.5)
            battle_cave_go = pyautogui.locateOnScreen('imgs/battle_cave_go.png', confidence=0.9)
        else:
            click_on_box(battle_cave_go)
            wait_on_img('imgs/battle_start.png', 0.8,60)
            empty_slot = pyautogui.locateOnScreen('imgs/empty_slot.png', confidence=0.9)
            if empty_slot is not None:
                click(746, 566)
                select_raid_heroes()
                click(1098, 675)
                time.sleep(2)
            click(1047, 664)
            #click_on_box(pyautogui.locateOnScreen('imgs/battle_start.png', confidence=0.9))
            time.sleep(1)
            break
    log("Seems no raid is available at the moment, escaping")
    escape(1)

last_wheel = datetime.datetime.now()
if last_wheel.hour == 0:
    last_wheel = last_wheel.replace(minute=0)
else:
    last_wheel = last_wheel.replace(hour=last_wheel.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_wheel_of_fortune)
def check_wheel_of_fortune():
    global last_wheel
    if not settings.wheel:
        return
    if delay_next_check(2, last_wheel):
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
    escape(1)
    time.sleep(2)

last_altar = datetime.datetime.now()
if last_altar.hour == 0:
    last_altar = last_altar.replace(minute=0)
else:
    last_altar = last_altar.replace(hour=last_altar.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_altar)
def check_altar():
    global last_altar
    if not settings.altar:
        return
    if delay_next_check(2, last_altar):
        return
    last_altar = datetime.datetime.now()
    log("Checking Altar.")
    altar = pyautogui.locateOnScreen('imgs/altar.png', confidence=0.9)
    if altar is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/altar.png', "Altar", altar_contribute)
    else:
        altar = pyautogui.locateOnScreen('imgs/altar.png', confidence=0.9)
        if altar is not None:
            click_on_box(altar)
        altar_contribute()

def altar_contribute():
    altar = pyautogui.locateOnScreen('imgs/altar.png', confidence=0.9)
    if altar is not None:
        click_on_box(altar)
    time.sleep(2)
    click(575, 260)  # contribute
    time.sleep(1)
    escape(1)


last_store = datetime.datetime.now()
if last_store.hour == 0:
    last_store = last_store.replace(minute=0)
else:
    last_store = last_store.replace(hour=last_store.hour - 1)  # Remove 1 hour to make sure it checks first run


# clan_castle_func(check_clan_store)
def check_clan_store():
    global last_store
    if not settings.clan_store:
        return
    if delay_next_check(2, last_store):
        return
    last_store = datetime.datetime.now()
    log("Checking Clan Store.")
    clan_store = pyautogui.locateOnScreen('imgs/clan_store.png', confidence=0.9)
    if clan_store is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/clan_store.png', "Clan Store", clan_store_buy)
    else:
        click_on_box(clan_store)
        clan_store_buy()


def clan_store_buy():
    time.sleep(2)
    click(1221-4, 424-28)  # Slug
    time.sleep(1)
    click(650, 716)  # Buy
    time.sleep(2)
    click(1222-4, 398-32)  # Escape
    time.sleep(1)
    click(780, 388-32)  # Amok
    time.sleep(1)
    click(650, 716)  # Buy
    time.sleep(2)
    click(1222-4, 398-32)  # Escape
    time.sleep(1)
    escape(1)