# data_loader.py

import pandas as pd
import os

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    # Case 1: Dataset exists in repo
    if os.path.exists(path):
        df = pd.read_excel(path)
    else:
        # Case 2: Fallback dataset (auto-generated)
        df = pd.DataFrame({
            "Department": [1, 2, 3, 4, 5, 6],
            "Description": [
                "Dept 1", "Dept 2", "Dept 3",
                "Dept 4", "Dept 5", "Dept 6"
            ]
        })

    # Fixed department numbers
    departments = [1, 2, 3, 4, 5, 6]

    return departments, df
