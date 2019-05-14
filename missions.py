import datetime

from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    delay_next_check, wait_on_img, go_down, wait_on_ad
import pyautogui
import time
import settings

missions_t = 'imgs/missions.PNG'
missions_available = 'imgs/missions_available.PNG'
missions_reward = 'imgs/missions_reward.PNG'
missions_continue = 'imgs/missions_continue.PNG'
mission_campaign_arrow = 'imgs/mission_campaign_arrow.PNG'

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


# ad_watch
def check_missions():
    global last_check
    if delay_next_check(2, last_check):
        return
    log("Checking missions")
    last_check = datetime.datetime.now()
    missions = pyautogui.locateOnScreen(missions_t, confidence=0.9)
    if missions is not None:
        click_on_box(missions)
        time.sleep(2)
        # Rewards
        reward = pyautogui.locateOnScreen(missions_reward, confidence=0.9)
        while reward is not None:  # Click all rewards
            time.sleep(1)
            click_on_box(reward)
            time.sleep(2)
            click_on_box(reward)
            time.sleep(1)
            reward = pyautogui.locateOnScreen(missions_reward, confidence=0.9)
            if reward is None:
                ad_watch = pyautogui.locateOnScreen('imgs/ad_watch.png', confidence=0.9)
                time.sleep(1)
                if ad_watch is not None:
                    click_on_box(ad_watch)
                    time.sleep(3)
                    accept = pyautogui.locateOnScreen('imgs/unity_accept.png', confidence=0.9)
                    if accept is not None:
                        click_on_box(accept)
                    # log("Giving ad 45 seconds to finish")
                    log("Waiting for ad to finish")
                    wait_on_ad(0.75, 60)
                    ad_close = pyautogui.locateOnScreen('imgs/ad_close.png', confidence=0.75)
                    click_on_box(ad_close)
                    log("Ad closed")
                    #wait_on_img('imgs/herosbutton.png', 0.9, 60)
                    #escape(1)
                    return

        # After or no rewards
        log("No rewards, leaving missions")
        if settings.missions_all:
            for x in range(0, 5):
                go_down()
                time.sleep(1)
            missions_continue = pyautogui.locateOnScreen('imgs/missions_continue.png', confidence=0.9)
            if missions_continue is not None:
                click_on_box(missions_continue)
        # sapphire_for_gold - turn - escape
        # experience_potion_mission - apply - click blue - escape2
        # enchant_mission - click orange_item or purple_item - click enchant_item - click enchant_go - escape2

        escape(1)
    else:
        log("Can't find missions")
