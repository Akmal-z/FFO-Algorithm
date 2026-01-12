# fitness.py

from config import PERIODS_PER_DAY, SHIFT_LENGTH

def evaluate_firefly(solution, demand):
    """
    solution: list of start periods for each department
    demand: value derived from dataset
    """

    penalty = 0

    for start in solution:
        # Must fit within a day
        if start < 0 or start + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 100

    # Cost = demand + penalties
    cost = demand + penalty
    return cost
