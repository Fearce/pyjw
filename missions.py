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
    missions = click_on_image(missions_available, "Missions", 0.9)
    if missions is not None:
        time.sleep(2)
        reward = click_on_image(missions_reward, "Reward", 0.9)
        if reward is not None:
            time.sleep(1)
            pyautogui.click(reward)
        pyautogui.drag(0, -400, 0.5, button='left')
        time.sleep(2.5)
        cont = click_on_image(missions_continue, "Continue", 0.9)
        if cont is not None:
            x, y = cont
            time.sleep(2.5)
            pyautogui.click(x, y-290)
            time.sleep(2.5)
        # Campaign-mission clicked, correct
        camp_arrow = pyautogui.locateOnScreen(mission_campaign_arrow, confidence=0.9)
        if camp_arrow is not None:
            soul_stones(False)
    escape()