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

from helpers import wait_on_img, click_on_box, click

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

##Images
daily_reward_2 = 'imgs/daily_reward_2.PNG'
daily_reward_3 = 'imgs/daily_reward_3.PNG'


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

locked_treasure = 'imgs/locked_treasure.PNG'

cash_offer = 'imgs/cash_offer.PNG'

missions_available = 'imgs/missions_available.PNG'
missions_reward = 'imgs/missions_reward.PNG'
missions_continue = 'imgs/missions_continue.PNG'
mission_campaign_arrow = 'imgs/mission_campaign_arrow.PNG'

max_food = 'imgs/max_food.PNG'
heroes_find_soul_stones = 'imgs/heroes_find_soul_stones.PNG'
soul_stones_battle_ready = 'imgs/soul_stones_battle_ready.PNG'
soul_stones_battle_ready1 = 'imgs/soul_stones_battle_ready1.PNG'
soul_stones_battle_ready2 = 'imgs/soul_stones_battle_ready2.PNG'

heroes_hanna = 'imgs/heroes_hanna.PNG'
heroes_meego = 'imgs/heroes_meego.PNG'

battle_start = 'imgs/battle_start.PNG'
to_battle = 'imgs/to_battle.PNG'

mailbox_available = 'imgs/mailbox_available.PNG'
mailbox_receive = 'imgs/mailbox_receive.PNG'

menu_expand = 'imgs/menu_expand.PNG'

in_the_name_of_the_light = 'imgs/in_the_name_of_the_light.PNG'

next_button = 'imgs/next.PNG'



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
        for x in range(0, 2):  # Do skills 20 times
            skillAddBox = pyautogui.locateOnScreen(skill_point_add, confidence=0.95)  # Find the + for adding skillpoints
            needBox = pyautogui.locateOnScreen(skill_points_need, confidence=0.8)
            zeroBox = pyautogui.locateOnScreen(skill_points_available0, confidence=0.8)
            # When you have skillpoints, add them
            counter = 0
            while skillAddBox is not None and needBox is None and zeroBox is None and counter < 5:
                if needBox is None and zeroBox is None:
                    needBox = pyautogui.locateOnScreen(skill_points_need, confidence=0.8)
                    zeroBox = pyautogui.locateOnScreen(skill_points_available0, confidence=0.8)
                if needBox is not None or zeroBox is not None:
                    break
                pyautogui.click(pyautogui.center(skillAddBox))
                time.sleep(0.2)
                skillAddBox = pyautogui.locateOnScreen(skill_point_add, confidence=0.95)
                time.sleep(0.2)
                counter += 1
            # When it doesn't exist, click on next hero
            powBox = pyautogui.locateOnScreen(skill_points_power, confidence=0.8)
            if powBox is not None and needBox is None and zeroBox is None:
                powBoxCoords = pyautogui.center(powBox)
                x, y = powBoxCoords
                pyautogui.click(x-65, y+280)
                time.sleep(0.2)
        log("Skill points distributed")
        escape()
    else:
        log("15 skill points not ready, waiting for next cycle")
        escape()



def check_chests():
    log("Checking for chests")
    chests = click_on_image(chest_available, "Chests", 0.95)
    if chests is not None:
        time.sleep(1)
        click_on_image(free_wood_chest, "Wooden Chest", 0.7)
        time.sleep(4)
        click_on_image(arch_escape, "Reward received", 0.8)
        time.sleep(1.5)
        click_on_image(arch_escape, "No more chests, leaving", 0.8)


def check_friends2():
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
                wait_on_img(facebook_send, 0.88, 120)
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
    escape()


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
        click_on_image(arch_escape, "Daily reward item 2 taken, leaving", 0.8)
    reward_3 = pyautogui.locateOnScreen(daily_reward_3, confidence=0.9)
    if reward_3 is not None:
        reward_3_Coords = pyautogui.center(reward_3)
        x, y = reward_3_Coords
        pyautogui.click(x + 20, y - 60)
        time.sleep(2)
        pyautogui.click(x - 20, y - 250)
        time.sleep(2)
        click_on_image(arch_escape, "Daily reward item 3 taken, leaving", 0.8)

def close_adds():
    expand = click_on_image(menu_expand, "Missions", 0.9)
    if expand is not None:
        log("Menu is hidden, fixing")
        time.sleep(1)
    next_b = click_on_image(next_button, "Next button", 0.88)
    if next_b is not None:
        time.sleep(2)
        click_on_image(arch_escape, "Fight done, leaving", 0.8)
    fb = click_on_image(facebook_send, "Facebook send button", 0.88)
    if fb is not None:
        time.sleep(2)
        click_on_image(arch_escape, "Add closed, leaving", 0.8)
    cash = pyautogui.locateOnScreen(cash_offer, confidence=0.9)
    if cash is not None:
        time.sleep(2)
        click_on_image(arch_escape, "Add closed, leaving", 0.8)
    escape()

def campaign_chapters():
    for y in range(0, 3):
        campaign_chapters2()

