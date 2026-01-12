# fitness.py

from config import PERIODS_PER_DAY, SHIFT_LENGTH

def evaluate_firefly(solution, demand):
    penalty = 0

    for start in solution:
        if start < 0 or start + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 100

    return demand + penalty   # lower = brighter
