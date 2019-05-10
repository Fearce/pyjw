from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

drag_count = 0

def select_heroes(mode):
    global drag_count
    log("Selecting heroes for " + mode)
    if mode == "Arena":
        select_arena_heroes()

    if mode == "Trial 1":
        select_tod_heroes(settings.tod_comp1)

    if mode == "Trial 2":
        select_tod_heroes(settings.tod_comp2)

    if mode == "Trial 3":
        select_tod_heroes(settings.tod_comp3)

    if mode == "Trial 4":
        select_tod_heroes(settings.tod_comp4)


def deselect_heroes():
    log("Deselecting Arena heroes")
    wait = 0.25
    pyautogui.click(settings.game_x + 335 - 2, settings.game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 482 - 2, settings.game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 636 - 2, settings.game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 785 - 2, settings.game_y + 707 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 952 - 2, settings.game_y + 707 - 30)


def select_arena_heroes():
    log("Selecting Arena heroes")
    wait = 0.25
    pyautogui.click(settings.game_x + 167 - 2, settings.game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 355 - 2, settings.game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 481 - 2, settings.game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 651 - 2, settings.game_y + 315 - 30)
    time.sleep(wait)
    pyautogui.click(settings.game_x + 795 - 2, settings.game_y + 315 - 30)


def select_tod_heroes(comp):
    log("Selecting ToD heroes")
    for x in comp:
        select_hero(x)
    time.sleep(0.15)
    pyautogui.click(settings.game_x + 1100, settings.game_y + 670)
    time.sleep(0.15)

promo_drag_count = 0
def select_promo_hero(mode):
    global promo_drag_count
    promo_img = 'imgs/heroes/promo_hero.PNG'
    log("Looking for promo hero")

recursion_limit = 0
def select_hero(hero):
    global drag_count, recursion_limit
    recursion_limit += 1
    if recursion_limit >= 50:
        recursion_limit = 0
        return
    tournament_clock = pyautogui.locateOnScreen('imgs/tournament_clock.PNG', confidence=0.88)
    if tournament_clock is not None:
        return
    log("Looking for " + hero)
    hero_found = pyautogui.locateOnScreen('imgs/heroes/'+hero+'.PNG', confidence=0.88)
    if hero_found is not None:
        log(hero + " found.")
        click_on_box(hero_found)
        time.sleep(0.1)
    else:

        pyautogui.moveTo(settings.game_x+630, settings.game_y+350)
        time.sleep(0.2)
        if drag_count < 8:
            pyautogui.drag(0, -90, 0.2, button='left')
        else:
            pyautogui.drag(0, 90, 0.2, button='left')
        if drag_count > 15:
            drag_count = 0
        else:
            drag_count += 1
        time.sleep(0.1)
        select_hero(hero)


def enter_lowest(power1, power2, power3, select):
    lowest = power1
    if float(power2) < float(lowest):
        lowest = power2
    if float(power3) < float(lowest):
        lowest = power3
    if lowest == power1:
        pyautogui.click(settings.game_x + 239, settings.game_y + 520)
    if lowest == power3:
        pyautogui.click(settings.game_x + 816, settings.game_y + 520)
    if lowest == power2:
        pyautogui.click(settings.game_x + 526, settings.game_y + 520)
    log("1: " + str(power1) + ". 2: " + str(power2) + ". 3: " + str(power3) + ".")
    log("Lowest power found: " + str(lowest) + ". Entering hero select.")
    time.sleep(2)
    if select is True:
        deselect_heroes()
        time.sleep(0.5)
        select_heroes(mode="Arena")
        time.sleep(0.5)
    log("Entering battle")
    pyautogui.click(settings.game_x + 1100, settings.game_y + 670)
    time.sleep(2)


def select_raid_heroes():
    time.sleep(1)
    wait_time = 0.15
    click(173, 264)
    time.sleep(wait_time)
    click(173, 413)
    time.sleep(wait_time)
    click(173, 542)
    time.sleep(wait_time)
    click(320, 264)
    time.sleep(wait_time)
    click(320, 413)
    time.sleep(wait_time)
    click(320, 542)
    time.sleep(wait_time)
    click(475, 264)
    time.sleep(wait_time)
    click(475, 413)
    time.sleep(wait_time)
    click(475, 542)
    time.sleep(wait_time)
    click(640, 264)
    time.sleep(wait_time)
    click(640, 413)
    time.sleep(wait_time)
    click(640, 542)
    time.sleep(wait_time)
    click(790, 264)
    time.sleep(wait_time)
    click(790, 413)
    time.sleep(wait_time)
    click(790, 542)
    time.sleep(wait_time)
    click(950, 264)
    time.sleep(wait_time)
    click(950, 413)
    time.sleep(wait_time)
    click(950, 542)
    time.sleep(wait_time)
    click(1100, 264)
    time.sleep(wait_time)
    click(1100, 413)
    time.sleep(wait_time)
    click(1100, 542)
    time.sleep(wait_time)
