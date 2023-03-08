import pydirectinput
import time

import random_breaks


def one_block():
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.1
    print("Moved")