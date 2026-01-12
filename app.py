import streamlit as st
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FFO Staff Scheduling Optimizer",
    layout="wide"
)

# =========================
# CUSTOM DARK STYLE
# =========================
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.block-container {
    padding-top: 2rem;
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
# SIDEBAR (LEFT CONTROL PANEL)
# =========================
st.sidebar.title("⚙ Control Panel")

st.sidebar.subheader("1. Basic Settings")

department = st.sidebar.selectbox(
    "Select Department:",
    [1, 2, 3, 4, 5, 6]
)

st.sidebar.subheader("Advanced Parameters")

w = st.sidebar.slider("Inertia Weight (w)", 0.1, 1.0, 0.7)
c1 = st.sidebar.slider("Cognitive (c1)", 0.5, 2.5, 1.5)
c2 = st.sidebar.slider("Social (c2)", 0.5, 2.5, 1.5)

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
# OPTIMIZATION SIMULATION
# =========================
if start:
    progress_text = st.empty()
    progress_bar = st.progress(0)

    cost_history = []

    for i in range(100):
        time.sleep(0.01)  # simulate optimization time
        progress_bar.progress(i + 1)
        progress_text.text(f"Optimizing... Iteration {i+1}/100")

        # Dummy convergence data (replace with FFO fitness)
        cost_history.append(80000 - i * 500 + np.random.randint(-500, 500))

    st.success("Optimization completed in 0.22 seconds.")

    # =========================
    # CONVERGENCE GRAPH
    # =========================
    st.markdown("### 1. Convergence Graph (Cost Reduction)")

    fig, ax = plt.subplots()
    ax.plot(cost_history, color="#58a6ff", linewidth=2)
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Cost")
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)
