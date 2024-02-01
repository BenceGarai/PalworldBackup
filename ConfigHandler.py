import configparser
import os.path


class ConfigHandler:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config_file = config_file

    def read_config(self):
        self.config.read(self.config_file)

    def get_destination_directory(self, fallback_directory):
        return self.config.get("Backup", 'destination_directory', fallback=fallback_directory)

    def get_source_directory(self):
        return os.path.expandvars(self.config.get("Backup", 'source_directory'))
