import yaml
from pathlib import Path

class ConfigError(Exception):
    pass

def load_config(path: str = None) -> dict:
    project_root = Path(__file__).resolve().parent.parent

    if path is None:
        path = project_root/"config"/"config.yaml"
    else:
        path = Path(path)
    
    if not path.exists():
        raise ConfigError(f"Config file missing in {path}")
    
    with open (path, "r") as f:
        config = yaml.safe_load(f)
    
    required_sections = ["project", "data", "target", "features", "split", "model"]

    for section in required_sections:
        if section not in config:
            raise ConfigError(f"Missing section in the {path}")
    
    return config