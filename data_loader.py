# data_loader.py

import pandas as pd
import os

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    if os.path.exists(path):
        df = pd.read_excel(path)
        status = "Dataset loaded from repository"
    else:
        # Structured fallback (dataset-style)
        df = pd.DataFrame({
            "Department": [1, 2, 3, 4, 5, 6],
            "Demand": [34, 36, 30, 32, 38, 38]
        })
        status = "Fallback dataset (structure-based)"

    return df, status
