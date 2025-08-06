import pandas as pd

def calculate_emissions(uploaded_file):
    df = pd.read_csv(uploaded_file)

    required_cols = ["value", "emission_factor"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: '{col}' in uploaded CSV")

    df["emissions"] = df["value"] * df["emission_factor"]
    df["scope"] = df.get("scope", "Scope 1")
    scope_totals = df.groupby("scope")["emissions"].sum().reset_index()

    return df, scope_totals
