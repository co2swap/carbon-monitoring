import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts(df):
    if "emissions" not in df.columns:
        st.warning("⚠️ 'emissions' column not found in dataset.")
        return

    # Try grouping by an available column
    group_by_col = None
    for col in ["category", "subcategory", "scope"]:
        if col in df.columns:
            group_by_col = col
            break

    if group_by_col:
        bar = df.groupby(group_by_col)["emissions"].sum().reset_index()
        st.subheader(f"📊 Emissions by {group_by_col.capitalize()}")
        st.plotly_chart(px.bar(bar, x=group_by_col, y="emissions", title=f"Emissions by {group_by_col.capitalize()}"))
    else:
        st.warning("⚠️ No suitable grouping column found (e.g., 'category', 'scope').")

    if "scope" in df.columns:
        pie = df.groupby("scope")["emissions"].sum().reset_index()
        st.subheader("🎯 Emissions by Scope")
        st.plotly_chart(px.pie(pie, values="emissions", names="scope", title="Emissions by Scope"))
