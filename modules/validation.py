
import pandas as pd

REQUIRED_COLUMNS = {
    "emissions": ["date", "source", "scope", "unit", "value", "emission_factor"],
    "offsets": ["date", "source", "unit", "value", "registry", "retirement_status"]
}

VALID_SCOPES = ["Scope 1", "Scope 2", "Scope 3"]

def validate_csv(df, file_type):
    errors = []

    required = REQUIRED_COLUMNS[file_type]
    missing_cols = [col for col in required if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing columns: {', '.join(missing_cols)}")

    if file_type == "emissions" and "scope" in df.columns:
        invalid_scopes = df[~df["scope"].isin(VALID_SCOPES)]["scope"].unique()
        if len(invalid_scopes) > 0:
            errors.append(f"Invalid scope values: {', '.join(invalid_scopes)}")

    if "value" in df.columns:
        if (df["value"] < 0).any():
            errors.append("Negative values found in 'value' column.")

    return errors
