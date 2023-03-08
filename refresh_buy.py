import pydirectinput
import time
from PIL import Image
import requests
import pyautogui
from random import random

import random_breaks


buy_icon = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/ShinySnipe/main/location/buy.png", stream=True).raw)

near_buy = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/ShinySnipe/main/location/near_buy.png", stream=True).raw)

no_entries = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/ShinySnipe/main/location/no_entries.png", stream=True).raw)

refresh_icon = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/ShinySnipe/main/location/refresh.png", stream=True).raw)

def go_to_refresh():
    while True:
        if pyautogui.locateOnScreen(refresh_icon, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(refresh_icon, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)

            pydirectinput.click()
            time.sleep(random_breaks.input_break())
            print("Refresh")
            break

def refresh():
    if pyautogui.locateOnScreen(no_entries, confidence=0.8) is not None:
        pydirectinput.press("space")
        time.sleep(random_breaks.input_break())
        print("Refresh")


def check_entries():
    if pyautogui.locateOnScreen(no_entries, confidence=0.8) is not None:
        return False
    else:
        return True


def buy():
    while True:
        if pyautogui.locateOnScreen(near_buy, confidence=0.8) is not None:
            location_near = pyautogui.locateOnScreen(near_buy, confidence=0.8)
            while True:
                if pyautogui.locateOnScreen(buy_icon, region=location_near, confidence=0.8):
                    location = pyautogui.locateOnScreen(buy_icon, region=location_near, confidence=0.8)
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)

                    pydirectinput.click()
                    time.sleep(random_breaks.input_break())
                    pydirectinput.press("enter")
                    time.sleep(random_breaks.input_break())
                    print("Buy")
                    return


def run(end_time):
    # while there are no entries, and we have not exceeded 10 minutes
    if not check_entries():
        go_to_refresh()
    while not check_entries() and end_time > time.time():
        refresh()
    if check_entries():
        buy()
    pydirectinput.press("p")
    time.sleep(random_breaks.input_break())

