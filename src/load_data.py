import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import load_config

class LoadDataError(Exception):
    pass

def load_data(path: str = None) -> pd.DataFrame:
    config = load_config()

    if path is None:
        path = Path(config["data"]["raw"])
    else:
        path = Path(path)

    if not path.exists():
        raise LoadDataError(f"DataFrame path not found in {path}")
    
    df = pd.read_csv(path)

    required_columns = config["features"]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise LoadDataError(f"Missing Columns {missing}")

    # for col in required_columns:
    #     if col not in df.columns:
    #         raise LoadDataError(f"Missing Columns in your dataframe")
    
    return df



