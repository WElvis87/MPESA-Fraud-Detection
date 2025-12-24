import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import load_config

class CleanDataError(Exception):
    pass

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    config = load_config()
    df = df.copy()

    required_columns = config["features"] + config["target"]

    # Check missing columns
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise CleanDataError(f"Missing columns in your dataframe: {missing}")

    # Fill missing values
    for col in required_columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Drop duplicates
    df = df.drop_duplicates()

    # # Clip upper outliers for numeric columns
    # for col in required_columns:
    #     if df[col].dtype in ["int64", "float64"]:
    #         q90 = df[col].quantile(0.9)
    #         df[col] = df[col].clip(upper=q90)

    df.reset_index(drop=True, inplace=True)
 
    return df
