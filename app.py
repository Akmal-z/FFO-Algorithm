import streamlit as st
import numpy as np
import pandas as pd
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FFO Staff Scheduling Optimizer",
    layout="wide"
)

# =========================
# DARK UI STYLE
# =========================
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.metric-card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
.metric-title {
    font-size: 14px;
    color: #9da5b4;
}
.metric-value {
    font-size: 36px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LEFT SIDEBAR – FFO CONTROLS
# =========================
st.sidebar.title("⚙ Control Panel")

st.sidebar.subheader("1. Basic Settings")
department = st.sidebar.selectbox(
    "Select Department:",
    [1, 2, 3, 4, 5, 6]
)

st.sidebar.subheader("2. FFO Parameters")

alpha = st.sidebar.slider(
    "Randomization (α)",
    0.0, 1.0, 0.3
)

beta = st.sidebar.slider(
    "Attractiveness (β)",
    0.1, 1.0, 0.6
)

iterations = st.sidebar.slider(
    "Iterations",
    20, 200, 100
)

population_size = st.sidebar.slider(
    "Number of Fireflies",
    5, 30, 15
)

# =========================
# MAIN TITLE
# =========================
st.markdown("## 🧠 FFO Staff Scheduling Optimizer")

# =========================
# METRIC CARDS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Total Demand (Man-hours)</div>
        <div class="metric-value">208</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Matrix Dimensions</div>
        <div class="metric-value">(7, 28)</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================
# START BUTTON
# =========================
start = st.button("🚀 START OPTIMIZATION")

# =========================
# FIRELY OPTIMIZATION (FFO)
# =========================
if start:
    progress_text = st.empty()
    progress_bar = st.progress(0)

    # 🔥 Step 1: Initialize fireflies (random solutions)
    fireflies = np.random.randint(
        low=50_000,
        high=90_000,
        size=population_size
    )

    cost_history = []

    # 🔥 Step 2: Optimization loop
    for t in range(iterations):
        for i in range(population_size):
            for j in range(population_size):
                if fireflies[j] < fireflies[i]:
                    # 🔥 Move firefly i towards brighter firefly j
                    attraction = beta * (fireflies[j] - fireflies[i])
                    random_move = alpha * np.random.randn() * 1000
                    fireflies[i] += attraction + random_move

        # Save best cost (brightness)
        best_cost = np.min(fireflies)
        cost_history.append(best_cost)

        progress_bar.progress(int((t + 1) / iterations * 100))
        progress_text.text(
            f"Optimizing... Iteration {t+1}/{iterations}"
        )

        time.sleep(0.01)

    st.success("Optimization completed successfully.")

    # =========================
    # CONVERGENCE GRAPH
    # =========================
    st.markdown("### 1. Convergence Graph (Cost Reduction)")

    df_chart = pd.DataFrame({
        "Cost": cost_history
    })

    st.line_chart(df_chart)
