# ffo.py

import numpy as np
from fitness import evaluate_firefly
from config import PERIODS_PER_DAY, SHIFT_LENGTH, NUM_DEPARTMENTS

def firefly_optimization(
    demand_vector,
    selected_departments,
    population_size,
    iterations,
    alpha,
    beta
):
    # Initialize fireflies
    fireflies = np.random.randint(
        0,
        PERIODS_PER_DAY - SHIFT_LENGTH,
        size=(population_size, NUM_DEPARTMENTS)
    )

    history = []

    for _ in range(iterations):
        fitness_list = []

        for f in fireflies:
            metrics = evaluate_firefly(
                f[[d - 1 for d in selected_departments]],
                demand_vector
            )
            fitness_list.append(metrics)

        # Move fireflies (FFO rule)
        for i in range(population_size):
            for j in range(population_size):
                if fitness_list[j]["global"] < fitness_list[i]["global"]:
                    for d in selected_departments:
                        idx = d - 1
                        fireflies[i][idx] += (
                            beta * (fireflies[j][idx] - fireflies[i][idx])
                            + alpha * np.random.randn()
                        )

                    fireflies[i] = np.clip(
                        fireflies[i],
                        0,
                        PERIODS_PER_DAY - SHIFT_LENGTH
                    )

        history.append(min(f["global"] for f in fitness_list))

    # =========================
    # MULTI-OBJECTIVE SELECTION
    # =========================
    balance_scores = [
        abs(f["shortage"] - f["workload"])
        for f in fitness_list
    ]

    best_index = int(np.argmin(balance_scores))
    best_solution = fireflies[best_index]

    return best_solution.astype(int), history, fitness_list[best_index]
