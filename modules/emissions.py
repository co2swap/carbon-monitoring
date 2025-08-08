
import pandas as pd

def calculate_emissions(file):
    df = pd.read_csv(file)
    required_cols = {"value", "emission_factor"}
    if not required_cols.issubset(df.columns):
        raise KeyError(f"Missing columns: {required_cols - set(df.columns)}")
    df["emissions"] = df["value"] * df["emission_factor"]
    totals = {
        "scope_1": df[df["scope"] == 1]["emissions"].sum(),
        "scope_2": df[df["scope"] == 2]["emissions"].sum(),
        "scope_3": df[df["scope"] == 3]["emissions"].sum(),
    }
    totals["total"] = sum(totals.values())
    return df, totals
