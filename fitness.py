# fitness.py

from config import PERIODS_PER_DAY, SHIFT_LENGTH

def evaluate_firefly(solution, demand_vector):
    """
    solution: start periods per department
    demand_vector: demand for selected departments on selected day
    """

    penalty = 0

    for start, demand in zip(solution, demand_vector):
        # Shift boundary constraint
        if start < 0 or start + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 100

        # Demand constraint
        if demand > 0 and start is None:
            penalty += demand * 10

    return penalty
