from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

def click_daily_rewards(game_x, game_y):
    pyautogui.click(game_x + 320 - 138, game_y + 485 - 126)  # click each reward once
    time.sleep(0.5)
    pyautogui.click(game_x + 508 - 138, game_y + 410 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 686 - 138, game_y + 485 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 876 - 138, game_y + 416 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 1046 - 138, game_y + 485 - 126)
    time.sleep(0.5)
    pyautogui.click(game_x + 1205 - 138, game_y + 423 - 126)
    time.sleep(0.5)
    escape(2)