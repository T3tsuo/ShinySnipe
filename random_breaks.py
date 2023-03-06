from random import random


def dialogue_break():
    # timer between 0.5 seconds to 1 seconds
    return random() * 0.5 + 0.5


def input_break():
    # 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1
