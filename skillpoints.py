from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings


def check_skill_points():
    heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
    if heroes_button_located is not None:
        click(508, 720)  # Click heroes button
        time.sleep(2)
        click(140, 260)  # Click first hero
        time.sleep(1)
        click(1180, 350)  # Click skill book
        points = get_value_from_rect(settings.game_x + 759, settings.game_y + 198, settings.game_x + 795,
                                     settings.game_y + 225)
        log(str(points))
        log("Distributing points")
        for x in range(0, settings.amount_heroes):
            try:
                if int(points) < 1:
                    break
                click(1056, 337)
                time.sleep(0.2)
                click(1056, 500)
                time.sleep(0.2)
                click(1056, 650)
                time.sleep(0.2)
                click(493, 400)
                points = get_value_from_rect(settings.game_x + 759, settings.game_y + 198, settings.game_x + 795,
                                             settings.game_y + 225)
                log(str(points))
                log("Done distributing points")
                time.sleep(20)
            except ValueError:
                log("Tesseract error, waiting until next cycle")
                break
