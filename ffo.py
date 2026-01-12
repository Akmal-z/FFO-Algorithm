# ffo.py

import random
from fitness import evaluate_firefly
from config import PERIODS_PER_DAY, SHIFT_LENGTH, NUM_DEPARTMENTS

BETA = 0.6    # attractiveness
ALPHA = 0.3   # randomization

def generate_firefly():
    return [
        random.randint(0, PERIODS_PER_DAY - SHIFT_LENGTH)
        for _ in range(NUM_DEPARTMENTS)
    ]

def firefly_optimization(selected_departments, population_size=20, iterations=50):
    population = [generate_firefly() for _ in range(population_size)]
    brightness = [evaluate_firefly(f, selected_departments) for f in population]

    for _ in range(iterations):
        for i in range(population_size):
            for j in range(population_size):
                if brightness[j] > brightness[i]:
                    for dept in selected_departments:
                        idx = dept - 1

                        # attraction
                        if random.random() < BETA:
                            population[i][idx] = population[j][idx]

                        # random walk
                        if random.random() < ALPHA:
                            population[i][idx] = random.randint(
                                0, PERIODS_PER_DAY - SHIFT_LENGTH
                            )

                    brightness[i] = evaluate_firefly(
                        population[i], selected_departments
                    )

    best_index = brightness.index(max(brightness))
    return population[best_index], brightness[best_index]
