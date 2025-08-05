import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts(df):
    pie = df.groupby("scope")["emissions"].sum().reset_index()
    st.plotly_chart(px.pie(pie, values="emissions", names="scope", title="Emissions by Scope"))

    bar = df.groupby("source")["emissions"].sum().reset_index()
    st.plotly_chart(px.bar(bar, x="source", y="emissions", title="Emissions by Source"))
