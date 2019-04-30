from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

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


def finish_trial():
    pyautogui.click(game_x+580, game_y+725)
    time.sleep(1.5)
    pyautogui.click(game_x+770, game_y+430)
    time.sleep(1)