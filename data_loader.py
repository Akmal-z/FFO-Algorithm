# data_loader.py

import pandas as pd
import os
import numpy as np

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    if os.path.exists(path):
        # ORIGINAL DATASET
        raw_df = pd.read_excel(path, header=None)

        days = raw_df.iloc[1, 1:29].astype(int)
        demand_matrix = raw_df.iloc[2:8, 1:29].copy()

        demand_matrix.index = [1, 2, 3, 4, 5, 6]
        demand_matrix.columns = days

        status = "Original dataset loaded from repository"
    else:
        # FALLBACK – SAME STRUCTURE (NOT SIMPLIFIED)
        days = list(range(1, 29))
        demand_matrix = pd.DataFrame(
            np.ones((6, 28), dtype=int),
            index=[1, 2, 3, 4, 5, 6],
            columns=days
        )

        status = "Fallback dataset (original structure)"

    return demand_matrix, status
