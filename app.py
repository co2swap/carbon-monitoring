
import os
import pandas as pd
os.makedirs("logs", exist_ok=True)  # ✅ ensures the log folder exists
import streamlit as st
from modules.auth import check_login
from modules.emissions import calculate_emissions
from modules.offsets import calculate_offsets
from modules.visuals import show_charts
from modules.logger import log_event
from modules.brsr import export_brsr_format
from modules.compliance import export_cdp_format, export_sbti_format


st.set_page_config(page_title="Carbon Tracker", layout="wide")
st.title("🌱 Carbon Tracking Dashboard")

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    username = check_login()
    if username:
        st.session_state.user = username
        st.rerun()
else:
    username = st.session_state.user
    st.sidebar.write(f"👤 Logged in as: {username}")
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Emissions", "🌿 Offsets", "📁 Reports", "📝 Audit Logs"])

    with tab1:
        st.header("Upload Emissions CSV")
        uploaded_emissions = st.file_uploader("Emissions File", type=["csv"])
        if uploaded_emissions:
            emissions_df, scope_totals = calculate_emissions(uploaded_emissions)
            log_event(username, 'upload_emissions', uploaded_emissions.name)
            st.metric("Total Emissions (tCO2e)", round(scope_totals["total"], 2))
            show_charts(emissions_df)
        else:
            st.info("Using sample emissions data")
            sample = "data/carbon_data.csv"
            emissions_df, scope_totals = calculate_emissions(sample)
            st.metric("Total Emissions (tCO2e)", round(scope_totals["total"], 2))
            show_charts(emissions_df)

    with tab2:
        st.header("Upload Offsets CSV")
        uploaded_offsets = st.file_uploader("Offset File", type=["csv"], key="offset")
        if uploaded_offsets:
            offsets_df, total_offsets = calculate_offsets(uploaded_offsets)
            log_event(username, 'upload_offset', uploaded_offsets.name)
            st.metric("Total Offsets (tCO2e)", round(total_offsets, 2))
            st.dataframe(offsets_df)

    with tab3:
        st.markdown("### 📁 Export Compliance Reports")
        st.write("Generate carbon emissions reports in the formats required by regulatory and voluntary disclosure frameworks:")

        if "scope_totals" in locals() and isinstance(scope_totals, dict):
            st.markdown("#### 🔄 BRSR Report")
            st.caption("For SEBI Business Responsibility and Sustainability Reporting")
            export_brsr_format(scope_totals)
            st.divider()

            st.markdown("#### 📄 CDP Report")
            st.caption("For Carbon Disclosure Project submissions")
            export_cdp_format(scope_totals)
            st.divider()

            st.markdown("#### 🌍 SBTi Report")
            st.caption("For Science Based Targets initiative tracking")
            export_sbti_format(scope_totals)
        else:
            st.info("📤 Please upload emissions data first to generate reports.")

    with tab4:
        st.subheader("📄 Audit Logs")

        log_path = "logs/audit_log.csv"

        if os.path.exists(log_path):
            logs = pd.read_csv(log_path)
            st.dataframe(logs)

            # 🧹 Clear Logs button
            if st.button("🧹 Clear Logs"):
                os.remove(log_path)
                st.success("Logs cleared. Please refresh the app.")
        else:
            st.info("No audit logs found.")
