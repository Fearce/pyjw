import threading

import pyjw
import settings
import multiprocessing
from helpers import log


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, func):
        super(StoppableThread, self).__init__(target=func)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def start_stop():
    global thread
    # log("Pressed button")
    if settings.enabled:
        log("Bot disabled")
        change_var('start_stop_string', "Enable bot")
        settings.enabled = False
        thread.stop()
        raise Exception('Program disabled')
    else:
        log("Bot enabled")
        change_var('start_stop_string', "Disable bot")
        settings.enabled = True
        threading.stack_size(200000000)
        # thread = multiprocessing.Process(target=test.program)
        thread = StoppableThread(pyjw.program)
        # thread = threading.Thread()
        thread.start()


def change_var(var_name, new_string):
    var = settings.app.builder.get_variable(var_name)
    var.set(new_string)


all_settings = False


def enable_disable_all():
    global all_settings
    if all_settings:
        log("Disabling all settings")
        settings.app.builder.get_variable("arena_check").set(False)
        settings.arena = False
        settings.app.builder.get_variable("tod_check").set(False)
        settings.trial_of_death = False
        settings.app.builder.get_variable("campaign_check").set(False)
        settings.campaign = False
        settings.app.builder.get_variable("caves_check").set(False)
        settings.caves = False
        settings.app.builder.get_variable("chests_check").set(False)
        settings.chests = False
        settings.app.builder.get_variable("coliseum_check").set(False)
        settings.coliseum = False
        settings.app.builder.get_variable("daily_rewards_check").set(False)
        settings.daily_rewards = False
        settings.app.builder.get_variable("events_check").set(False)
        settings.events = False
        settings.app.builder.get_variable("all_missions_check").set(False)
        settings.missions_all = False
        settings.app.builder.get_variable("mailbox_check").set(False)
        settings.mailbox = False
        settings.app.builder.get_variable("tournament_check").set(False)
        settings.tournament = False
        settings.app.builder.get_variable("missions_check").set(False)
        settings.missions = False
        settings.app.builder.get_variable("portal_check").set(False)
        settings.portal = False
        settings.app.builder.get_variable("trials_check").set(False)
        settings.trials = False
        settings.app.builder.get_variable("otherworld_check").set(False)
        settings.otherworld = False
        settings.app.builder.get_variable("otherworld_bash_check").set(False)
        settings.otherworld_bash = False
        settings.app.builder.get_variable("clan_castle_check").set(False)
        settings.clan_castle = False
        settings.app.builder.get_variable("treasury_check").set(False)
        settings.treasury = False
        settings.app.builder.get_variable("clan_store_check").set(False)
        settings.clan_store = False
        settings.app.builder.get_variable("praises_check").set(False)
        settings.praises = False
        settings.app.builder.get_variable("caravan_check").set(False)
        settings.caravan = False
        settings.app.builder.get_variable("altar_check").set(False)
        settings.altar = False
        settings.app.builder.get_variable("brawls_check").set(False)
        settings.brawls = False
        settings.app.builder.get_variable("wheel_check").set(False)
        settings.wheel = False
        settings.app.builder.get_variable("raids_check").set(False)
        settings.raids = False
        settings.app.builder.get_variable("skill_points_check").set(False)
        settings.skill_points = False
        settings.app.builder.get_variable("leveling_check").set(False)
        settings.leveling = False
        settings.app.builder.get_variable("elevating_check").set(False)
        settings.elevating = False
        settings.app.builder.get_variable("equipping_check").set(False)
        settings.equipping = False
        settings.app.builder.get_variable("friends_check").set(False)
        settings.friends = False
        all_settings = False
        for x in settings.settings_array:
            x = False
    else:
        log("Enabling all settings")
        settings.app.builder.get_variable("arena_check").set(True)
        settings.arena = True
        settings.app.builder.get_variable("tod_check").set(True)
        settings.trial_of_death = True
        settings.app.builder.get_variable("campaign_check").set(True)
        settings.campaign = True
        settings.app.builder.get_variable("caves_check").set(True)
        settings.caves = True
        settings.app.builder.get_variable("chests_check").set(True)
        settings.chests = True
        settings.app.builder.get_variable("coliseum_check").set(True)
        settings.coliseum = True
        settings.app.builder.get_variable("daily_rewards_check").set(True)
        settings.daily_rewards = True
        settings.app.builder.get_variable("events_check").set(True)
        settings.events = True
        settings.app.builder.get_variable("all_missions_check").set(True)
        settings.missions_all = True
        settings.app.builder.get_variable("mailbox_check").set(True)
        settings.mailbox = True
        settings.app.builder.get_variable("tournament_check").set(True)
        settings.tournament = True
        settings.app.builder.get_variable("missions_check").set(True)
        settings.missions = True
        settings.app.builder.get_variable("portal_check").set(True)
        settings.portal = True
        settings.app.builder.get_variable("trials_check").set(True)
        settings.trials = True
        settings.app.builder.get_variable("otherworld_check").set(True)
        settings.otherworld = True
        settings.app.builder.get_variable("otherworld_bash_check").set(True)
        settings.otherworld_bash = True
        settings.app.builder.get_variable("clan_castle_check").set(True)
        settings.clan_castle = True
        settings.app.builder.get_variable("treasury_check").set(True)
        settings.treasury = True
        settings.app.builder.get_variable("clan_store_check").set(True)
        settings.clan_store = True
        settings.app.builder.get_variable("praises_check").set(True)
        settings.praises = True
        settings.app.builder.get_variable("caravan_check").set(True)
        settings.caravan = True
        settings.app.builder.get_variable("altar_check").set(True)
        settings.altar = True
        settings.app.builder.get_variable("brawls_check").set(True)
        settings.brawls = True
        settings.app.builder.get_variable("wheel_check").set(True)
        settings.wheel = True
        settings.app.builder.get_variable("raids_check").set(True)
        settings.raids = True
        settings.app.builder.get_variable("skill_points_check").set(True)
        settings.skill_points = True
        settings.app.builder.get_variable("leveling_check").set(True)
        settings.leveling = True
        settings.app.builder.get_variable("elevating_check").set(True)
        settings.elevating = True
        settings.app.builder.get_variable("equipping_check").set(True)
        settings.equipping = True
        settings.app.builder.get_variable("friends_check").set(True)
        settings.friends = True
        #log(str(var.get()))
        #var.set(True)
        #log(str(var.get()))
        #settings.root.nametowidget("check_arena").Select()
        all_settings = True
        for x in settings.settings_array:
            x = True


