import datetime

from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    delay_next_check
from heroselection import enter_lowest
import pyautogui
import time
import settings

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run

def check_arena():
    global last_check
    if delay_next_check(5, last_check):
        return
    click_image('imgs/arena_ready.PNG', "Checking Arena", do_arena_battle)
    #arena_ready = pyautogui.locateOnScreen('imgs/arena_ready.PNG', confidence=0.95)
    #if arena_ready is not None:
    #    log("Arena ready")
    #    click_on_box(arena_ready)
    #    time.sleep(3)
    #    pyautogui.click(settings.game_x + 1095 - 33, settings.game_y + 487 - 49)
    #    time.sleep(1)
    #    do_arena_battle()


def do_arena_battle():
    no_battles_ready = pyautogui.locateOnScreen('imgs/no_battles_ready.PNG', confidence=0.97)
    waiting = pyautogui.locateOnScreen('imgs/dont_wait.PNG', confidence=0.97)
    if no_battles_ready is None and waiting is None:
        log("Arena battles available. Doing Battle!")
        power1 = get_value_from_rect(settings.game_x+241-2, settings.game_y+425-29+49, settings.game_x+325-2, settings.game_y+505-29)
        power2 = get_value_from_rect(settings.game_x + 528 - 2, settings.game_y + 425 - 29 + 49, settings.game_x + 605 - 2, settings.game_y + 505 - 29)
        power3 = get_value_from_rect(settings.game_x + 818 - 2, settings.game_y + 425 - 29 + 49, settings.game_x + 890 - 2, settings.game_y + 505 - 29)
        enter_lowest(power1, power2, power3, True)
    else:
        log("Not ready for arena battle")
        escape(1)