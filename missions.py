from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next
import pyautogui
import time
import settings

missions_available = 'imgs/missions_available.PNG'
missions_reward = 'imgs/missions_reward.PNG'
missions_continue = 'imgs/missions_continue.PNG'
mission_campaign_arrow = 'imgs/mission_campaign_arrow.PNG'


def check_missions():
    log("Checking missions")
    missions = pyautogui.locateOnScreen(missions_available, confidence=0.9)
    if missions is not None:
        click_on_box(missions)
        time.sleep(2)
        reward = pyautogui.locateOnScreen(missions_reward, confidence=0.9)
        while reward is not None:  # Click all rewards
            time.sleep(1)
            click_on_box(reward)
            time.sleep(2)
            click_on_box(reward)
            time.sleep(1)
            reward = pyautogui.locateOnScreen(missions_reward, confidence=0.9)
        log("No rewards, leaving missions")
        escape(1)
    else:
        log("Can't find missions")
