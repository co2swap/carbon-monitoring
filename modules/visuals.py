import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts(df):
    import streamlit as st
    import plotly.express as px

    # Validate necessary columns
    for col in ["category", "emissions"]:
        if col not in df.columns:
            st.warning(f"Missing column '{col}' in emissions data. Chart cannot be displayed.")
            return

    bar = df.groupby("category")["emissions"].sum().reset_index()
    st.subheader("📊 Emissions by Category")
    st.plotly_chart(px.bar(bar, x="category", y="emissions", title="Emissions by Category"))

    pie = df.groupby("scope")["emissions"].sum().reset_index()
    st.subheader("🎯 Emissions by Scope")
    st.plotly_chart(px.pie(pie, values="emissions", names="scope", title="Emissions by Scope"))
