# data_loader.py

import pandas as pd
import os

def load_dataset():
    """
    Load dataset from repository.
    If not found (Streamlit Cloud case),
    generate a structured fallback dataset.
    """

    path = "dataset/Store_Size_6.xlsx"

    if os.path.exists(path):
        df = pd.read_excel(path)
        status = "Dataset loaded from repository"
    else:
        # Fallback dataset (STRUCTURE-BASED, NOT RANDOM)
        df = pd.DataFrame({
            "Department": [1, 2, 3, 4, 5, 6],
            "Demand": [34, 36, 30, 32, 38, 38]
        })
        status = "Fallback dataset (structure-based)"

    return df, status
