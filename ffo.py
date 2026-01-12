# ffo.py

import numpy as np
from fitness import evaluate_firefly
from config import PERIODS_PER_DAY, SHIFT_LENGTH, NUM_DEPARTMENTS

def firefly_optimization(
    demand,
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

    brightness = np.array([
        evaluate_firefly(f, demand) for f in fireflies
    ])

    best_cost_history = []

    for t in range(iterations):
        for i in range(population_size):
            for j in range(population_size):
                if brightness[j] < brightness[i]:
                    # Move firefly i toward j
                    fireflies[i] = fireflies[i] + \
                        beta * (fireflies[j] - fireflies[i]) + \
                        alpha * np.random.randn(NUM_DEPARTMENTS)

                    fireflies[i] = np.clip(
                        fireflies[i],
                        0,
                        PERIODS_PER_DAY - SHIFT_LENGTH
                    )

                    brightness[i] = evaluate_firefly(
                        fireflies[i], demand
                    )

        best_cost_history.append(np.min(brightness))

    best_index = np.argmin(brightness)
    best_solution = fireflies[best_index]

    return best_solution.astype(int), best_cost_history
