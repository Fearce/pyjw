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
                    time.sleep(1)
                    ad_close = pyautogui.locateOnScreen('imgs/ad_close.png', confidence=0.75)
                    if ad_close is None:
                        ad_close = pyautogui.locateOnScreen('imgs/ad_close2.png', confidence=0.75)
                        if ad_close is None:
                            ad_close = pyautogui.locateOnScreen('imgs/add_close.png', confidence=0.75)
                    if ad_close is not None:
                        click_on_box(ad_close)
                        log("Ad closed")
                    else:
                        log("Problem with closing ad, escaping")
                        escape(1)
                        return
                    #wait_on_img('imgs/herosbutton.png', 0.9, 60)
                    #escape(1)
                    return

        # After or no rewards
        log("No rewards, leaving missions")
        if settings.missions_all:
            for x in range(0, 5):
                log("Looking for mission")
                go_down()
                time.sleep(1)
            missions_continue = pyautogui.locateOnScreen('imgs/missions_continue.png', confidence=0.9)
            if missions_continue is not None:
                log("Mission found, doing missions!")
                click_on_box(missions_continue)
                time.sleep(2) # Wait for mission to be clicked
                do_mission()
        # sapphire_for_gold - turn - escape
        # experience_potion_mission - apply - click blue - escape2
        # enchant_mission - click orange_item or purple_item - click enchant_item - click enchant_go - escape2

        escape(1)
    else:
        log("Can't find missions")

def do_mission():
    time.sleep(2)
    hero_power = pyautogui.locateOnScreen('imgs/hero_power.png', confidence=0.9)
    if hero_power is not None:
        enchant_mission()
        do_mission()

    sapphire_for_gold = pyautogui.locateOnScreen('imgs/sapphire_for_gold.png', confidence=0.9)
    if sapphire_for_gold is not None:
        sapphire_for_gold_mission()
        do_mission()

    experience_potion_mission = pyautogui.locateOnScreen('imgs/experience_potion_mission.png', confidence=0.9)
    if experience_potion_mission is not None:
        experience_mission()
        do_mission()


def experience_mission():
    log("TODO")
    log("Doing experience potion mission")
    apply = pyautogui.locateOnScreen('imgs/apply.png', confidence=0.9)
    if apply is not None:
        log("Clicking apply")
        click_on_box(apply)
        time.sleep(1)
        escape(1)

def sapphire_for_gold_mission():
    log("Doing sapphire for gold mission")
    turn = pyautogui.locateOnScreen('imgs/turn.png', confidence=0.9)
    if turn is not None:
        log("Clicking turn")
        click_on_box(turn)
        time.sleep(1)
        escape(1)

def enchant_mission():
    log("Doing enchanting mission")
    empty_star_orange = pyautogui.locateOnScreen('imgs/empty_star_orange.png', confidence=0.9)
    empty_star_purple = pyautogui.locateOnScreen('imgs/empty_star_purple.png', confidence=0.9)
    if empty_star_orange is not None or empty_star_purple is not None:
        log("Clicking item to be enchanted")
        if empty_star_orange is not None:
            click_on_box(empty_star_orange)
        else:
            click_on_box(empty_star_purple)
        time.sleep(2)
        enchant_item = pyautogui.locateOnScreen('imgs/enchant_item.png', confidence=0.9)
        if enchant_item is not None:
            log("Clicking enchanting material")
            click_on_box(enchant_item)
            time.sleep(2)
            enchant_go = pyautogui.locateOnScreen('imgs/enchant_go.png', confidence=0.9)
            if enchant_go is not None:
                log("Enchanting item and escaping")
                click_on_box(enchant_go)
                escape(2)