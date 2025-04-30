import configparser
from pathlib import Path

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
config_path = BASE_DIR.joinpath('configurations').joinpath('config.ini')
config.read(config_path)

class ReadConfig:

    @staticmethod
    def get_username():
        return config['user']['username']

    @staticmethod
    def get_password():
        return config['user']['password']

