import os
import shutil
from Colors import Colors


class BackupManager:
    def __init__(self, source_directory, destination_directory):
        self.source_directory = source_directory
        self.destination_directory = destination_directory

    def create_backup(self):
        os.makedirs(self.destination_directory, exist_ok=True)
        files = os.listdir(self.source_directory)
        print("Files: ", files)

        success = False
        try:
            for file in files:
                source_path = os.path.join(self.source_directory, file)
                print("Source Path: ", source_path)
                destination_path = os.path.join(self.destination_directory, file)
                print("Destination Path: ", destination_path)

                if file == 'UserOption.sav':
                    shutil.copy(source_path, destination_path)
                else:
                    shutil.copytree(source_path, destination_path)
                    success = True

        except Exception as e:
            success = False
            print(f"{Colors.fail}Error was encountered", e)
            input(f"{Colors.endc}Press enter to close...")
        else:
            print("Backup success!")
            input("Press enter to exit...")
