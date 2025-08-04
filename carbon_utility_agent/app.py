import streamlit as st
from actions import get_best_action
from simulate import simulate_state
from config.emission_weights import weights

st.title("Carbon Optimization AI Agent")

st.sidebar.header("Input Parameters")
emissions = st.sidebar.slider("Current Emissions (kg CO₂)", 50, 500, 100)
cost = st.sidebar.slider("Current Cost (₹ in thousands)", 10, 200, 50)
compliance = st.sidebar.slider("Compliance Score", 0, 10, 5)
renewable = st.sidebar.slider("Renewable Share (%)", 0, 100, 10)

st.sidebar.header("Utility Weights")
weights['emissions'] = st.sidebar.slider("Weight: Emissions", 0.0, 5.0, 1.5)
weights['cost'] = st.sidebar.slider("Weight: Cost", 0.0, 5.0, 1.0)
weights['compliance'] = st.sidebar.slider("Weight: Compliance", 0.0, 5.0, 2.0)
weights['renewable'] = st.sidebar.slider("Weight: Renewable", 0.0, 5.0, 1.2)

state = {
    'emissions': emissions,
    'cost': cost,
    'compliance': compliance,
    'renewable': renewable
}

st.subheader("Current State")
st.write(state)

if st.button("Recommend Best Action"):
    action, utility = get_best_action(state, weights)
    st.success(f"✅ Recommended Action: **{action}**")
    st.write(f"Estimated Utility: {utility}")
    st.write("Simulated Next State:")
    st.json(simulate_state(action, state))
