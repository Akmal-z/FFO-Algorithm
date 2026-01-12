# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization
from config import SHIFT_LENGTH, DAYS_OF_WEEK

st.set_page_config(page_title="FFO Algorithm Scheduling")

st.title("Firefly Optimization (FFO) – Employee Shift Scheduling")

st.write("X-axis: Day of Month | Y-axis: Day of Week")

# Load dataset
departments, df = load_dataset()

# 🔹 Department selector on MAIN PAGE
st.subheader("Select Departments")
selected_departments = st.multiselect(
    "Department Numbers",
    options=departments,
    default=departments
)

# Axis selection
st.subheader("Select Day")
day_of_month = st.selectbox("Day of Month (X-axis)", list(range(1, 29)))
day_of_week = st.selectbox("Day of Week (Y-axis)", DAYS_OF_WEEK)

st.sidebar.header("FFO Parameters")
population_size = st.sidebar.slider("Population Size", 10, 50, 20)
iterations = st.sidebar.slider("Iterations", 10, 100, 50)

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
            "Department": f"Department {dept}",
            "Start Period": start + 1,
            "End Period": end,
            "Working Hours": "8 hours"
        })

    result_df = pd.DataFrame(result)
    st.dataframe(result_df)

    st.success(f"Best Fitness Score: {fitness}")
