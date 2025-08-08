
import streamlit as st
import pandas as pd

def export_cdp_format(scope_totals: dict):
    cdp_df = pd.DataFrame([scope_totals])
    st.download_button(
        label="📥 Download CDP Format CSV",
        data=cdp_df.to_csv(index=False).encode('utf-8'),
        file_name="cdp_report.csv",
        mime="text/csv"
    )

def export_sbti_format(scope_totals: dict):
    sbti_df = pd.DataFrame([scope_totals])
    st.download_button(
        label="📥 Download SBTi Format CSV",
        data=sbti_df.to_csv(index=False).encode('utf-8'),
        file_name="sbti_report.csv",
        mime="text/csv"
    )
