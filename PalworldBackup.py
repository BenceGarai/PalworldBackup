import datetime
import os
from BackupManager import BackupManager
from Colors import Colors
from ConfigHandler import ConfigHandler


def main():
    print(f"{Colors.header}\nThis program takes the files located in the local appdata folder of Palworld."
          "\nThese files are copied to the destination folder defined in the config.ini"
          "\nYou may change the destination file in the config.ini. Make sure to follow the format."
          f"\n{Colors.endc}")
    config_handler = ConfigHandler()
    config_handler.read_config()

    source_directory = os.path.expandvars(config_handler.get_source_directory())
    fallback_directory = os.path.dirname(os.path.abspath(__file__))
    base_destination_directory = config_handler.get_destination_directory(fallback_directory)

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    destination_directory = os.path.join(base_destination_directory, f"Backup_{timestamp}")

    backup_manager = BackupManager(source_directory, destination_directory)
    backup_manager.create_backup()


if __name__ == "__main__":
    main()
