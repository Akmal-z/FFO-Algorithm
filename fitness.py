# fitness.py

from config import PERIODS_PER_DAY, SHIFT_LENGTH

def evaluate_firefly(firefly, selected_departments):
    penalty = 0

    for dept in selected_departments:
        start = firefly[dept - 1]

        # Shift must fit within 28 periods
        if start < 0 or start + SHIFT_LENGTH > PERIODS_PER_DAY:
            penalty += 50

    return -penalty   # Brightness
