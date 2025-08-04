import pandas as pd

def calculate_emissions():
    df = pd.read_csv("data/carbon_data.csv")
    df["emissions"] = df["value"] * df["emission_factor"]
    by_scope = df.groupby("scope")["emissions"].sum().reset_index()
    return df, by_scope
