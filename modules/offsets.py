import pandas as pd

def calculate_offsets(uploaded_file):
    df = pd.read_csv(uploaded_file)

    if "amount_tonnes" not in df.columns:
        raise ValueError("Missing required column: 'amount_tonnes' in uploaded offsets CSV")

    total_offsets = df["amount_tonnes"].sum()
    return df, total_offsets
