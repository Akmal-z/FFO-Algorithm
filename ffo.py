# ffo.py

import random
from fitness import evaluate_firefly
from config import NUM_DEPARTMENTS, PERIODS_PER_DAY, SHIFT_LENGTH

def generate_firefly():
    return [
        random.randint(0, PERIODS_PER_DAY - SHIFT_LENGTH)
        for _ in range(NUM_DEPARTMENTS)
    ]

def firefly_optimization(population_size=20, iterations=50):
    population = [generate_firefly() for _ in range(population_size)]
    brightness = [evaluate_firefly(f) for f in population]

    for _ in range(iterations):
        for i in range(population_size):
            for j in range(population_size):
                if brightness[j] > brightness[i]:
                    # Move firefly i towards firefly j
                    for d in range(NUM_DEPARTMENTS):
                        if random.random() < 0.3:
                            population[i][d] = population[j][d]

                    brightness[i] = evaluate_firefly(population[i])

    best_index = brightness.index(max(brightness))
    return population[best_index], brightness[best_index]
