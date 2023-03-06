import pydirectinput
import time

import random_breaks

def load_terminal():
    pydirectinput.press("z")
    time.sleep(random_breaks.dialogue_break())
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("z")
