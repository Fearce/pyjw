import pyautogui
import time
import os
import tkinter
import threading
import random
import datetime
import winsound
import sys
import pygubu
from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

##Images
daily_reward_2 = 'imgs/daily_reward_2.PNG'

arch_escape = 'imgs/escape1.PNG'
arch_available = 'imgs/archavailable.png'

arena_available = 'imgs/arenaavailable.png'

heros_button = 'imgs/herosbutton.png'

skill_points_available = 'imgs/skillpointsavailable.PNG'
skill_points_available15 = 'imgs/15skillpoints.PNG'
skill_points_available0 = 'imgs/0skillpoints.PNG'
skill_point_add = 'imgs/skillpointadd.PNG'
skill_points_power = 'imgs/skillpointspower.PNG'
skill_points_need = 'imgs/needsomeskillpoints.PNG'


chest_available = 'imgs/chestavailable.PNG'
free_wood_chest = 'imgs/freewoodchest.PNG'


friend_currency = 'imgs/friend_currency.PNG'
friend_send = 'imgs/friend_send.PNG'
friend_gifts = 'imgs/friend_gifts.PNG'
friend_gift_send = 'imgs/friend_gift_send.PNG'
friend_collect = 'imgs/friend_collect.PNG'
friend_thank = 'imgs/friend_thank.PNG'
friend_gold = 'imgs/friend_gold.PNG'

sell_button = 'imgs/sell_button.PNG'

facebook_send = 'imgs/facebook_send.PNG'

cash_offer = 'imgs/cash_offer.PNG'

##Functions
def log(msg):
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + ": " + msg)

def click_on_image(img, name, confidence):
    imgBox = pyautogui.locateOnScreen(img, confidence=confidence)
    if imgBox is not None:
        centerPoints = pyautogui.center(imgBox)
        pyautogui.click(centerPoints)
        print("Clicking: " + name + " @ " + str(centerPoints))
        return centerPoints
    return None

def skill_points():
    log("Checking skill points")
    points = click_on_image(heros_button, "Heroes", 0.8)
    time.sleep(1.5)
    pyautogui.click(points)
    time.sleep(1.5)
    skillPointsBook = pyautogui.locateOnScreen(skill_points_available, confidence=0.8)
    if skillPointsBook is not None:
        pyautogui.click(pyautogui.center(skillPointsBook))
        time.sleep(1.5)
    skillPointsMaxed = pyautogui.locateOnScreen(skill_points_available15, confidence=0.95)
    if skillPointsMaxed is not None:
        # If skill points are available
        log("Skill points available, trying to distribute.")
        for x in range(0, 20):  # Do skills 20 times
            skillAddBox = pyautogui.locateOnScreen(skill_point_add, confidence=0.95)  # Find the + for adding skillpoints
            needBox = pyautogui.locateOnScreen(skill_points_need, confidence=0.8)
            zeroBox = pyautogui.locateOnScreen(skill_points_available0, confidence=0.8)
            # When you have skillpoints, add them
            while skillAddBox is not None and needBox is None and zeroBox is None:
                pyautogui.click(pyautogui.center(skillAddBox))
                time.sleep(0.2)
                skillAddBox = pyautogui.locateOnScreen(skill_point_add, confidence=0.95)
                time.sleep(0.2)
            # When it doesn't exist, click on next hero
            powBox = pyautogui.locateOnScreen(skill_points_power, confidence=0.8)
            if powBox is not None and needBox is None and zeroBox is None:
                powBoxCoords = pyautogui.center(powBox)
                x, y = powBoxCoords
                pyautogui.click(x-65, y+280)
                time.sleep(0.2)
        log("Skill points distributed")
    else:
        log("15 skill points not ready, waiting for next cycle")
        time.sleep(4)
        click_on_image(arch_escape, "Escaping", 0.8)
        time.sleep(4)
        click_on_image(arch_escape, "Escaping", 0.8)


def arch_event():
    log("Checking Arch Event")
    click_on_image(arch_available, "Arch Event", 0.8)

def check_chests():
    log("Checking for chests")
    chests = click_on_image(chest_available, "Chests", 0.95)
    if chests is not None:
        time.sleep(1)
        click_on_image(free_wood_chest, "Wooden Chest", 0.7)
        time.sleep(4)
        click_on_image(arch_escape, "Reward received", 0.8)
        time.sleep(4)
        click_on_image(arch_escape, "No more chests, leaving", 0.8)


def check_friends():
    log("Checking for friend currency")
    heart = click_on_image(friend_currency, "Friend Heart", 0.88)
    if heart is not None:
        time.sleep(2)
        click_on_image(friend_send, "Send Button", 0.88)
        time.sleep(4)
        click_on_image(facebook_send, "Facebook send button", 0.88)
    log("Checking for gifts from friends")
    friends = click_on_image(friend_gifts, "Friend Heart", 0.88)
    if friends is not None:
        time.sleep(2)
        collect = click_on_image(friend_collect, "Collect", 0.88)
        if collect is not None:
            time.sleep(2)
            thank = click_on_image(friend_thank, "Thanks", 0.88)
            if thank is not None:
                time.sleep(4)
                click_on_image(facebook_send, "Facebook send button", 0.88)
            gold = click_on_image(friend_gold, "gold", 0.88)
            if gold is not None:
                x, y = gold
                pyautogui.click(x, y - 280)
                time.sleep(2)
        send = click_on_image(friend_gift_send, "Send", 0.88)
        if send is not None:
            time.sleep(4)
            click_on_image(facebook_send, "Facebook send button", 0.88)


def check_shops():
    log("Checking for shop activity")
    sell = click_on_image(sell_button, "Sell Button", 0.9)
    if sell is not None:
        time.sleep(2)
        click_on_image(arch_escape, "Items sold, leaving", 0.8)

def check_daily_rewards():
    log("Checking for daily rewards")
    reward_2 = pyautogui.locateOnScreen(daily_reward_2, confidence=0.9)
    if reward_2 is not None:
        reward_2_Coords = pyautogui.center(reward_2)
        x, y = reward_2_Coords
        pyautogui.click(x+20, y-60)
        time.sleep(2)
        pyautogui.click(x - 20, y - 250)
        time.sleep(2)
        click_on_image(arch_escape, "Daily quest item 2 taken, leaving", 0.8)

def close_adds():
    fb = click_on_image(facebook_send, "Facebook send button", 0.88)
    if fb is not None:
        time.sleep(2)
        click_on_image(arch_escape, "Add closed, leaving", 0.8)
    cash = pyautogui.locateOnScreen(cash_offer, confidence=0.9)
    if cash is not None:
        time.sleep(2)
        click_on_image(arch_escape, "Add closed, leaving", 0.8)


##Main loop
def main():
    close_adds()
    # Daily rewards
    check_daily_rewards()
    close_adds()

    # Chests
    check_chests()
    close_adds()

    # Friend currency
    check_friends()
    close_adds()

    # Shops
    check_shops()
    close_adds()

    # Skill points
    skill_points()
    close_adds()


    # Arch


    # Arena

    # Trial of Death



    # Wait 30 sec and start over
    log("Checks done, waiting 20 seconds and restarting")
    time.sleep(20)
    main()

##Init
if __name__ == '__main__':
    main()
