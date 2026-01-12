# ffo.py

import numpy as np
from fitness import evaluate_firefly
from config import NUM_DEPARTMENTS

def firefly_optimization(
    demand_vector,
    selected_departments,
    population_size,
    iterations,
    alpha,
    beta
):
    # Firefly = staff assigned per department
    fireflies = np.random.randint(
        low=0,
        high=10,
        size=(population_size, NUM_DEPARTMENTS)
    )

    history = []
    metrics_list = []

    for _ in range(iterations):
        metrics_list = []

        for f in fireflies:
            metrics = evaluate_firefly(
                f[[d - 1 for d in selected_departments]],
                demand_vector
            )
            metrics_list.append(metrics)

        # Move fireflies
        for i in range(population_size):
            for j in range(population_size):
                if metrics_list[j]["global"] < metrics_list[i]["global"]:
                    for d in selected_departments:
                        idx = d - 1
                        fireflies[i][idx] += (
                            beta * (fireflies[j][idx] - fireflies[i][idx]) +
                            alpha * np.random.randn()
                        )

        history.append(
            min(m["global"] for m in metrics_list)
        )

    # ======================
    # MULTI-OBJECTIVE BALANCE
    # ======================
    balance_scores = [
        abs(m["deviation"] - m["workload"])
        for m in metrics_list
    ]

    best_idx = int(np.argmin(balance_scores))
    return fireflies[best_idx].astype(int), history, metrics_list[best_idx]
