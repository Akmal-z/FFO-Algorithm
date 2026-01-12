# fitness.py

import numpy as np
from config import SHIFT_LENGTH

def evaluate_firefly(solution, demand_vector):
    """
    solution: start periods per department
    demand_vector: demand for departments (original matrix)
    """

    # ======================
    # HARD CONSTRAINT 1: Shortage
    # ======================
    staff_assigned = np.ones(len(solution)) * SHIFT_LENGTH
    shortage = np.maximum(0, demand_vector - staff_assigned)
    shortage_penalty = np.sum(shortage) * 10

    # ======================
    # HARD CONSTRAINT 2: Workload balance
    # ======================
    workload = staff_assigned
    avg_workload = np.mean(workload)
    workload_penalty = np.sum(np.abs(workload - avg_workload)) * 5

    # ======================
    # GLOBAL FITNESS
    # ======================
    global_fitness = shortage_penalty + workload_penalty

    return {
        "global": global_fitness,
        "shortage": shortage_penalty,
        "workload": workload_penalty
    }
