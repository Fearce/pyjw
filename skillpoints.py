from helpers import delay_next_check, log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings
import datetime

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run


def check_skill_points():
    global last_check
    # delay_msg = "Checked skillpoints at " + str(last_check) + ". Waiting until 30 minutes has passed"
    if delay_next_check(30, last_check):
        return

    heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
    if heroes_button_located is not None:
        last_check = datetime.datetime.now()
        log("Checking skill points")
        click(508, 720)  # Click heroes button
        time.sleep(2)
        click(140, 260)  # Click first hero
        time.sleep(2)
        click(1180, 350)  # Click skill book
        time.sleep(2)
        points = get_value_from_rect(settings.game_x + 759, settings.game_y + 198, settings.game_x + 795,
                                     settings.game_y + 225)
        log(str(points))
        log("Distributing points")
        for x in range(0, settings.amount_heroes):
            try:
                log("distributing point " + str(x))
                if int(points) < 1:
                    log("No points, breaking")
                    break
                #click(1056, 337)  # Skill points 1-3
                #time.sleep(0.2)
                #click(1056, 500)
                #time.sleep(0.2)
                #click(1056, 650)
                time.sleep(0.4)
                skill_add = pyautogui.locateOnScreen('imgs/skillpointadd.png', confidence=0.99)
                if skill_add is None:
                    time.sleep(0.4)
                    click(493, 400)  # Next hero
                    log("hero is filled, checking next")
                else:
                    time.sleep(0.4)
                    log("adding point")
                    click_on_box(skill_add)
                    time.sleep(0.2)
                points = get_value_from_rect(settings.game_x + 759, settings.game_y + 198, settings.game_x + 795,
                                             settings.game_y + 225)
                log(str(points))
            except ValueError:
                log("Tesseract error, waiting until next cycle")
                escape(1)
                break
        log("Done distributing points")
        escape(2)
