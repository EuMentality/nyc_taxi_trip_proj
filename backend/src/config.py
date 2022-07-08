import yaml


def import_config(config_path: str):
        with open(config_path, "r") as f:
                return yaml.safe_load(f)