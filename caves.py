import datetime
from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check
import pyautogui
import time
import settings

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run

def check_cave():
    global last_check
    # delay_msg = "Checked skillpoints at " + str(last_check) + ". Waiting until 30 minutes has passed"
    if delay_next_check(20, last_check):
        return
    last_check = datetime.datetime.now()

    log("Checking Cave")
    cave_ready = pyautogui.locateOnScreen('imgs/cave_ready.png', confidence=0.88)
    if cave_ready is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/cave_ready.png', "Cave", refresh_cave)
    else:
        click_on_box(cave_ready)
        refresh_cave()


def refresh_cave():
    #pyautogui.click(settings.game_x+905, settings.game_y+544)  # click cave
    time.sleep(1.5)
    pyautogui.click(settings.game_x+370, settings.game_y+419)  # click gold
    time.sleep(0.2)
    cave_output = pyautogui.locateOnScreen('imgs/cave_output.png', confidence=0.85)
    if cave_output is not None:
        log("Cave currently running")
        escape(2)
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
    escape(3)
