# data_loader.py

import pandas as pd
import os

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found at {path}. "
            "Make sure the dataset folder and file exist in the repository."
        )

    df = pd.read_excel(path)

    # Fixed department numbers as requested
    departments = [1, 2, 3, 4, 5, 6]

    return departments, df
