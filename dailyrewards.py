from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

def click_daily_rewards2():
    pyautogui.click(settings.game_x + 320 - 138, settings.game_y + 485 - 146)  # click each reward once
    time.sleep(0.5)
    pyautogui.click(settings.game_x + 508 - 138, settings.game_y + 410 - 146)
    time.sleep(0.5)
    pyautogui.click(settings.game_x + 686 - 138, settings.game_y + 485 - 146)
    time.sleep(0.5)
    pyautogui.click(settings.game_x + 876 - 138, settings.game_y + 416 - 146)
    time.sleep(0.5)
    pyautogui.click(settings.game_x + 1046 - 138, settings.game_y + 485 - 146)
    time.sleep(0.5)
    pyautogui.click(settings.game_x + 1205 - 138, settings.game_y + 423 - 146)
    time.sleep(0.5)
    escape(2)


def click_daily_rewards():
    if not settings.daily_rewards:
        return
    log("Clicking all the rewards")
    pyautogui.click(settings.game_x + 320 - 138, settings.game_y + 485 - 146)  # click each reward once
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 320 - 138, settings.game_y + 485 - 146)  # click each reward once
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 320 - 138, settings.game_y + 485 - 146)  # click each reward once
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 320 - 138, settings.game_y + 485 - 146)  # click each reward once
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 508 - 138, settings.game_y + 410 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 508 - 138, settings.game_y + 410 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 508 - 138, settings.game_y + 410 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 508 - 138, settings.game_y + 410 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 686 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 686 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 686 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 686 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 876 - 138, settings.game_y + 416 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 876 - 138, settings.game_y + 416 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 876 - 138, settings.game_y + 416 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 876 - 138, settings.game_y + 416 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1046 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1046 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1046 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1046 - 138, settings.game_y + 485 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1205 - 138, settings.game_y + 423 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1205 - 138, settings.game_y + 423 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1205 - 138, settings.game_y + 423 - 146)
    time.sleep(0.2)
    pyautogui.click(settings.game_x + 1205 - 138, settings.game_y + 423 - 146)
    time.sleep(0.2)
    click(632, 649)
    time.sleep(0.2)
    click(632, 649)
    time.sleep(0.2)
    click(632, 649)
    time.sleep(0.2)
    click(632, 649)
    time.sleep(0.2)
    escape(2)