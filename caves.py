import datetime
from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check, wait_on_img, go_down
import pyautogui
import time
import settings

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_cave():
    global last_check
    if not settings.caves:
        return
    # delay_msg = "Checked skillpoints at " + str(last_check) + ". Waiting until 30 minutes has passed"
    if delay_next_check(20, last_check):
        return
    last_check = datetime.datetime.now()

    log("Checking Cave")
    cave_ready = pyautogui.locateOnScreen('imgs/cave_ready.png', confidence=0.95)
    if cave_ready is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/cave_ready.png', "Cave", refresh_cave)
    else:
        click_on_box(cave_ready)
        refresh_cave()


first_check = False
def refresh_cave():
    global first_check
    #pyautogui.click(settings.game_x+905, settings.game_y+544)  # click cave
    time.sleep(1)
    in_cave = pyautogui.locateOnScreen('imgs/in_cave.png', confidence=0.85)
    if in_cave is None:
        return
    pyautogui.click(settings.game_x+370, settings.game_y+419)  # click gold
    time.sleep(2)
    cave_output = pyautogui.locateOnScreen('imgs/caves_mined.png', confidence=0.85)
    if cave_output is not None and first_check:
        log("Cave currently running")
        escape(1)
        do_cave_fights()
        return
    pyautogui.click(settings.game_x + 370, settings.game_y + 419)  # click gold
    time.sleep(1.5)
    pyautogui.click(settings.game_x+780, settings.game_y+124)  # accept gold
    time.sleep(1)
    pyautogui.click(settings.game_x+780, settings.game_y+124)  # click tantalum cave
    time.sleep(1)
    pyautogui.click(settings.game_x + 370, settings.game_y + 419)  # click xp
    time.sleep(1)
    pyautogui.click(settings.game_x+780, settings.game_y+124)  # accept xp
    time.sleep(1)
    pyautogui.click(settings.game_x + 370, settings.game_y + 419)  # click xp
    time.sleep(3)
    pyautogui.click(settings.game_x+1012, settings.game_y+725)  # set up all
    time.sleep(1)
    first_check = True
    escape(1)
    time.sleep(0.2)
    escape(1)
    do_cave_fights()
    escape(1)
    do_cave_fights()




def do_cave_fights():
    # cave fights cave_fights_ready, 889, 509
    log("Checking cave fights")
    cave_buy = pyautogui.locateOnScreen('imgs/cave_buy.png', confidence=0.8)
    cave_no_attempts = pyautogui.locateOnScreen('imgs/cave_no_attempts.png', confidence=0.85)
    if cave_buy is not None or cave_no_attempts is not None:
        log("No cave attempts, leaving")
        escape(1)
        return
    time.sleep(1)
    #pyautogui.click(settings.game_x + 370, settings.game_y + 419)  # click gold
    #time.sleep(1)
    log("Clicking fight")
    click(888, 500)
    time.sleep(3)
    cave_battle_go = pyautogui.locateOnScreen('imgs/cave_battle_go.png', confidence=0.8)
    if cave_battle_go is None:
        cave_battle_go = pyautogui.locateOnScreen('imgs/cave_battle_go2.png', confidence=0.8)
    if cave_battle_go is not None:
        log("Going")

        power1 = get_value_from_rect(settings.game_x+635, settings.game_y+171-40, settings.game_x+720, settings.game_y+197-28)
        power2 = get_value_from_rect(settings.game_x + 639, settings.game_y + 385-34, settings.game_x + 716, settings.game_y + 410-30)
        power3 = get_value_from_rect(settings.game_x + 639, settings.game_y + 598-34, settings.game_x + 716, settings.game_y + 623-30)
        log(power1)
        log(power2)
        log(power3)
        powers = [power1,power2,power3]
        for p in powers:
            try:
                if int(p) > settings.cave_max_power:
                    log("Power " + str(p) + " is too high, searching for new opponent")
                    click(1047, 670)
                    time.sleep(4)
                    #return
            except ValueError:
                if p == ". 0":
                    log("0")
                else:
                    log("Error parsing power " + str(p))

        #time.sleep(10)
        cave_empty = pyautogui.locateOnScreen('imgs/cave_empty.png', confidence=0.8)
        #if cave_empty is None:
        #    log("Heroes full, going")
        click_on_box(cave_battle_go)

        time.sleep(2)
        cave_empty = pyautogui.locateOnScreen('imgs/cave_empty.png', confidence=0.85)

        while cave_empty is not None:
            log("Picking hero for cave battle")
            hero_red = pyautogui.locateOnScreen('imgs/hero_red.png', confidence=0.95)
            if hero_red is None:
                go_down()
                time.sleep(1)
            else:
                click_on_box(hero_red)
                time.sleep(1)
            cave_empty = pyautogui.locateOnScreen('imgs/cave_empty.png', confidence=0.8)
        time.sleep(1)
        cave_battle_start = pyautogui.locateOnScreen('imgs/cave_battle.png', confidence=0.8)
        if cave_battle_start is not None:
            log("Starting cave battle.")
            click_on_box(cave_battle_start)
    #log("Cave battles done")
    #escape(1)

    #escape(1)

def get_cave_gold():
    cave_gold = pyautogui.locateOnScreen('imgs/cave_gold.png', confidence=0.9)
    if cave_gold is not None:
        log("Clicking cave gold")
        click_on_box(cave_gold)
        time.sleep(1)
        #escape(1)