from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    delay_next_check
import pyautogui
import time
import settings
import datetime

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


def check_events():
    global last_check
    if not settings.events:
        return
    #if delay_next_check(5, last_check):
    #    return
    event = pyautogui.locateOnScreen('imgs/event.PNG', confidence=0.92)
    if event is not None:
        log("Checking event.")
        last_check = datetime.datetime.now()
        click_on_box(event)
        check_lab()
        check_wayback()
        check_magic()
        check_tree_of_life()

lab_done = False
def check_lab():
    global lab_done
    if lab_done:
        log("Laboratory already done, escaping")
        escape(2)
        return
    time.sleep(1)
    laboratory = pyautogui.locateOnScreen('imgs/laboratory.PNG', confidence=0.88)
    if laboratory is not None:
        log("Laboratory of the Alchemist event found.")
        time.sleep(1)
        lab_three = pyautogui.locateOnScreen('imgs/lab_three.PNG', confidence=0.88)
        if lab_three is not None:
            click_on_box(lab_three)
            time.sleep(2)
            click(1040, 610)
            time.sleep(3)
            lab_done = True
        escape(3)


wayback_done = 0
def check_wayback():
    global wayback_done
    if wayback_done >= 2:
        log("Way back home already done, escaping")
        escape(2)
        return
    time.sleep(1)
    wayback = pyautogui.locateOnScreen('imgs/wayback.PNG', confidence=0.88)
    if wayback is not None:
        log("Way back home event found.")
        time.sleep(1)
        lab_three = pyautogui.locateOnScreen('imgs/lab_three.PNG', confidence=0.88)
        if lab_three is not None:
            click_on_box(lab_three)
            time.sleep(2)
            click(1024, 700)
            wayback_done += 1
            time.sleep(3)
        escape(3)


tree_of_life_done = 0
def check_tree_of_life():
    global tree_of_life_done
    if tree_of_life_done >= 2:
        log("Tree of Life already done, escaping")
        escape(2)
        return
    time.sleep(1)
    wayback = pyautogui.locateOnScreen('imgs/tree_of_life.PNG', confidence=0.88)
    if wayback is not None:
        log("Tree of Life event found.")
        time.sleep(1)
        lab_three = pyautogui.locateOnScreen('imgs/lab_three.PNG', confidence=0.88)
        if lab_three is not None:
            click_on_box(lab_three)
            time.sleep(2)
            click(1024, 700)
            tree_of_life_done += 1
            time.sleep(3)
        escape(3)

        
        
magic_done = False
def check_magic():
    global magic_done
    if magic_done:
        log("Magic against the power already done, escaping")
        escape(2)
        return
    time.sleep(1)
    magic = pyautogui.locateOnScreen('imgs/magic.PNG', confidence=0.88)
    if magic is not None:
        log("Magic against the power event found.")
        time.sleep(1)
        magic_three = pyautogui.locateOnScreen('imgs/lab_three.PNG', confidence=0.88)
        if magic_three is not None:
            click_on_box(magic_three)
            time.sleep(2)
            click(1024, 700)
            time.sleep(3)
            magic_done = True
        escape(3)
