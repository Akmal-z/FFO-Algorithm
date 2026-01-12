# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization
from config import DEPARTMENTS, DAYS_OF_WEEK, SHIFT_LENGTH

st.set_page_config(
    page_title="FFO Staff Scheduling Optimizer",
    layout="wide"
)

st.title("🔥 Firefly Optimization (FFO) – Staff Scheduling")
st.write("Dataset-driven optimization using Firefly Algorithm")

# =========================
# LOAD DATASET
# =========================
df, dataset_status = load_dataset()
st.info(f"Dataset status: {dataset_status}")
st.dataframe(df.head())

# =========================
# SIDEBAR – DEPARTMENT SELECTOR (UNCHANGED)
# =========================
st.sidebar.header("Scheduling Settings")

selected_departments = st.sidebar.multiselect(
    "Select Departments",
    options=DEPARTMENTS,
    default=DEPARTMENTS
)

day_of_month = st.sidebar.selectbox(
    "Day of Month (X-axis)",
    list(range(1, 29))
)

day_of_week = st.sidebar.selectbox(
    "Day of Week (Y-axis)",
    DAYS_OF_WEEK
)

# =========================
# SIDEBAR – FFO PARAMETERS
# =========================
st.sidebar.header("FFO Parameters")

population_size = st.sidebar.slider(
    "Number of Fireflies", 5, 30, 15
)

iterations = st.sidebar.slider(
    "Iterations", 20, 200, 100
)

alpha = st.sidebar.slider(
    "Randomization (α)", 0.0, 1.0, 0.3
)

beta = st.sidebar.slider(
    "Attractiveness (β)", 0.1, 1.0, 0.6
)

# =========================
# DEMAND FROM DATASET
# =========================
numeric_cols = df.select_dtypes(include="number")
demand = int(numeric_cols.sum().sum())

# =========================
# RUN FFO
# =========================
if selected_departments and st.button("🚀 Run Firefly Optimization"):

    best_solution, cost_history = firefly_optimization(
        demand=demand,
        population_size=population_size,
        iterations=iterations,
        alpha=alpha,
        beta=beta
    )

    st.success("Optimization completed successfully")

    st.subheader(
        f"Optimized Schedule – Day {day_of_month} ({day_of_week})"
    )

    result = []
    for dept in selected_departments:
        start = best_solution[dept - 1]
        end = start + SHIFT_LENGTH

        result.append({
            "Department": dept,
            "Start Period": start + 1,
            "End Period": end,
            "Working Hours": "8 hours"
        })

    st.dataframe(pd.DataFrame(result))

    st.subheader("Convergence Graph (Cost Reduction)")
    st.line_chart(pd.DataFrame({"Cost": cost_history}))
