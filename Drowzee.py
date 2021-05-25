import numpy as np
import random

# Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
# Developed by Your Mother
# You see, young child. I add weights to randomness based on what you choose
# If you defect, I'll have a higher chance of doing the same.
# If you cooperate, I'll consider cooperating.
# You see, I'm a double edged sword.
# I will never be coerced into doing something. I'm always a bit random.

def strategy(history, memory):
    if history.shape[1] == 0:
        return random.randint(0, 1), None
    return random.random() < sum(history[1]) / len(history[1]), None