import random

# Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
# Developed by Your Mother
# You see, young child. I add weights to randomness based on what you choose
# If you defect, I'll have a higher chance of doing the same.
# If you cooperate, I'll consider cooperating.
# You see, I'm a double edged sword.
# I will never be coerced into doing something. I'm always a bit random.

def strategy(history, memory):
    if memory is None:
        memory = 0.5
    if history.shape[1] == 0:
        return 1, None
    else:
        if history[1, -1] == 0:
            memory = max(0.0, memory - 0.1)
            return random.random() < memory, memory
            
        else:
            memory = min(1.0, memory + 0.1)
            return random.random() < memory, memory
        
# psst if you're reading this hi cary <3