import plotly.express as px
import pandas as pd

def bar_chart(df):
    return px.bar(df, x="source", y="emissions", color="scope", title="Emissions by Source")

def line_chart(df):
    df["date"] = pd.to_datetime(df["date"])
    daily = df.groupby("date")["emissions"].sum().reset_index()
    return px.line(daily, x="date", y="emissions", title="Total Emissions Over Time")

def pie_chart(df):
    pie = df.groupby("scope")["emissions"].sum().reset_index()
    return px.pie(pie, values="emissions", names="scope", title="Emissions by Scope")
