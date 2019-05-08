import datetime

from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    delay_next_check
import pyautogui
import time
import settings
from heroselection import enter_lowest

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_coliseum():
    global last_check
    if not settings.coliseum:
        return
    if delay_next_check(25, last_check):
        return
    log("Checking Coliseum")
    click_image('imgs/coliseum_ready.PNG', "Coliseum ready", do_coliseum)
    #coliseum_ready = pyautogui.locateOnScreen('imgs/coliseum_ready.PNG', confidence=0.95)
    #if coliseum_ready is not None:
    #    log("Coliseum ready")
    #    click_on_box(coliseum_ready)
    #    time.sleep(1)
    #    do_coliseum()


def do_coliseum():
    global last_check
    last_check = datetime.datetime.now()
    if pyautogui.locateOnScreen('imgs/0_2.PNG', confidence=0.95) is None:
        power1 = get_value_from_rect(settings.game_x + 245, settings.game_y + 425 - 29 + 49, settings.game_x + 325 - 2, settings.game_y + 505 - 29)
        power2 = get_value_from_rect(settings.game_x + 528 - 2, settings.game_y + 425 - 29 + 49, settings.game_x + 605 - 2, settings.game_y + 505 - 29)
        power3 = get_value_from_rect(settings.game_x + 818 - 2, settings.game_y + 425 - 29 + 49, settings.game_x + 890 - 2, settings.game_y + 505 - 29)
        enter_lowest(power1, power2, power3, False)
    else:
        log("Coliseum done")
        escape(1)