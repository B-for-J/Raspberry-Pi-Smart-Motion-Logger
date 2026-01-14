import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("data/motion_log.csv")

def log_motion():
    LOG_FILE.parent.mkdir(exist_ok=True)

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), "Motion detected"])
