
import streamlit as st
import plotly.express as px

def show_charts(df):
    if "emissions" not in df.columns:
        st.warning("⚠️ 'emissions' column missing.")
        return
    for group_col in ["category", "subcategory", "scope"]:
        if group_col in df.columns:
            grouped = df.groupby(group_col)["emissions"].sum().reset_index()
            st.subheader(f"📊 Emissions by {group_col.capitalize()}")
            st.plotly_chart(px.bar(grouped, x=group_col, y="emissions"))
            break
    if "scope" in df.columns:
        pie = df.groupby("scope")["emissions"].sum().reset_index()
        st.subheader("🎯 Emissions by Scope")
        st.plotly_chart(px.pie(pie, values="emissions", names="scope"))
