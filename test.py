import handlers
from campaign import check_campaign
from clancastle import check_treasury, check_caravan, check_praises, check_raids, check_wheel_of_fortune, check_altar, \
    check_clan_store, check_clan_castle, do_raids
from helpers import log, locate_game_window, get_value_from_rect, click_on_box, escape, click_image, click, click_next, \
    speed_up_battle, wait_on_img
from dailyrewards import click_daily_rewards
from caves import check_cave, do_cave_fights, get_cave_gold
from missions import check_missions
from portal import check_portal
from skillpoints import check_skill_points
from tournament import check_tournament
from trialofdeath import check_trial_of_death, do_trial_of_death, finish_trial
from coliseum import check_coliseum, do_coliseum
from arena import check_arena, do_arena_battle
from chests import check_chests
from friends import check_friends
from mailbox import check_mailbox
from events import check_events
import settings
from heroselection import select_heroes, deselect_heroes, select_arena_heroes, select_tod_heroes, select_hero, \
    enter_lowest
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
import pytesseract

from upgrades import check_upgrades

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def detect_game_state():
    reward_for_support = pyautogui.locateOnScreen('imgs/reward_for_support.PNG', confidence=1)
    if reward_for_support is not None:
        settings.current_state = "Reward!"
        log("Taking reward")
        click_on_box(reward_for_support)
        time.sleep(60)
        escape(1)
        return

    add_close_located = pyautogui.locateOnScreen('imgs/add_close.PNG', confidence=0.95)
    if add_close_located is not None:
        settings.current_state = "Advertisement"
        log("Escaping ad")
        escape(1)
        return

    daily_rewards = 'imgs\daily_rewards.PNG'
    daily_rewards_located = pyautogui.locateOnScreen(daily_rewards, confidence=0.95)
    if daily_rewards_located is not None:
        settings.current_state = "Daily Rewards"
        return

    heroes_button_located = pyautogui.locateOnScreen('imgs/herosbutton2.png', confidence=0.98)
    escape_sign_located = pyautogui.locateOnScreen('imgs/escape1.PNG', confidence=0.95)
    if heroes_button_located is not None:
        log("Heroes button located")
        if escape_sign_located is not None:
            settings.current_state = "Clan Castle"
            return
        else:
            settings.current_state = "Home Screen"
            return

    tod_win = pyautogui.locateOnScreen('imgs/tod_win.png', confidence=0.88)
    if tod_win is not None:
        if escape_sign_located is not None:
            settings.current_state = "Trial Win"
            return

    arena_available_battles = pyautogui.locateOnScreen('imgs/arena_available_battles.png', confidence=0.98)
    if arena_available_battles is not None:
        if escape_sign_located is not None:
            settings.current_state = "Arena"
            return

    state_cave_battle = pyautogui.locateOnScreen('imgs/state_cave_battle.png', confidence=0.95)
    if state_cave_battle is not None:
        if escape_sign_located is not None:
            settings.current_state = "Cave Battles"
            return

    in_cave = pyautogui.locateOnScreen('imgs/in_cave.png', confidence=0.85)
    if in_cave is not None:
        if escape_sign_located is not None:
            settings.current_state = "Cave"
            return

    cave_buy = pyautogui.locateOnScreen('imgs/cave_buy.png', confidence=0.8)
    if cave_buy is not None:
        if cave_buy is not None:
            log("Escaping cave buy")
            escape(2)
            return

    walk_through_tod = pyautogui.locateOnScreen('imgs/walk_through_tod.png', confidence=0.98)
    if walk_through_tod is not None:
        if escape_sign_located is not None:
            settings.current_state = "Trial of Death"
            return

    power = pyautogui.locateOnScreen('imgs/power.png', confidence=0.95)
    battle_start = pyautogui.locateOnScreen('imgs/battle_start.png', confidence=0.95)
    if power is not None and battle_start is not None:
        settings.current_state = "Hero Select"
        return

    next_button = pyautogui.locateOnScreen('imgs/next.png', confidence=0.95)
    if next_button is not None:
        settings.current_state = "Victory"
        return

    auto_on = pyautogui.locateOnScreen('imgs/auto_on.png', confidence=0.95)
    if auto_on is not None:
        settings.current_state = "In Battle"
        speed_up_battle()
        return

    clan_raids = pyautogui.locateOnScreen('imgs/clan_raids.png', confidence=0.95)
    if clan_raids is not None:
        settings.current_state = "Clan Raids"
        return
    else:
        settings.current_state = "Working"


def escape_on_disable(func):
    if not settings.enabled:
        return
    else:
        func()


def home_screen_func(func):
    detect_game_state()
    if settings.current_state != "Home Screen":
        log("Wrong state, escaping")
        escape(1)
        return
        #do_work()
    else:
        log("Game state is : " + settings.current_state)
        escape_on_disable(func)
        time.sleep(1)


def clan_castle_func(func):
    detect_game_state()
    if settings.current_state != "Clan Castle":
        log("Wrong state, escaping")
        escape(1)
        return
        #do_work()
    else:
        escape_on_disable(func)
        time.sleep(1)


fail_count = 0


