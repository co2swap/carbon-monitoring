
import pandas as pd

def calculate_offsets(file):
    df = pd.read_csv(file)
    if "value" not in df.columns:
        raise KeyError("Missing 'value' column")
    total_offsets = df["value"].sum()
    return df, total_offsets
