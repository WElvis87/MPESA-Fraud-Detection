from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.load_data import load_data

try:
    df = load_data()
    print("Data Loaded Successfully", df.columns.tolist())

except Exception as e:
    print("Failed to load the data", e)