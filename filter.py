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
    pydirectinput.press("z")
    time.sleep(random_breaks.dialogue_break())
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("z")
    time.sleep(random_breaks.input_break())
    while True:
        if pyautogui.locateOnScreen(lowest_price, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(lowest_price, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)

            pydirectinput.click()
            time.sleep(random_breaks.input_break())
            break
    while True:
        if pyautogui.locateOnScreen(advanced_search, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(advanced_search, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)

            pydirectinput.click()
            time.sleep(random_breaks.input_break())
            break

