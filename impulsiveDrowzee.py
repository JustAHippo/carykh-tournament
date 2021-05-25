import numpy as np
import random

# Developed by Your Mother
# You see, young child. I add weights based on what you choose
# Depending on what you choose, I'll decide exactly what move to make

def strategy(history, memory):
    if history.shape[1] == 0:
        return 1, None
    else:
        chance = sum(history[1]) / len(history[1])
        if chance > 0.5:
            return 1, None
        if chance < 0.5:
            return 0, None
        if chance == 0.5:
           return random.randint(0, 1), None
        
# psst if you're reading this hi cary <3