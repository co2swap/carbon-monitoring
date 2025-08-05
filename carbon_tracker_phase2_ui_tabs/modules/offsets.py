import pandas as pd

def calculate_offsets(file):
    df = pd.read_csv(file)
    total_offsets = df["value"].sum()
    return df, total_offsets
