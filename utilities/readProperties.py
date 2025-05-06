import configparser
import os
from pathlib import Path

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
config_path = BASE_DIR.joinpath('configurations').joinpath('config.ini')
config.read(config_path)

if not os.path.exists(config_path):
    print(f"Config file {config_path} not found!")
else:
    print(f"Config file {config_path} found!")
class ReadConfig:

    @staticmethod
    def get_username():
        return config['users']['username']

    @staticmethod
    def get_password():
        return config['users']['password']

