# fitness.py

import numpy as np
from config import SHIFT_LENGTH, MIN_STAFF

W_DEVIATION = 20     # main hard constraint
W_WORKLOAD  = 3
W_MINSTAFF  = 30

def evaluate_firefly(solution, demand_vector):
    """
    solution: staff assigned per department
    demand_vector: demand from dataset
    """

    assigned = solution.astype(int)

    # =========================
    # HARD: Deviation from demand
    # (covers shortage + overstaff)
    # =========================
    deviation = np.abs(assigned - demand_vector)
    deviation_penalty = np.sum(deviation) * W_DEVIATION

    # =========================
    # HARD: Workload balance
    # =========================
    workload = assigned * SHIFT_LENGTH
    avg_workload = np.mean(workload)
    workload_penalty = np.sum(
        np.abs(workload - avg_workload)
    ) * W_WORKLOAD

    # =========================
    # SOFT: Minimum staff
    # =========================
    total_staff = np.sum(assigned)
    min_staff_penalty = 0
    if total_staff < MIN_STAFF:
        min_staff_penalty = (MIN_STAFF - total_staff) * W_MINSTAFF

    global_fitness = (
        deviation_penalty +
        workload_penalty +
        min_staff_penalty
    )

    return {
        "global": global_fitness,
        "deviation": deviation_penalty,
        "workload": workload_penalty,
        "min_staff": min_staff_penalty
    }
