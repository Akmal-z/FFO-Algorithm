# data_loader.py

import pandas as pd
import os

def load_dataset():
    path = "dataset/Store_Size_6.xlsx"

    if not os.path.exists(path):
        raise FileNotFoundError(
            "Dataset not found. Ensure dataset/Store_Size_6.xlsx exists."
        )

    df = pd.read_excel(path)

    return df
