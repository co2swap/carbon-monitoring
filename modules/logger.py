import os
import pandas as pd
from datetime import datetime

def log_event(user, action, filename):
    log_path = "logs/audit_log.csv"  # ✅ Ensures file is saved in /logs/
    os.makedirs("logs", exist_ok=True)  # ✅ Creates folder if missing

    entry = {
        "user": user,
        "action": action,
        "filename": filename,
        "timestamp": datetime.now().isoformat()
    }

    df = pd.DataFrame([entry])
    if os.path.exists(log_path):
        df.to_csv(log_path, mode="a", header=False, index=False)
    else:
        df.to_csv(log_path, index=False)
