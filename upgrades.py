from helpers import delay_next_check, log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, \
    click, click_next, go_right, wait_on_img, go_up_far, go_down
import pyautogui
import time
import settings
import datetime

last_check = datetime.datetime.now()
if last_check.hour == 0:
    last_check = last_check.replace(minute=0)
else:
    last_check = last_check.replace(hour=last_check.hour-1)  # Remove 1 hour to make sure it checks first run


def check_upgrades():
    global last_check
    if delay_next_check(20, last_check):
        return
    last_check = datetime.datetime.now()
    #log("Searching for equipment & Elevation upgrades")
    if settings.leveling or settings.equipping or settings.elevating:
        log("Checking upgrades")
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is not None:
            click_on_box(heroes_button_located)
            time.sleep(2)

        if settings.leveling:
            click(164, 300)
            time.sleep(1)
            click(1080,111)

            wait_on_img('imgs/giant_experience_potion.png', 0.9, 50)
            giant_experience_potion = pyautogui.locateOnScreen('imgs/giant_experience_potion.png', confidence=0.9)
            if giant_experience_potion is not None:
                click_on_box(giant_experience_potion)
                time.sleep(0.3)
                click(360, 715)  # Apply
                time.sleep(3)
                for y in range(0, 10):
                    go_up_far()  # Go to top
                time.sleep(2)
                give_levels()

                #log("What now boss?")
                #time.sleep(20)

        for x in range(0, 10):
            upgrade_elevate = pyautogui.locateOnScreen('imgs/upgrade_elevate.png', confidence=0.95)
            upgrade_equipment = pyautogui.locateOnScreen('imgs/upgrade_equipment.png', confidence=0.95)
            if upgrade_elevate is not None and settings.elevating:
                click_on_box(upgrade_elevate)
                do_upgrade()
                return
                #break
            if upgrade_equipment is not None and settings.equipping:
                click_on_box(upgrade_equipment)
                do_upgrade()
                return
                #break
            power_stone = pyautogui.locateOnScreen('imgs/power_stone.png', confidence=0.95)
            if power_stone is not None:
                log("End reached, escaping")
                escape(1)
                return
            log(str(x))
            for y in range(0, 6):
                go_right()
            time.sleep(1)
    #log("Checking levels")
    #log("Checking elevation")
    #log("Checking equip")


def give_levels():
    bad_level_number = settings.current_level-1
    bad_level = pyautogui.locateOnScreen('imgs/levels/'+str(bad_level_number)+'.png', confidence=0.98)
    if bad_level is not None:
        log("Giving xp")
        center_points = pyautogui.center(bad_level)
        for x in range(0, 20):
            pyautogui.click(center_points)
            time.sleep(0.001)
        give_levels()
    else:
        bottom = pyautogui.locateOnScreen('imgs/levels/bottom.png', confidence=0.99)
        if bottom is not None:
            log("Reached bottom, leaving")
            escape(3)
            return
        go_down()
        give_levels()



def do_upgrade():
    time.sleep(3)
    log("Doing upgrade")
    elevate = pyautogui.locateOnScreen('imgs/elevate.png', confidence=0.85)
    evolve = pyautogui.locateOnScreen('imgs/elevate.png', confidence=0.85)
    promote = pyautogui.locateOnScreen('imgs/promote.png', confidence=0.85)
    if evolve is None:
        evolve = pyautogui.locateOnScreen('imgs/evolve2.png', confidence=0.85)
    if elevate is not None or evolve is not None or promote is not None:
        log("Elevating/Evolving hero")
        if elevate is not None:
            click_on_box(elevate)
        elif promote is not None:
            click_on_box(promote)
        else:
            click_on_box(evolve)
            time.sleep(2)
            click(640, 460)
        time.sleep(2)
        click(464, 676)  # Elevate
        time.sleep(1)
        escape(4)
        #check_upgrades()
        return

    equipment_upgrade = pyautogui.locateOnScreen('imgs/equipment_upgrade.png', confidence=0.95)
    if equipment_upgrade is not None:
        log("Equipping item")
        click_on_box(equipment_upgrade)
        time.sleep(2)
        equipment_missing = pyautogui.locateOnScreen('imgs/equipment_missing.png', confidence=0.88)
        while equipment_missing is not None:
            click_on_box(equipment_missing)
            time.sleep(1)
            click(1063, 720)  # Assemble
            time.sleep(1)
            click(776, 418)  # Continue
            equipment_missing = pyautogui.locateOnScreen('imgs/equipment_missing.png', confidence=0.88)
            # To be continued
        time.sleep(1)
        click(1030, 723)  # Assemble
        time.sleep(1)
        click(776, 418)  # Continue
        time.sleep(3.5)
        click(335, 720)  # Equip
        time.sleep(1)
        escape(1)
        #check_upgrades()
        return

    equipment_give = pyautogui.locateOnScreen('imgs/equipment_give.png', confidence=0.95)
    if equipment_give is not None:
        log("Equipping item")
        click_on_box(equipment_give)
        time.sleep(2)
        click(816, 623)  # Equip
        time.sleep(3.5)
        escape(1)
        #check_upgrades()
        return

