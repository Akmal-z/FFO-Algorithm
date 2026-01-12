# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization
from config import DEPARTMENTS, DAYS_OF_WEEK, SHIFT_LENGTH

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FFO Multi-Objective Staff Scheduling",
    layout="wide"
)

st.title("🔥 Firefly Optimization – Multi-Objective Staff Scheduling")
st.write(
    "Hard constraints: Shortage & Workload | "
    "Soft constraints: Minimum staff = 6, Shift length = 14 periods"
)

# =========================
# LOAD ORIGINAL DATASET
# =========================
demand_matrix, dataset_status = load_dataset()

st.info(f"Dataset status: {dataset_status}")
st.subheader("Original Demand Matrix (Department × Day of Month)")
st.dataframe(demand_matrix)

# =========================
# SIDEBAR – USER INPUT
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

population_size = st.sidebar.slider(
    "Population Size", 5, 30, 15
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
# EXTRACT ORIGINAL DEMAND VECTOR
# =========================
demand_vector = demand_matrix.loc[
    selected_departments, day_of_month
].values

# =========================
# RUN FFO
# =========================
if selected_departments and st.button("🚀 Run Firefly Optimization"):

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
    # PENALTY BREAKDOWN
    # =========================
    st.subheader("Penalty Breakdown (Best Balanced Solution)")
    col1, col2, col3 = st.columns(3)

    col1.metric("Shortage Penalty", best_metrics["shortage"])
    col2.metric("Workload Penalty", best_metrics["workload"])
    col3.metric("Global Fitness", best_metrics["global"])

    # =========================
    # FINAL SCHEDULING TABLE
    # =========================
    st.subheader(
        f"Final Schedule (Day {day_of_month} – {day_of_week})"
    )

    table = []
    for d in selected_departments:
        staff_assigned = best_solution[d - 1]
        demand = demand_matrix.loc[d, day_of_month]
        shortage = max(0, demand - staff_assigned)

        table.append({
            "Department": d,
            "Staff Assigned": int(staff_assigned),
            "Demand": int(demand),
            "Shortage": int(shortage),
            "Workload (Staff × Shift)": int(
                staff_assigned * SHIFT_LENGTH
            )
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
