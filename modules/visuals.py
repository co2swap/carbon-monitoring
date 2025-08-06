import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts(df):
    if "emissions" not in df.columns:
        st.warning("⚠️ 'emissions' column not found in the uploaded data.")
        return

    # Dynamically choose grouping column
    for group_col in ["category", "subcategory", "scope"]:
        if group_col in df.columns:
            st.subheader(f"📊 Emissions by {group_col.capitalize()}")
            grouped = df.groupby(group_col)["emissions"].sum().reset_index()
            st.plotly_chart(px.bar(grouped, x=group_col, y="emissions"))
            break
    else:
        st.warning("⚠️ No valid column to group by (e.g. 'category', 'subcategory', or 'scope').")

    # Pie chart by scope (if exists)
    if "scope" in df.columns:
        pie = df.groupby("scope")["emissions"].sum().reset_index()
        st.subheader("🎯 Emissions by Scope")
        st.plotly_chart(px.pie(pie, values="emissions", names="scope", title="Emissions by Scope"))
