import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts(df):
    if "emissions" not in df.columns:
        st.warning("❗ 'emissions' column missing. No charts will be displayed.")
        return

    st.subheader("📊 Emissions Breakdown")

    # Bar chart by category or subcategory
    group_col = None
    for col in ["category", "subcategory", "source", "scope"]:
        if col in df.columns:
            group_col = col
            break

    if group_col:
        bar = df.groupby(group_col)["emissions"].sum().reset_index()
        st.plotly_chart(px.bar(bar, x=group_col, y="emissions", title=f"Emissions by {group_col.capitalize()}"))
    else:
        st.warning("No grouping column (like 'category' or 'scope') found in uploaded data.")

    # Pie chart by scope (if available)
    if "scope" in df.columns:
        pie = df.groupby("scope")["emissions"].sum().reset_index()
        st.plotly_chart(px.pie(pie, values="emissions", names="scope", title="Emissions by Scope"))
