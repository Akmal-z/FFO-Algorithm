# data_loader.py

import pandas as pd
import os

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    if not os.path.exists(path):
        raise FileNotFoundError(
            "Dataset not found. Please ensure dataset/Store_Size_6.xlsx exists."
        )

    # Read raw Excel (no header)
    raw_df = pd.read_excel(path, header=None)

    # Day of month (columns 1–28)
    days = raw_df.iloc[1, 1:29].astype(int)

    # Demand matrix: rows = departments, cols = days
    demand_matrix = raw_df.iloc[2:8, 1:29].copy()
    demand_matrix.index = [1, 2, 3, 4, 5, 6]
    demand_matrix.columns = days

    return demand_matrix
