from helpers import delay_next_check, log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, \
    click, click_next, go_right
import pyautogui
import time
import settings
import datetime


def check_upgrades():
    #log("Searching for equipment & Elevation upgrades")
    if settings.leveling or settings.equipping or settings.elevating:
        heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton.png', confidence=0.95)
        if heroes_button_located is not None:
            click_on_box(heroes_button_located)
            time.sleep(2)
        for x in range(0,60):
            upgrade_elevate = pyautogui.locateOnScreen('imgs/upgrade_elevate.png', confidence=0.95)
            upgrade_equipment = pyautogui.locateOnScreen('imgs/upgrade_equipment.png', confidence=0.95)
            if upgrade_elevate is not None:
                click_on_box(upgrade_elevate)
                do_upgrade()
                break
            if upgrade_equipment is not None:
                click_on_box(upgrade_equipment)
                do_upgrade()
                break
            log(str(x))
            go_right()
            time.sleep(1)
    #log("Checking levels")
    #log("Checking elevation")
    #log("Checking equip")


def do_upgrade():
    time.sleep(2)
    elevate = pyautogui.locateOnScreen('imgs/elevate.png', confidence=0.95)
    if elevate is not None:
        click_on_box(elevate)
        time.sleep(2)
        click(464, 676)  # Elevate
        time.sleep(1)
        escape(3)

    equipment_upgrade = pyautogui.locateOnScreen('imgs/equipment_upgrade.png', confidence=0.95)
    if equipment_upgrade is not None:
        click_on_box(equipment_upgrade)
        time.sleep(2)
        click(1030, 723)  # Assemble
        time.sleep(3.5)
        click(335, 720)  # Equip
        time.sleep(1)
        escape(1)

