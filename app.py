# app.py

import streamlit as st
import pandas as pd
from ffo import firefly_optimization
from config import NUM_DEPARTMENTS, SHIFT_LENGTH

st.set_page_config(page_title="FFO Algorithm - Shift Scheduling")

st.title("Employee Shift Scheduling using Firefly Optimization (FFO)")
st.write("Simplified Period-Based Scheduling Model")

st.sidebar.header("FFO Parameters")

population_size = st.sidebar.slider("Population Size", 10, 50, 20)
iterations = st.sidebar.slider("Iterations", 10, 100, 50)

if st.button("Run Firefly Optimization"):
    best_firefly, fitness = firefly_optimization(population_size, iterations)

    st.subheader("Optimized Shift Schedule (Per Department)")

    schedule_data = []
    for dept in range(NUM_DEPARTMENTS):
        start = best_firefly[dept]
        end = start + SHIFT_LENGTH

        schedule_data.append({
            "Department": f"Department {dept + 1}",
            "Start Period": start + 1,
            "End Period": end,
            "Working Hours": "8 hours"
        })

    df = pd.DataFrame(schedule_data)
    st.dataframe(df)

    st.success(f"Best Fitness Score: {fitness}")