def arena():
    if settings.arena:
        #log("Disabling arena")
        settings.arena = False
    else:
        #log("Enabling arena")
        settings.arena = True


def campaign():
    if settings.campaign:
        settings.campaign = False
    else:
        settings.campaign = True


def caves():
    if settings.caves:
        settings.caves = False
    else:
        settings.caves = True


cave_max_power = 39000


def chests():
    if settings.chests:
        settings.chests = False
    else:
        settings.chests = True


def coliseum():
    if settings.coliseum:
        settings.coliseum = False
    else:
        settings.coliseum = True


def daily_rewards():
    if settings.daily_rewards:
        settings.daily_rewards = False
    else:
        settings.daily_rewards = True


def events():
    if settings.events:
        settings.events = False
    else:
        settings.events = True


def friends():
    if settings.friends:
        settings.friends = False
    else:
        settings.friends = True


def mailbox():
    if settings.mailbox:
        settings.mailbox = False
    else:
        settings.mailbox = True


def tournament():
    if settings.tournament:
        settings.tournament = False
    else:
        settings.tournament = True


def trial_of_death():
    if settings.trial_of_death:
        settings.trial_of_death = False
    else:
        settings.trial_of_death = True


def missions():
    if settings.missions:
        settings.missions = False
    else:
        settings.missions = True


#missions_all = False  # Exchanging, experience potions, enchanting, friend currency
def missions_all():
    if settings.missions_all:
        settings.missions_all = False
    else:
        settings.missions_all = True

def portal():
    if settings.portal:
        settings.portal = False
    else:
        settings.portal = True


def trials():
    if settings.trials:
        settings.trials = False
    else:
        settings.trials = True


def otherworld():
    if settings.otherworld:
        settings.otherworld = False
    else:
        settings.otherworld = True


def otherworld_bash():
    if settings.otherworld_bash:
        settings.otherworld_bash = False
    else:
        settings.otherworld_bash = True


# Clan Castle
def clan_castle():
    if settings.clan_castle:
        settings.clan_castle = False
    else:
        settings.clan_castle = True


def treasury():
    if settings.treasury:
        settings.treasury = False
    else:
        settings.treasury = True


def clan_store():
    if settings.clan_store:
        settings.clan_store = False
    else:
        settings.clan_store = True


def praises():
    if settings.praises:
        settings.praises = False
    else:
        settings.praises = True


def caravan():
    if settings.caravan:
        settings.caravan = False
    else:
        settings.caravan = True


def altar():
    if settings.altar:
        settings.altar = False
    else:
        settings.altar = True


def brawls():
    if settings.brawls:
        settings.brawls = False
    else:
        settings.brawls = True


def wheel():
    if settings.wheel:
        settings.wheel = False
    else:
        settings.wheel = True


def raids():
    if settings.raids:
        settings.raids = False
    else:
        settings.raids = True


# Hero upgrades
def skill_points():
    if settings.skill_points:
        settings.skill_points = False
    else:
        settings.skill_points = True


def leveling():
    if settings.leveling:
        settings.leveling = False
    else:
        settings.leveling = True


current_level = 86  # Set the level you wish to level heroes to


def elevating():
    if settings.elevating:
        settings.elevating = False
    else:
        settings.elevating = True


def equipping():
    if settings.equipping:
        settings.equipping = False
    else:
        settings.equipping = True
