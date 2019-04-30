from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

def refresh_cave():
    pyautogui.click(game_x+905, game_y+544)  # click cave
    time.sleep(1.5)
    pyautogui.click(game_x+370, game_y+419)  # click gold
    time.sleep(1.5)
    pyautogui.click(game_x+780, game_y+124)  # accept gold
    time.sleep(1)
    pyautogui.click(game_x+780, game_y+124)  # click tantalum cave
    time.sleep(1)
    pyautogui.click(game_x + 370, game_y + 419)  # click xp
    time.sleep(1)
    pyautogui.click(game_x+780, game_y+124)  # accept xp
    time.sleep(1)
    pyautogui.click(game_x + 370, game_y + 419)  # click xp
    time.sleep(1)
    pyautogui.click(game_x+1012, game_y+725)  # set up all
    time.sleep(1)
    escape(3)