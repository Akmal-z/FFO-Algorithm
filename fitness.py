# fitness.py

from config import PERIODS_PER_DAY, SHIFT_LENGTH, NUM_DEPARTMENTS

def evaluate_firefly(firefly):
    penalty = 0

    for dept in range(NUM_DEPARTMENTS):
        start_period = firefly[dept]

        # Constraint: shift must fit inside the day
        if start_period < 0 or start_period + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 50

        # Constraint: continuous 16 periods
        # (Automatically satisfied by encoding)

    # Higher fitness = better solution
    fitness = -penalty
    return fitness
