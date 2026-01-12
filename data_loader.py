# data_loader.py

import pandas as pd
import os

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    if not os.path.exists(path):
        raise FileNotFoundError(
            "Dataset not found. Please ensure "
            "'dataset/Store_Size_6.xlsx' exists in the repository."
        )

    df = pd.read_excel(path)

    # Fixed department numbers (1–6)
    departments = [1, 2, 3, 4, 5, 6]

    return departments, df
