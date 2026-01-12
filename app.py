# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization
from config import DEPARTMENTS, DAYS_OF_WEEK, SHIFT_LENGTH

st.set_page_config(page_title="FFO Staff Scheduling", layout="wide")

st.title("Firefly Optimization – Multi-Objective Staff Scheduling")

# =========================
# LOAD DATASET
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
# DEMAND VECTOR
# =========================
demand_vector = demand_matrix.loc[
    selected_departments, day_of_month
].values

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

    st.success("Optimization completed – Best BALANCED solution selected")

    # =========================
    # PENALTY SUMMARY
    # =========================
    st.subheader("Penalty Breakdown (Best Balanced)")
    col1, col2, col3 = st.columns(3)

    col1.metric("Deviation Penalty", best_metrics["deviation"])
    col2.metric("Workload Penalty", best_metrics["workload"])
    col3.metric("Global Fitness", best_metrics["global"])

    # =========================
    # FINAL SCHEDULE TABLE
    # =========================
    st.subheader(f"Final Schedule – Day {day_of_month} ({day_of_week})")

    table = []
    for d in selected_departments:
        staff = best_solution[d - 1]
        demand = demand_matrix.loc[d, day_of_month]

        table.append({
            "Department": d,
            "Staff Assigned": int(staff),
            "Demand": int(demand),
            "Deviation": int(abs(staff - demand)),
            "Workload": int(staff * SHIFT_LENGTH)
        })

    st.dataframe(pd.DataFrame(table))

    # =========================
    # CONVERGENCE GRAPH
    # =========================
    st.subheader("Global Fitness Convergence (FFO)")
    st.line_chart(
        pd.DataFrame(
            {"Global Fitness": history},
            index=range(1, len(history) + 1)
        )
    )
