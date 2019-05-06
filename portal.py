import datetime
from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check
import pyautogui
import time
import settings

last_check = datetime.datetime.now()
last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run

def check_portal():
    global last_check
    if not settings.portal:
        return
    # delay_msg = "Checked skillpoints at " + str(last_check) + ". Waiting until 30 minutes has passed"
    if delay_next_check(20, last_check):
        return
    log("Checking portal")
    portal = pyautogui.locateOnScreen('imgs/portal.png', confidence=0.85)
    last_check = datetime.datetime.now()
    if portal is None:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is None:
            return
        look_for_button('imgs/portal.png', "Portal", portal_work)
    else:
        click_on_box(portal)
        portal_work()


def portal_work():
    check_trial()
    check_otherworld()


def check_trial():
    if not settings.trials:
        return
    time.sleep(1)
    trial_ready = pyautogui.locateOnScreen('imgs/trial_ready.png', confidence=0.85)
    if trial_ready is not None:
        log("Clicking trial")
        click_on_box(trial_ready)
        time.sleep(4)
        do_trial()
        escape(2)
    else:
        log("Trial not available")
        #escape(1)


def do_trial():
    trial_middle = pyautogui.locateOnScreen('imgs/trial_middle.png', confidence=0.9)
    if trial_middle is not None:
        click_on_box(trial_middle)
        time.sleep(4)
        click_on_box(trial_middle)
        time.sleep(2)
        trial_vip = pyautogui.locateOnScreen('imgs/trial_vip.png', confidence=0.9)
        if trial_vip is not None:  # Vip 3 battle x5 first
            click_on_box(trial_vip)
        else:  # Else normal autobattle
            auto_battle = pyautogui.locateOnScreen('imgs/trial_autobattle.png', confidence=0.75)
            if auto_battle is not None:
                click_on_box(auto_battle)
        time.sleep(3)
        escape(4)
        #to_battle = pyautogui.locateOnScreen('imgs/to_battle.png', confidence=0.75)
        #if to_battle is not None:
        #    click_on_box(to_battle)


def check_otherworld():
    if not settings.otherworld:
        return
    time.sleep(1)
    otherworld_ready = pyautogui.locateOnScreen('imgs/otherworld_ready.png', confidence=0.85)
    if otherworld_ready is not None:
        log("Clicking otherworld")
        click_on_box(otherworld_ready)
        time.sleep(4)
        do_otherworld()
        escape(2)
    else:
        log("Otherworld not available")
        escape(1)

def do_otherworld():
    otherworld_current = pyautogui.locateOnScreen('imgs/otherworld_current.png', confidence=0.8)
    if otherworld_current is not None:
        click_on_box(otherworld_current)
        time.sleep(4)
        otherworld_battle = pyautogui.locateOnScreen('imgs/otherworld_battle.png', confidence=0.8)
        if otherworld_battle is not None:
            click_on_box(otherworld_battle)
        time.sleep(5)
        escape(4)
        #trial_vip = pyautogui.locateOnScreen('imgs/trial_vip.png', confidence=0.9)
        #if trial_vip is not None:  # Vip 3 battle x5 first
        #    click_on_box(trial_vip)
        #else:  # Else normal autobattle
        #    auto_battle = pyautogui.locateOnScreen('imgs/trial_autobattle.png', confidence=0.75)
        #    if auto_battle is not None:
        #        click_on_box(auto_battle)
        #time.sleep(3)
        #escape(5)
        # to_battle = pyautogui.locateOnScreen('imgs/to_battle.png', confidence=0.75)
        # if to_battle is not None:
        #    click_on_box(to_battle)


def otherworld_brute_force():
    log("todo spam otherworld for hours")