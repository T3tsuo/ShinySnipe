import pydirectinput
import time
from PIL import Image
import requests
import pyautogui
from random import random

import random_breaks


lowest_price = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/ShinySnipe/main/location/lowest_price.png", stream=True).raw)

advanced_search = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/ShinySnipe/main/location/advanced_search.png", stream=True).raw)


def load_terminal():
    pydirectinput.press("p")
    time.sleep(random_breaks.input_break())
    print("Entered GTL")
    while True:
        if pyautogui.locateOnScreen(lowest_price, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(lowest_price, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)

            pydirectinput.click()
            time.sleep(random_breaks.input_break())
            print("Filter Lowest Price")
            break
    while True:
        if pyautogui.locateOnScreen(advanced_search, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(advanced_search, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)

            pydirectinput.click()
            time.sleep(random_breaks.input_break())
            print("Advanced Search")
            break


def price_filter(price):
    for i in range(5):
        pydirectinput.press("tab")
        time.sleep(random_breaks.input_break())

    for i in range(len(price)):
        pydirectinput.press(price[i])
        time.sleep(random_breaks.input_break())

def shiny_filter():
    for i in range(2):
        pydirectinput.press("tab")
        time.sleep(random_breaks.input_break())
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
