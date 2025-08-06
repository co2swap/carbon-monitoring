import streamlit as st
import pandas as pd

def export_brsr_format(scope_totals):
    st.subheader("Download BRSR Format Output")
    brsr_df = scope_totals.rename(columns={"scope": "Scope", "emissions": "Total Emissions (tCO2e)"})
    csv = brsr_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download BRSR Report (CSV)", csv, "brsr_output.csv", "text/csv")
