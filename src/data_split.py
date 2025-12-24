from sklearn.model_selection import train_test_split
import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import load_config

class DataSplitError(Exception):
    pass

def split_data(df):
    config = load_config()

    target = config["target"]
    features = config["features"]

    # Check target column
    missing_target = [col for col in target if col not in df.columns]
    if missing_target:
        raise DataSplitError(f"Missing target column: {missing_target}")

    # Check feature columns
    missing_features = [col for col in features if col not in df.columns]
    if missing_features:
        raise DataSplitError(f"Missing feature columns: {missing_features}")

    # Create X and y
    X = df[features]
    y = df[target[0]]

    test_size = config["split"]["test_size"]
    random_state = config["split"]["random_state"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    return X_train, X_test, y_train, y_test
