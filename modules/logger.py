import pandas as pd
from datetime import datetime
import os

def log_event(username, action, filename):
    log_path = "logs/audit_log.csv"
    os.makedirs("logs", exist_ok=True)  # Ensure 'logs' directory exists
    entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Username": username,
        "Action": action,
        "Target File": filename
    }
    df = pd.DataFrame([entry])
    if os.path.exists(log_path):
        df.to_csv(log_path, mode="a", header=False, index=False)
    else:
        df.to_csv(log_path, index=False)
