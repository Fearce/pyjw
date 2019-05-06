from helpers import delay_next_check, log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, \
    click, click_next
import pyautogui
import time
import settings
import datetime


def check_upgrades():
    log("Searching for equipment & Elevation upgrades")
    log("Checking levels")
