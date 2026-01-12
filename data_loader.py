# data_loader.py

import pandas as pd
import os

def load_dataset(uploaded_file=None):
    """
    Priority:
    1. Uploaded file (Streamlit Cloud safe)
    2. Dataset inside repository
    """

    # Option 1: User uploads file
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        departments = [1, 2, 3, 4, 5, 6]
        return departments, df

    # Option 2: Dataset in repo
    repo_path = "dataset/Store_Size_6.xlsx"

    if os.path.exists(repo_path):
        df = pd.read_excel(repo_path)
        departments = [1, 2, 3, 4, 5, 6]
        return departments, df

    # Fail-safe (never silent crash)
    raise FileNotFoundError(
        "Dataset not found. Upload the Excel file "
        "or place it inside dataset/Store_Size_6.xlsx"
    )
