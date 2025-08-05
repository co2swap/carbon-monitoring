import pandas as pd

def calculate_emissions(file):
    df = pd.read_csv(file)
    df["emissions"] = df["value"] * df["emission_factor"]
    scope_totals = df.groupby("scope")["emissions"].sum().reset_index()
    return df, scope_totals
