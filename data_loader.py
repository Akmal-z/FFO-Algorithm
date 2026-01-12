# data_loader.py

import pandas as pd

def load_dataset():
    # Dataset stored inside GitHub repo
    path = "dataset/Store_Size_6.xlsx"
    df = pd.read_excel(path)

    # Fixed department numbers as requested
    departments = [1, 2, 3, 4, 5, 6]

    return departments, df
