import datetime

from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check
import pyautogui
import time
import settings
from main import campaign_chapters

current_food = 0

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run

def get_food():
    global current_food
    food = get_value_from_rect(settings.game_x + 1013, settings.game_y + 16, settings.game_x + 1060,
                                 settings.game_y + 43)
    try:
        food = int(food)
        current_food = food
        log("Current food is: " + str(food))
    except ValueError:
        food = get_value_from_rect(settings.game_x + 1013, settings.game_y + 16, settings.game_x + 1050,
                                   settings.game_y + 43)
        try:
            food = int(food)
            current_food = food
            log("Current food is: " + str(food))
        except ValueError:
            log("Can't read food")



def check_campaign():
    global last_check
    get_food()
    if delay_next_check(20, last_check):
        return
    last_check = datetime.datetime.now()
    log("Checking Campaign")
    if current_food > 40 and current_food != 97 and current_food != 11:
        log("Trying to spend food")
        click(512, 725)
        time.sleep(1.5)
        for hero in settings.campaign_heroes:
            hero_collection = pyautogui.locateOnScreen('imgs/hero_collection.PNG', confidence=0.9)
            if hero_collection is None:
                break
            log("Checking " + hero)
            time.sleep(1)
            farm_stones(hero)
            time.sleep(1)
        escape(1)


def farm_stones(hero):
    img = pyautogui.locateOnScreen('imgs/heroesbig/'+hero+'.PNG', confidence=0.88)
    if img is not None:
        click_on_box(img)
        time.sleep(2)
        get_food()
        if current_food < 30:
            return
        click(820, 719)
        time.sleep(2)
        campaign_chapters()
        time.sleep(1)
        escape(3)