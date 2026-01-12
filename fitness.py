# fitness.py

import numpy as np
from config import SHIFT_LENGTH, MIN_STAFF

def evaluate_firefly(solution, demand_vector):
    """
    solution        : start period for each selected department
    demand_vector   : original demand from dataset
    """

    # =========================
    # HARD CONSTRAINT 1: Shortage
    # =========================
    staff_assigned = np.ones(len(solution)) * SHIFT_LENGTH
    shortage = np.maximum(0, demand_vector - staff_assigned)
    shortage_penalty = np.sum(shortage) * 10

    # =========================
    # HARD CONSTRAINT 2: Workload balance
    # =========================
    avg_workload = np.mean(staff_assigned)
    workload_penalty = np.sum(
        np.abs(staff_assigned - avg_workload)
    ) * 5

    # =========================
    # SOFT CONSTRAINT: Min staff
    # =========================
    if len(solution) < MIN_STAFF:
        workload_penalty += (MIN_STAFF - len(solution)) * 20

    # =========================
    # GLOBAL FITNESS
    # =========================
    global_fitness = shortage_penalty + workload_penalty

    return {
        "global": global_fitness,
        "shortage": shortage_penalty,
        "workload": workload_penalty
    }
