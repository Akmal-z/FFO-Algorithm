# fitness.py

import numpy as np
from config import SHIFT_LENGTH, MIN_STAFF

W_SHORTAGE = 20
W_WORKLOAD = 5
W_MIN_STAFF = 30

def evaluate_firefly(solution, demand_vector):
    """
    solution        : number of staff assigned per department
    demand_vector   : demand per department (from original dataset)
    """

    # ======================
    # Assigned staff
    # ======================
    assigned_staff = solution.astype(int)

    # ======================
    # HARD 1: Shortage
    # ======================
    shortage = np.maximum(0, demand_vector - assigned_staff)
    shortage_penalty = np.sum(shortage) * W_SHORTAGE

    # ======================
    # HARD 2: Workload balance
    # ======================
    workload = assigned_staff * SHIFT_LENGTH
    avg_workload = np.mean(workload)

    workload_penalty = np.sum(
        np.abs(workload - avg_workload)
    ) * W_WORKLOAD

    # ======================
    # SOFT: Minimum staff
    # ======================
    total_staff = np.sum(assigned_staff)
    min_staff_penalty = 0

    if total_staff < MIN_STAFF:
        min_staff_penalty = (MIN_STAFF - total_staff) * W_MIN_STAFF

    # ======================
    # Fitness
    # ======================
    global_fitness = (
        shortage_penalty +
        workload_penalty +
        min_staff_penalty
    )

    return {
        "global": global_fitness,
        "shortage": shortage_penalty,
        "workload": workload_penalty,
        "min_staff": min_staff_penalty
    }
