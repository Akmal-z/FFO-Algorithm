# fitness.py

import numpy as np
from config import PERIODS_PER_DAY, SHIFT_LENGTH

def evaluate_firefly(solution, demand):
    """
    solution: array of start periods for departments
    demand: demand value from dataset
    """

    penalty = 0

    # Constraint: shift must fit in a day
    for start in solution:
        if start < 0 or start + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 100

    # Cost function (based on dataset demand)
    cost = demand + penalty

    return cost
