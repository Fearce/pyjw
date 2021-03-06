import datetime
import pyautogui
import time
import pytesseract
import settings
from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def delay_next_check(delay_min, last_check):
    now = datetime.datetime.now()
    if now.minute >= delay_min:
        now = now.replace(minute=now.minute - delay_min)
    else:
        try:
            now = now.replace(hour=now.hour - 1)
            for x in range(0, delay_min - now.minute):
                now = now.replace(minute=now.minute + 1)
        except ValueError:
            log("Value error, time is changing")
    if now < last_check:
        # log(delay_msg)
        # return True  # Uncomment to allow delays
        return False
    return False


def wait_on_ad(conf, amount):
    ad_closes = ['imgs/ad_close.PNG', 'imgs/ad_close2.PNG', 'imgs/add_close.PNG']
    count = 0
    found = pyautogui.locateOnScreen('imgs/ad_close.PNG', confidence=conf)
    while found is None:
        count += 1  # Fail safe to stop after 480 attempts at locating image
        if count > amount:
            break
        time.sleep(0.25)
        for x in ad_closes:
            if found is None:
                found = pyautogui.locateOnScreen(x, confidence=conf)
            else:
                break


def wait_on_img(img, conf, amount):
    count = 0
    found = pyautogui.locateOnScreen(img, confidence=conf)
    while found is None:
        count += 1  # Fail safe to stop after 'amount' attempts at locating image.
        if count > amount:
            break
        time.sleep(0.25)
        found = pyautogui.locateOnScreen(img, confidence=conf)


def go_up():
    pyautogui.moveTo(settings.game_x + 630, settings.game_y + 365)
    time.sleep(0.2)
    pyautogui.drag(0, 90, 0.2, button='left')


def go_up_far():
    pyautogui.moveTo(settings.game_x + 630, settings.game_y + 365)
    time.sleep(0.1)
    pyautogui.drag(0, 300, 0.2, button='left')


def go_down():
    pyautogui.moveTo(settings.game_x + 630, settings.game_y + 365)
    time.sleep(0.1)
    pyautogui.drag(0, -90, 0.2, button='left')


def go_down_far():
    pyautogui.moveTo(settings.game_x + 630, settings.game_y + 365)
    time.sleep(0.1)
    pyautogui.drag(0, -300, 0.2, button='left')


def go_left():
    pyautogui.moveTo(settings.game_x + 630, settings.game_y + 365)
    time.sleep(0.2)
    pyautogui.drag(100, 0, 0.2, button='left')


def go_right():
    pyautogui.moveTo(settings.game_x + 630, settings.game_y + 365)
    time.sleep(0.2)
    pyautogui.drag(-100, 0, 0.2, button='left')


def click(x, y):
    pyautogui.click(settings.game_x + x, settings.game_y + y)


def click_next():
    pyautogui.click(settings.game_x + 1163, settings.game_y + 585)
    time.sleep(1)
    click(1142, 490)


def click_image(img, msg, func):
    img_ready = pyautogui.locateOnScreen(img, confidence=0.95)
    if img_ready is not None:
        log(msg)
        click_on_box(img_ready)
        time.sleep(3)
        func()


def click_on_box(box):
    center_points = pyautogui.center(box)
    pyautogui.click(center_points)
    time.sleep(0.5)


def current_time():  # Makes sure the log frame isn't flooded and returns current time.
    log_count = int(settings.app.builder.get_object('text_logframe').index('end-1c').split('.')[0])
    if log_count > 18:
        settings.app.builder.get_object('text_logframe').delete("end-1c linestart", "end")
    return datetime.datetime.now().strftime("%H:%M:%S")


def log(msg):
    log_message = current_time() + " " + msg + "\n"
    print(log_message)
    log_file_name = "log-" + datetime.datetime.now().strftime("%d-%m-%Y") + ".txt"
    log_file = open(log_file_name, 'a+')
    log_file.write(log_message)
    settings.app.builder.get_object('text_logframe').insert('1.0', log_message)


