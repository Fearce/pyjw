from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, go_left, go_right
import pyautogui
import time
import settings

drag_count = 0

def check_chests():
    global drag_count
    chest = pyautogui.locateOnScreen('imgs/chestavailable.png', confidence=0.88)
    if chest is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        for x in range(0, 20):  # Look for chest 20 times or give up
            time.sleep(2)
            chest = pyautogui.locateOnScreen('imgs/chestavailable.png', confidence=0.88)
            if chest is not None:
                log("Chest button found, clicking")
                click_on_box(chest)
                time.sleep(2)
                open_chests()
                break
            log("Looking for chest button")
            if drag_count < 5:
                go_right()
            else:
                go_left()
            drag_count += 1
            # log(str(drag_count))
            if drag_count > 9:
                drag_count = 0
            # check_chests()
    else:
        click_on_box(chest)


def open_chests():
    chest = pyautogui.locateOnScreen('imgs/freewoodchest.png', confidence=0.88)
    if chest is not None:
        log("Opening wooden chest")
        click_on_box(chest)
        time.sleep(4)
        escape(2)
    else:
        log("No chests available")
        escape(1)
