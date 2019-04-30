from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

def check_skill_points():
    click(508, 720)  # Click heroes button
    time.sleep(2)
    click(140, 260)  # Click first hero
    time.sleep(1)
    click(1180, 350)  # Click skill book
    points = get_value_from_rect(settings.game_x+759, settings.game_y+198, settings.game_x+795, settings.game_y+225)
    log(str(points))
    time.sleep(20)
