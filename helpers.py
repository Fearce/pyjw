import datetime
import pyautogui
import time
import pytesseract
import settings
from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def go_left():
    pyautogui.moveTo(settings.game_x+630, settings.game_y+365)
    time.sleep(0.2)
    pyautogui.drag(100, 0, 0.2, button='left')

def go_right():
    pyautogui.moveTo(settings.game_x+630, settings.game_y+365)
    time.sleep(0.2)
    pyautogui.drag(-100, 0, 0.2, button='left')


def click(x, y):
    pyautogui.click(settings.game_x+x, settings.game_y+y)


def click_next():
    pyautogui.click(settings.game_x+1163, settings.game_y+585)
    time.sleep(1)


def click_image(img, msg, func):
    img_ready = pyautogui.locateOnScreen(img, confidence=0.95)
    if img_ready is not None:
        log(msg)
        click_on_box(img_ready)
        time.sleep(3)
        pyautogui.click(settings.game_x + 1095 - 33, settings.game_y + 487 - 49)
        time.sleep(1)
        func()

def click_on_box(box):
    center_points = pyautogui.center(box)
    pyautogui.click(center_points)
    time.sleep(0.5)


def log(msg):
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + ": " + msg)


def get_value_from_rect(x1, y1, x2, y2):
    image = getRectAsImage((int(x1), int(y1), int(x2), int(y2)))
    image.save('screencapture_256_256.png', format='png')
    config = '-l digits1+digits+digits_comma --psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    value = pytesseract.pytesseract.image_to_string(image, config=config)
    return value


# Use top bar to locate game start
def locate_game_window():
    memu_play = 'memu_play.PNG'
    img_box = pyautogui.locateOnScreen(memu_play, confidence=0.95)  # locate top left corner
    if img_box is not None:
        x, y = pyautogui.center(img_box)
        settings.game_x_start = x - 47
        settings.game_y_start = y + 13
        log("Game window found at " + str(settings.game_x_start) + ", " + str(settings.game_y_start))
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
    for x in range(0, 20):  # Look for chest 20 times or give up
        time.sleep(2)
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
    log("Can't find chest, something is wrong, escaping")
    escape(2)
