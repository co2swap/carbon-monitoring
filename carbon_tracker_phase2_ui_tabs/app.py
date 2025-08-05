import streamlit as st
from modules.auth import require_login
from modules.logger import log_event
from modules.emissions import calculate_emissions
from modules.offsets import calculate_offsets
from modules.visuals import show_charts
from modules.brsr import export_brsr_format
from modules.compliance import export_cdp_format, export_sbti_format
import pandas as pd
import os

st.set_page_config(page_title="Carbon Tracker", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.title("🌍 Carbon Tracker Login")
    username = st.text_input("Enter username to continue")
    if username:
        st.session_state["username"] = username
        st.session_state["logged_in"] = True
        st.rerun()
    st.stop()

username = st.session_state["username"]
st.sidebar.success(f"Logged in as: {username}")

st.title("🌱 Carbon Tracking Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Emissions", "🌿 Offsets", "📁 Reports", "📝 Audit Logs"])

with tab1:
    st.subheader("Upload Emissions CSV")
    uploaded_emissions = st.file_uploader("Emissions File", type="csv", key="em_file")
    if uploaded_emissions:
        emissions_df, scope_totals = calculate_emissions(uploaded_emissions)
        log_event(username, 'upload', uploaded_emissions.name)
    else:
        st.info("Using sample emissions data")
        with open("data/carbon_data.csv", "rb") as f:
            emissions_df, scope_totals = calculate_emissions(f)

    st.metric("Total Emissions (tCO2e)", round(scope_totals["emissions"].sum(), 2))
    st.dataframe(emissions_df)
    show_charts(emissions_df)

with tab2:
    st.subheader("Upload Offset CSV")
    uploaded_offsets = st.file_uploader("Offset File", type="csv", key="offset_file")
    if uploaded_offsets:
        offsets_df, total_offsets = calculate_offsets(uploaded_offsets)
        log_event(username, 'upload', uploaded_offsets.name)
    else:
        st.info("Using sample offset data")
        with open("data/offset_data.csv", "rb") as f:
            offsets_df, total_offsets = calculate_offsets(f)

    st.metric("Total Offsets (tCO2e)", total_offsets)
    st.dataframe(offsets_df)

with tab3:
    st.subheader("📁 Export Reports")
    export_brsr_format(scope_totals)
    export_cdp_format(scope_totals)
    export_sbti_format(scope_totals)

with tab4:
    st.subheader("📄 Audit Logs")
    if os.path.exists("logs/audit_log.csv"):
        logs = pd.read_csv("logs/audit_log.csv")
        st.dataframe(logs)
    else:
        st.warning("No audit logs found.")
