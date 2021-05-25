import random

# Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
# Developed by Your Mother
# You see, young child. I add weights based on what you choose
# Depending on what you choose, I'll decide exactly what move to make


def strategy(history, memory):
    if memory is None:
        memory = 0.5
    if history.shape[1] == 0:
        return 1, None
    else:
        if history[1, -1] == 0:
            memory = max(0.0, memory - 0.1)
            if memory < 0.5:
                return 0, memory
            if memory > 0.5:
                return 1, memory
            if memory == 0.5:
                return random.randint(0, 1), memory
            
        else:
            memory = min(1.0, memory + 0.1)
            if memory < 0.5:
                return 0, memory
            if memory > 0.5:
                return 1, memory
            if memory == 0.5:
                return random.randint(0, 1), memory
        
# psst if you're reading this hi cary <3