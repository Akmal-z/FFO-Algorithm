# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization
from config import SHIFT_LENGTH, DAYS_OF_WEEK

st.set_page_config(page_title="FFO Algorithm Scheduling", layout="wide")

st.title("Firefly Optimization (FFO) – Employee Shift Scheduling")
st.write("Department-based scheduling using Firefly Optimization")

# =========================
# Load dataset (NO upload)
# =========================
departments, df = load_dataset()

# =========================
# LEFT SIDEBAR: Department Selector
# =========================
st.sidebar.header("Department Selection")

selected_departments = st.sidebar.multiselect(
    "Select Department Numbers",
    options=departments,
    default=departments
)

# =========================
# LEFT SIDEBAR: FFO Parameters
# =========================
st.sidebar.header("FFO Parameters")

population_size = st.sidebar.slider(
    "Population Size", 10, 50, 20
)

iterations = st.sidebar.slider(
    "Iterations", 10, 100, 50
)

# =========================
# MAIN PAGE: Time Selection (X / Y axis)
# =========================
st.subheader("Time Selection")

col1, col2 = st.columns(2)

with col1:
    day_of_month = st.selectbox(
        "Day of Month (X-axis)",
        list(range(1, 29))
    )

with col2:
    day_of_week = st.selectbox(
        "Day of Week (Y-axis)",
        DAYS_OF_WEEK
    )

# =========================
# Run Optimization
# =========================
if selected_departments and st.button("Run Firefly Optimization"):
    best_firefly, fitness = firefly_optimization(
        selected_departments,
        population_size,
        iterations
    )

    st.subheader(
        f"Optimized Schedule (Day {day_of_month}, {day_of_week})"
    )

    result = []
    for dept in selected_departments:
        start = best_firefly[dept - 1]
        end = start + SHIFT_LENGTH

        result.append({
            "Department": dept,
            "Start Period": start + 1,
            "End Period": end,
            "Working Duration": "8 hours"
        })

    result_df = pd.DataFrame(result)
    st.dataframe(result_df)

    st.success(f"Best Fitness Score: {fitness}")

# =========================
# Dataset Preview (Optional)
# =========================
with st.expander("View Dataset Preview"):
    st.dataframe(df.hea
