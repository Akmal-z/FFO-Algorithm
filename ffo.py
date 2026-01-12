# ffo.py

import numpy as np
from fitness import evaluate_firefly
from config import PERIODS_PER_DAY, SHIFT_LENGTH, NUM_DEPARTMENTS

def firefly_optimization(demand, population_size, iterations, alpha, beta):
    fireflies = np.random.randint(
        0,
        PERIODS_PER_DAY - SHIFT_LENGTH,
        size=(population_size, NUM_DEPARTMENTS)
    )

    brightness = np.array([
        evaluate_firefly(f, demand) for f in fireflies
    ])

    cost_history = []

    for _ in range(iterations):
        for i in range(population_size):
            for j in range(population_size):
                if brightness[j] < brightness[i]:
                    fireflies[i] = (
                        fireflies[i]
                        + beta * (fireflies[j] - fireflies[i])
                        + alpha * np.random.randn(NUM_DEPARTMENTS)
                    )

                    fireflies[i] = np.clip(
                        fireflies[i],
                        0,
                        PERIODS_PER_DAY - SHIFT_LENGTH
                    )

                    brightness[i] = evaluate_firefly(
                        fireflies[i], demand
                    )

        cost_history.append(brightness.min())

    best_index = brightness.argmin()
    return fireflies[best_index].astype(int), cost_history
