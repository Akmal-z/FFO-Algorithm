# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization
from config import DEPARTMENTS, DAYS_OF_WEEK, SHIFT_LENGTH

st.set_page_config(page_title="FFO Staff Scheduling", layout="wide")

st.title("🔥 Firefly Optimization – Multi-Objective Staff Scheduling")

# =========================
# LOAD ORIGINAL DATA
# =========================
demand_matrix, status = load_dataset()
st.info(f"Dataset status: {status}")
st.dataframe(demand_matrix)

# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.header("Scheduling Settings")

selected_departments = st.sidebar.multiselect(
    "Select Departments",
    options=DEPARTMENTS,
    default=DEPARTMENTS
)

day_of_month = st.sidebar.selectbox(
    "Day of Month (X-axis)",
    list(demand_matrix.columns)
)

day_of_week = st.sidebar.selectbox(
    "Day of Week (Y-axis)",
    DAYS_OF_WEEK
)

st.sidebar.header("FFO Parameters")
population_size = st.sidebar.slider("Population Size", 5, 30, 15)
iterations = st.sidebar.slider("Iterations", 20, 200, 100)
alpha = st.sidebar.slider("Randomization (α)", 0.0, 1.0, 0.3)
beta = st.sidebar.slider("Attractiveness (β)", 0.1, 1.0, 0.6)

# =========================
# ORIGINAL DEMAND VECTOR
# =========================
demand_vector = demand_matrix.loc[selected_departments, day_of_month].values

# =========================
# RUN FFO
# =========================
if selected_departments and st.button("Run Firefly Optimization"):

    best_solution, history, best_metrics = firefly_optimization(
        demand_vector=demand_vector,
        selected_departments=selected_departments,
        population_size=population_size,
        iterations=iterations,
        alpha=alpha,
        beta=beta
    )

    st.success("Optimization completed (Best Balanced Solution Selected)")

    st.subheader("Penalty Breakdown (Best Balanced)")
    st.write(f"Shortage Penalty: {best_metrics['shortage']}")
    st.write(f"Workload Penalty: {best_metrics['workload']}")
    st.write(f"Global Fitness: {best_metrics['global']}")

    # =========================
    # SCHEDULING TABLE
    # =========================
    table = []
    for d in selected_departments:
        start = best_solution[d - 1]
        end = start + SHIFT_LENGTH

        table.append({
            "Department": d,
            "Start Period": start + 1,
            "End Period": end,
            "Shift Length": SHIFT_LENGTH
        })

    st.subheader("Final Schedule (Best Balanced Fitness)")
    st.dataframe(pd.DataFrame(table))

    # =========================
    # CONVERGENCE GRAPH
    # =========================
    st.subheader("Global Fitness Convergence")
    st.line_chart(
        pd.DataFrame(
            {"Global Fitness": history},
            index=range(1, len(history) + 1)
        )
    )
