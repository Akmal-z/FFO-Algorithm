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
    fireflies = np.random.randint(
        0,
        PERIODS_PER_DAY - SHIFT_LENGTH,
        size=(population_size, NUM_DEPARTMENTS)
    )

    brightness = np.array([
        evaluate_firefly(
            firefly[[d-1 for d in selected_departments]],
            demand_vector
        )
        for firefly in fireflies
    ])

    cost_history = []

    for _ in range(iterations):
        for i in range(population_size):
            for j in range(population_size):
                if brightness[j] < brightness[i]:
                    for dept in selected_departments:
                        idx = dept - 1
                        fireflies[i][idx] += (
                            beta * (fireflies[j][idx] - fireflies[i][idx])
                            + alpha * np.random.randn()
                        )

                    fireflies[i] = np.clip(
                        fireflies[i],
                        0,
                        PERIODS_PER_DAY - SHIFT_LENGTH
                    )

                    brightness[i] = evaluate_firefly(
                        fireflies[i][[d-1 for d in selected_departments]],
                        demand_vector
                    )

        cost_history.append(brightness.min())

    best_index = brightness.argmin()
    return fireflies[best_index].astype(int), cost_history
