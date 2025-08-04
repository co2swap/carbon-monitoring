import streamlit as st
from emissions_calc import calculate_emissions
from visualizations import bar_chart, line_chart, pie_chart

st.title("Carbon Emissions Dashboard")

df, by_scope = calculate_emissions()

st.sidebar.header("Filters")
scopes = st.sidebar.multiselect("Select Scopes", df["scope"].unique(), default=df["scope"].unique())
filtered_df = df[df["scope"].isin(scopes)]

st.subheader("Emissions Data")
st.dataframe(filtered_df)

st.subheader("Total Emissions by Scope")
st.write(by_scope)

st.plotly_chart(bar_chart(filtered_df))
st.plotly_chart(line_chart(filtered_df))
st.plotly_chart(pie_chart(filtered_df))
