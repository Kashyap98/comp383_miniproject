import os
# TODO Handle all of the logging for the wrapper


class Logger():

    def __init__(self, folder_path, quiet_arg):
        self.folder_path = folder_path
        self.log_file_name = os.path.basename(folder_path[12:])
        self.file_path = os.path.join(self.folder_path, f"{self.log_file_name}.txt")
        self.quiet_mode = self.get_quiet_mode(quiet_arg[0])

        self.create_log_file()

    def log(self, input_log):
        with open(self.file_path, "w+") as log_file:
            log_file.write(f"{input_log}\n")
            if not self.quiet_mode:
                print(str(input_log))

    def create_log_file(self):
        self.log("Creating Log File")

    def get_quiet_mode(self, quiet_arg):
        if quiet_arg == "y":
            return True
        else:
            return False



