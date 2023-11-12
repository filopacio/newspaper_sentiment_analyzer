import yaml
from pathlib import Path


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


CURR_DIR = Path(__file__)
SRC_DIR = CURR_DIR.parents[1]
CONFIG_PATH = SRC_DIR / 'config/config.yaml'
API_KEY_PATH = SRC_DIR / 'config/api_key.yaml'


parameters = read_yaml(CONFIG_PATH)
api_key = read_yaml(API_KEY_PATH)['api_key']