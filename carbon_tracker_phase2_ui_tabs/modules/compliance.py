import streamlit as st
import pandas as pd
import datetime

def export_cdp_format(scope_totals):
    today = datetime.date.today()
    data = {
        "CDP Question": [
            "Scope 1 emissions (tCO2e)",
            "Scope 2 emissions (tCO2e)",
            "Scope 3 emissions (tCO2e)",
            "Emissions change YOY",
            "Boundary methodology",
            "Third-party verification"
        ],
        "Response": [
            get_scope_emissions(scope_totals, 1),
            get_scope_emissions(scope_totals, 2),
            get_scope_emissions(scope_totals, 3),
            "Not available",
            "Operational control",
            "No"
        ]
    }
    df = pd.DataFrame(data)
    st.subheader("Download CDP Report")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CDP Format (CSV)", csv, f"cdp_report_{today}.csv", "text/csv")

def export_sbti_format(scope_totals):
    today = datetime.date.today()
    base_year = today.year
    target_year = base_year + 5
    base_total = scope_totals["emissions"].sum()
    reduction_needed = round(base_total * 0.42, 2)
    target_total = round(base_total - reduction_needed, 2)
    data = {
        "Field": [
            "Year", "Scope 1 emissions", "Scope 2 emissions", "Scope 3 emissions",
            "Target year", "Target reduction (%)", "Reduction needed (tCO2e)", "Projected emissions target"
        ],
        "Value": [
            base_year,
            get_scope_emissions(scope_totals, 1),
            get_scope_emissions(scope_totals, 2),
            get_scope_emissions(scope_totals, 3),
            target_year,
            "42%",
            reduction_needed,
            target_total
        ]
    }
    df = pd.DataFrame(data)
    st.subheader("Download SBTi Report")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download SBTi Format (CSV)", csv, f"sbti_report_{today}.csv", "text/csv")

def get_scope_emissions(df, scope_level):
    match = df[df["scope"] == scope_level]
    return round(match["emissions"].sum(), 2) if not match.empty else 0
