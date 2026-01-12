# fitness.py

from config import PERIODS_PER_DAY, SHIFT_LENGTH

def evaluate_firefly(solution, demand_vector):
    penalty = 0

    for start, demand in zip(solution, demand_vector):
        if start < 0 or start + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 100

        if demand > 0:
            penalty += demand * 5

    return penalty
