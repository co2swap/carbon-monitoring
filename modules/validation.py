
import pandas as pd

def validate_csv(file, required_columns=None) -> bool:
    df = pd.read_csv(file)
    if required_columns:
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Missing columns: {', '.join(missing)}")
    return True
