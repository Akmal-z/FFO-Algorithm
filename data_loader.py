# data_loader.py

import pandas as pd
import os

def load_dataset(uploaded_file=None):
    """
    Priority:
    1. Use uploaded file (Streamlit Cloud safe)
    2. Use dataset from repo if exists
    """

    # Option 1: Uploaded file
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        departments = [1, 2, 3, 4, 5, 6]
        return departments, df

    # Option 2: Dataset inside repo
    path = "dataset/Store_Size_6.xlsx"

    if os.path.exists(path):
        df = pd.read_excel(path)
        departments = [1, 2, 3, 4, 5, 6]
        return departments, df

    # If BOTH fail → clear error
    raise FileNotFoundError(
        "Dataset not found. Please upload the Excel file "
        "or ensure dataset/Store_Size_6.xlsx exists in the repository."
    )