def do_work():
    global fail_count
    if settings.current_state == "Cave Battles":
        log("Cave fight")
        escape_on_disable(do_cave_fights)

    if settings.current_state == "Cave":
        log("Getting cave gold")
        escape_on_disable(get_cave_gold)
        click(888, 500)
        escape(1)

    #if settings.current_state == "In Battle":

    if settings.current_state == "Trial Win":
        log("Trial finish")
        escape_on_disable(finish_trial)

    if settings.current_state == "Daily Rewards":
        log("Daily rewards")
        escape_on_disable(click_daily_rewards)

    if settings.current_state == "Clan Castle":
        if settings.treasury:
            clan_castle_func(check_treasury)
        if settings.clan_store:
            clan_castle_func(check_clan_store)
        if settings.caravan:
            clan_castle_func(check_caravan)
        if settings.praises:
            clan_castle_func(check_praises)
        if settings.wheel:
            clan_castle_func(check_wheel_of_fortune)
        if settings.altar:
            clan_castle_func(check_altar)
        if settings.raids:
            clan_castle_func(check_raids)
        escape(1)

    if settings.current_state == "Trial of Death":
        log("In trial")
        escape_on_disable(do_trial_of_death)

    if settings.current_state == "Hero Select":
        log("Escaping hero select")
        escape(2)

    if settings.current_state == "Victory":
        log("Victory")
        click_next()

    if settings.current_state == "Home Screen" or settings.current_state == "Clan Castle":
        log("Upgrades")
        check_upgrades()

    if settings.current_state == "Home Screen":
        arrow_expand = pyautogui.locateOnScreen('imgs/arrow_expand.png', confidence=0.95)
        if arrow_expand is not None:
            log("Expanding arrow")
            click_on_box(arrow_expand)
        if settings.arena:
            log("Arena check")
            home_screen_func(check_arena)
        if settings.trial_of_death:
            log("trial_of_death check")
            home_screen_func(check_trial_of_death)
        if settings.skill_points:
            log("skill_points check")
            home_screen_func(check_skill_points)
        if settings.coliseum:
            log("coliseum check")
            home_screen_func(check_coliseum)
        if settings.tournament:
            log("tournament check")
            home_screen_func(check_tournament)
        if settings.events:
            log("events check")
            home_screen_func(check_events)
        if settings.caves:
            log("caves check")
            log(settings.current_state)
            home_screen_func(check_cave)
        if settings.chests:
            log("chests check")
            home_screen_func(check_chests)
        if settings.mailbox:
            log("mailbox check")
            home_screen_func(check_mailbox)
        if settings.missions:
            log("missions check")
            home_screen_func(check_missions)
        if settings.friends:
            log("friends check")
            home_screen_func(check_friends)
        if settings.portal:
            log("portal check")
            home_screen_func(check_portal)
        if settings.campaign:
            log("campaign check")
            home_screen_func(check_campaign)
        if settings.clan_castle:
            log("clan_castle check")
            home_screen_func(check_clan_castle)

    if settings.current_state == "Clan Raids":
        log("Clan raids")
        do_raids()

    if settings.current_state == "Arena":
        log("Arena state")
        do_arena_battle()

        # home_screen_func(check_upgrades)

    if settings.current_state == "Working":
        log("Unknown game state, trying to correct")
        fail_count += 1
        # escape(1)
        # time.sleep(2)
        jw_help = pyautogui.locateOnScreen('imgs/jw_help.png', confidence=1)
        if jw_help is not None:
            log("Selecting game")
            click_on_box(jw_help)
            time.sleep(60)
        jw_facebook = pyautogui.locateOnScreen('imgs/jw_facebook.png', confidence=0.95)
        if jw_facebook is not None:
            log("Closing facebook tab")
            click_on_box(jw_facebook)
        ad_close = pyautogui.locateOnScreen('imgs/ad_close.png', confidence=0.95)
        if ad_close is not None:
            log("Closing ad")
            click_on_box(ad_close)
        escape(1)
        if fail_count > 5:
            fail_count = 0
            log("Something wrong, restarting game")
            game_exit = pyautogui.locateOnScreen('imgs/game_exit.png', confidence=0.95)
            if game_exit is not None:
                log("Exiting game")
                click_on_box(game_exit)
                time.sleep(2)
                jw_game = pyautogui.locateOnScreen('imgs/jw_game.png', confidence=0.95)
                if jw_game is not None:
                    log("Starting game")
                    click_on_box(jw_game)
                    wait_on_img('imgs/herosbutton.png', 0.9, 360)

def main_loop(args):
    settings.current_state = "Working"

    # Detect game state
    detect_game_state()
    log("Current state is: " + settings.current_state)

    # Act on game state
    do_work()

    # Wait wait_time sec and start over
    log("Cycle done, waiting " + str(settings.wait_time) + " seconds and restarting")
    # settings.current_state = "Waiting"
    if settings.current_state == "Home Screen":
        time.sleep(settings.wait_time)
    else:
        time.sleep(1)
    return main_loop, (args,)


class Application:
    def __init__(self, master):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('pyjw.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('jw_frame', master)

        # Configure callbacks
        callbacks = {
            'start_stop': handlers.start_stop,
            'settings_all': handlers.enable_disable_all,
            'settings_arena': handlers.arena,

        }

        builder.connect_callbacks(callbacks)


def program():
    global main_loop, args
    try:
        log('Press CTRL-ALT-Delete to quit or close the program.')
        if settings.enabled:
            settings.game_x, settings.game_y = locate_game_window()
            main_loop, args = main_loop("Start")
        else:
            return
        while True:
            if not settings.enabled:
                return
            main_loop, args = main_loop(*args)
    except KeyboardInterrupt:
        print('\n')
    except pyautogui.FailSafeException:
        log("Stopping")


def start_program():
    time.sleep(1)  # Wait a few secs to load GUI
    program()


# Init
if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=start_program)
    thread.start()
    settings.root = tkinter.Tk()
    settings.app = Application(settings.root)
    settings.root.title("Juggernaut Wars Bot")
    # print(app.builder.get_variable('attack_status'))
    # test_variable()
    # print(app.builder.get_variable('attack_status'))
    settings.root.mainloop()
