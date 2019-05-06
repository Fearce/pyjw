from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings
import datetime


def check_events():
    if not settings.events:
        return
    log("checking events")