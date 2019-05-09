# User settings
resolution_x = 1280  # Game window resolution width
resolution_y = 800  # Game window resolution height
wait_time = 1  # Amount of seconds to wait between each cycle
amount_heroes = 67
tod_comp1 = ["Elf_Maiden_Alisia", "Ninja_Meego", "Tagath_the_Potionbrewer", "Norak_the_Virtuous", "General_Kurbatov"]
tod_comp2 = ["Nymph_Edera", "Naga_Kertana", "Drowned_Samara", "Beastborn_Raider_Miaba", "Master_Hideus"]
tod_comp3 = ["Arzgar_the_Herald_of_Death", "Hitay_the_Spirit_of_Flame", "Crystalloid_Vern", "Samurai_Yasi",
             "Guard_Langerd"]
tod_comp4 = ["Healer_Cassandra", "Necromancer_Khardur", "Ronald_the_Inquisitor", "Gorbakh_the_Tyrant",
             "Superslug_Caliban"]
campaign_heroes = ["Ninja_Meego", "Hanna_the_Inquisitor", "Beastborn_Warrior_Grog",
                   "Assassin_Torus", "Fire_Eril", "Crystallon_Rarh"]

settings_all = False  # If this is set to true everything is enabled
#### Enable / disable features
arena = False
campaign = False
caves = False
cave_max_power = 39000
chests = False
coliseum = False
daily_rewards = False
events = False
friends = False
mailbox = False
tournament = False
trial_of_death = False

missions = False  # Disable Missions to stop all missions
missions_all = False  # Exchanging, experience potions, enchanting, friend currency


portal = False  # Disable Portal to stop checking it altogether
trials = True
otherworld = True
otherworld_bash = True  # This will keep fighting until the otherworld is complete

# Clan Castle
clan_castle = False  # Disable all clan castle features
treasury = False
clan_store = True
praises = False
caravan = False
altar = False
brawls = False
wheel = False
raids = False

# Hero upgrades
skill_points = False  # Add skill points, takes a while, so disable if no need
leveling = False  # To use this, set to true, it takes a while to scroll past all heroes, so disable if no need
current_level = 86  # Set the level you wish to level heroes to
elevating = False
equipping = False

# Store options
clan_heroes = ["Superslug_Caliban", "Amok_the_Prince_of_Naga"]

#### End of settings

# Game variables
current_state = "Offline"
game_x = 0
game_y = 0

x_scaling = 1280 / resolution_x
y_scaling = 800 / resolution_y

settings_array = [arena, campaign, caves, chests, clan_castle, coliseum, daily_rewards, events, friends,
                  mailbox, missions, tournament, trial_of_death, portal, trials, otherworld, treasury,
                  clan_store, praises, caravan, altar, brawls, wheel, raids, skill_points, leveling, elevating,
                  equipping, otherworld_bash]
