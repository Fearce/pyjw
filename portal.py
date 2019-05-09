import datetime
from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    go_left, go_right, look_for_button, delay_next_check, wait_on_img
import pyautogui
import time
import settings

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour - 1)  # Remove 1 hour to make sure it checks first run


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
    trial_ready = pyautogui.locateOnScreen('imgs/trial_ready2.png', confidence=0.9)
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
    x = 640
    y = 430
    trial_middle = pyautogui.locateOnScreen('imgs/trial_middle.png', confidence=0.9)
    if trial_middle is None:
        trial_middle = pyautogui.locateOnScreen('imgs/trial_right.png', confidence=0.9)
        x = 1035
    if trial_middle is None:
        trial_middle = pyautogui.locateOnScreen('imgs/trial_left.png', confidence=0.9)
        x = 245
    if trial_middle is not None:
        #click_on_box(trial_middle)
        click(x, y)
        time.sleep(4)
        #click_on_box(trial_middle)
        click(640, 430)
        time.sleep(2)
        trial_vip = pyautogui.locateOnScreen('imgs/trial_vip.png', confidence=0.9)
        if trial_vip is not None:  # Vip 3 battle x5 first
            click_on_box(trial_vip)
        else:  # Else normal autobattle
            auto_battle = pyautogui.locateOnScreen('imgs/trial_autobattle.png', confidence=0.75)
            if auto_battle is not None:
                click_on_box(auto_battle)
        time.sleep(3)
        escape(2)
        #to_battle = pyautogui.locateOnScreen('imgs/to_battle.png', confidence=0.75)
        #if to_battle is not None:
        #    click_on_box(to_battle)


def check_otherworld():
    if not settings.otherworld:
        return
    time.sleep(2)
    otherworld_ready = pyautogui.locateOnScreen('imgs/otherworld_ready2.png', confidence=0.91)
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
    otherworld_new = pyautogui.locateOnScreen('imgs/otherworld_new.png', confidence=0.9)
    if otherworld_new is not None:
        log("New otherworld week, starting highest diff")
        click(630, 430)
        time.sleep(1)
        click(630, 440)
    otherworld_current = pyautogui.locateOnScreen('imgs/otherworld_current.png', confidence=0.8)
    if otherworld_current is not None:
        log("Doing current otherworld")
        click_on_box(otherworld_current)
        time.sleep(4)
        otherworld_battle = pyautogui.locateOnScreen('imgs/otherworld_battle.png', confidence=0.8)
        if otherworld_battle is not None:
            log("Doing otherworld battle")
            click_on_box(otherworld_battle)
        else:
            otherworld_bash()
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


def otherworld_bash():
    global completed
    log("Starting otherworld bash, make sure the composition you want to use is selected")
    completed = False
    while completed is False:
        bash_complete = pyautogui.locateOnScreen('imgs/bash_complete.png', confidence=0.8)
        if bash_complete is not None:
            log("No more attempts")
            completed = True
            break
        click(1051, 700)  # Start battle
        time.sleep(5)
        click(198, 715)   # Speed up
        time.sleep(1)
        click(198, 715)   # Speed up
        time.sleep(3)
        wait_on_img('imgs/bash_next.png', 0.8, 200)
        click(1150, 500)  # Next
        time.sleep(3)
        otherworld_current = pyautogui.locateOnScreen('imgs/otherworld_current.png', confidence=0.8)
        if otherworld_current is not None:
            log("Doing current otherworld")
            click_on_box(otherworld_current)
            time.sleep(4)
    escape(2)