def get_value_from_rect(x1, y1, x2, y2):
    image = getRectAsImage((int(x1), int(y1), int(x2), int(y2)))
    image.save('screencapture_256_256.png', format='png')
    config = '-l digits1+digits+digits_comma --psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    value = pytesseract.pytesseract.image_to_string(image, config=config)
    value = value.strip('.')
    value = value.strip(' ')
    value = value.strip('/')
    return value


# Use top bar to locate game start
def locate_game_window():
    memu_play = 'memu_play.PNG'
    img_box = pyautogui.locateOnScreen(memu_play, confidence=0.95)  # locate top left corner
    if img_box is not None:
        x, y = pyautogui.center(img_box)
        settings.game_x_start = x - 47  # Game distance from Memu Icon
        settings.game_y_start = y + 13
        log("Game window found at " + str(settings.game_x_start) + ", " + str(settings.game_y_start))
        log("Selecting game window")
        click_on_box(img_box)
        return settings.game_x_start, settings.game_y_start
    log("Game window not found")
    return 0, 0


def escape(amount):
    for x in range(0, amount):
        pyautogui.click(settings.game_x + 1449 - 200, settings.game_y + 150 - 118)
        time.sleep(0.4)


drag_count = 0


def look_for_button(img, msg, func):
    global drag_count
    for x in range(0, 13):  # previously 18
        time.sleep(2)

        if msg == "Friend Heart":
            friend_box = pyautogui.locateOnScreen('imgs/friend_box.PNG', confidence=0.88)
            if friend_box is not None:
                click_on_box(friend_box)
                time.sleep(1)
                click(660, 650)
                time.sleep(4)
                facebook_send = pyautogui.locateOnScreen('imgs/facebook_send.PNG', confidence=0.88)
                if facebook_send is not None:
                    click_on_box(facebook_send)
                    time.sleep(1)
                    escape(1)
                break
            no_heart = pyautogui.locateOnScreen('imgs/no_heart.png', confidence=0.88)
            if no_heart is not None:
                log("Ad available!")
                click_on_box(no_heart)
                time.sleep(1)
                click(807 - 18, 615 - 33)
                time.sleep(3)
                accept = pyautogui.locateOnScreen('imgs/unity_accept.png', confidence=0.9)
                if accept is not None:
                    click_on_box(accept)
                # log("Giving ad 45 seconds to finish")
                log("Waiting for ad to finish")
                wait_on_ad(0.75, 200)
                wait_on_img('imgs/ad_close.png', 0.75, 80)
                ad_close = pyautogui.locateOnScreen('imgs/ad_close.png', confidence=0.75)
                if ad_close is not None:
                    click_on_box(ad_close)
                    log("Ad closed")
                    wait_on_img('imgs/herosbutton.png', 0.9, 60)
                    escape(1)
                    return
                else:
                    log("Trying to escape ad")
                    escape(1)
                    time.sleep(1)
                    escape(1)
                    time.sleep(1)
                    return
                # break

        chest = pyautogui.locateOnScreen(img, confidence=0.88)
        if chest is not None:
            log(msg + " button found, clicking")
            click_on_box(chest)
            time.sleep(2)
            func()
            break
        log("Looking for " + msg + " button")
        if drag_count < 5:
            go_right()
        else:
            go_left()
        drag_count += 1
        # log(str(drag_count))
        if drag_count > 9:
            drag_count = 0
        # check_chests()
        # time.sleep(0.5)
    escape(2)


def speed_up_battle():
    times_four = pyautogui.locateOnScreen('imgs/times_four.png', confidence=0.95)
    if times_four is not None:
        return
    time.sleep(1)
    times_one = pyautogui.locateOnScreen('imgs/times_one.png', confidence=0.95)
    if times_one is not None:
        log("Speeding up battle")
        click_on_box(times_one)
    time.sleep(1)
    times_two = pyautogui.locateOnScreen('imgs/times_two.png', confidence=0.95)
    if times_two is not None:
        log("Speeding up battle")
        click_on_box(times_one)