def campaign_chapters2():
    for x in range(0, 2):
        count = 3
        rdy = click_on_image(soul_stones_battle_ready, "Chapter 3/3", 0.95)
        if rdy is None:
            rdy = click_on_image(soul_stones_battle_ready1, "Chapter 1/3", 0.95)
            count = 1
        if rdy is None:
            count = 2
            rdy = click_on_image(soul_stones_battle_ready2, "Chapter 2/3", 0.95)
        if rdy is not None:
            for y in range(0, count):
                time.sleep(1.5)
                coords = click_on_image(battle_start, "Start battle!", 0.9)
                time.sleep(2)
                pyautogui.click(coords)
                ask_for_food = pyautogui.locateOnScreen('imgs/in_cave.png', confidence=0.85)
                if ask_for_food is not None:
                    click_on_box(ask_for_food)
                    time.sleep(2)
                    click(540, 655)
                    time.sleep(1)
                    click(900, 662)
                    time.sleep(3)
                    click(891, 95)
                    time.sleep(1)
                    import helpers
                    helpers.escape(4)
                    return

            import helpers
            helpers.escape(2)


def soul_stones(need_food):
    food_max = pyautogui.locateOnScreen(max_food, confidence=0.95)
    if food_max is not None or need_food is False:
        log("Food is maxed or coming from missions, getting soul stones")
        heroes = click_on_image(heros_button, "Heroes", 0.8)
        time.sleep(1.5)
        # Hanna check
        click_on_image(heroes_hanna, "Hanna", 0.8)
        time.sleep(1.5)
        click_on_image(heroes_find_soul_stones, "Plus", 0.8)
        time.sleep(1.5)
        campaign_chapters()
        escape()
        heroes = click_on_image(heros_button, "Heroes", 0.8)
        time.sleep(1.5)
        # Meego check
        click_on_image(heroes_meego, "Meego", 0.8)
        time.sleep(1.5)
        click_on_image(heroes_find_soul_stones, "Plus", 0.8)
        time.sleep(1.5)
        for x in range(0, 2):
            count = 3
            rdy = click_on_image(soul_stones_battle_ready, "Chapter 3/3", 0.95)
            if rdy is None:
                rdy = click_on_image(soul_stones_battle_ready1, "Chapter 1/3", 0.95)
                count = 1
            if rdy is None:
                count = 2
                rdy = click_on_image(soul_stones_battle_ready2, "Chapter 2/3", 0.95)
            if rdy is not None:
                for y in range(0, count):
                    time.sleep(1.5)
                    coords = click_on_image(battle_start, "Start battle!", 0.9)
                    time.sleep(4)
                    pyautogui.click(coords)
        escape()


def escape():
    esc = click_on_image(arch_escape, "Escaping", 0.8)
    if esc is not None:
        time.sleep(1)
    esc1 = click_on_image(arch_escape, "Escaping", 0.8)
    if esc1 is not None:
        time.sleep(1)
    esc2 = click_on_image(arch_escape, "Escaping", 0.8)
    if esc2 is not None:
        time.sleep(1)
    esc3 = click_on_image(arch_escape, "Escaping", 0.8)
    if esc3 is not None:
        time.sleep(1)
    if esc is not None:
        x, y = esc
        for x in range(0, 10):
            pyautogui.move(-12, 0)
            pyautogui.drag(12, 0, 0.1, button='left')

def check_mailbox():
    log("Checking mailbox")
    mbox = click_on_image(mailbox_available, "Mailbox", 0.9)
    if mbox is not None:
        time.sleep(1.5)
        rec = click_on_image(mailbox_receive, "Mailbox", 0.9)
        if rec is not None:
            time.sleep(1.5)
            pyautogui.click(rec)
            time.sleep(1.5)
            click_on_image(arch_escape, "Reward received, leaving", 0.8)

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


def check_events():
    log("Checking events")
    check_itnotl_event()


def check_itnotl_event():
    current_level = 2
    event = click_on_image(in_the_name_of_the_light, "ITNOTL event", 0.9)
    if event is not None:
        log("In the Name of the Light event found.")
        time.sleep(1.5)
        if current_level == 2:
            click_on_image('imgs/itnotl_2.PNG', "Level 2", 0.9)
            time.sleep(1.5)
            click_on_image(to_battle, "To Battle", 0.9)
            time.sleep(20)


def arch_event():
    log("Checking Arch Event")
    click_on_image(arch_available, "Arch Event", 0.8)




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
    #check_friends()
    close_adds()

    # Shops
    check_shops()
    close_adds()

    # Skill points
    skill_points()
    close_adds()

    # Mailbox
    check_mailbox()

    # Soul stones
    soul_stones(True)
    close_adds()

    # Missions
    check_missions()
    close_adds()

    # Events
    check_events()
    close_adds()

    # Arena

    # Trial of Death



    # Wait 30 sec and start over
    log("Checks done, waiting 20 seconds and restarting")
    time.sleep(20)
    close_adds()
    main()

##Init
if __name__ == '__main__':
    main()
