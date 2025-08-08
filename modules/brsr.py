
import streamlit as st
import pandas as pd

def export_brsr_format(scope_totals: dict):
    brsr_df = pd.DataFrame([scope_totals])
    st.download_button(
        label="📥 Download BRSR Format CSV",
        data=brsr_df.to_csv(index=False).encode('utf-8'),
        file_name="brsr_report.csv",
        mime="text/csv"
    )
