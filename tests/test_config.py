from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import load_config

try:
    config = load_config()
    print("Config file Loaded Successfully")
    print("Project Name:", config["project"]["name"])

except Exception as e:
    print("Failed to load config file", e)