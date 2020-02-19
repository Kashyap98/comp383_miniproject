import argparse
import os
from scripts.log_handler import Logger
from scripts.get_input_data import get_input_files
from scripts.kallisto_helper import retrieve_genbank

# This will be the script that is called first and will call all the other python scripts / handle outputs.
# TODO Handle input of data, create output directory and log files, call the scripts in order of tasks needed to
# complete the task.


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--name', metavar='name', type=str, nargs='+',
                    help='a name for your test run')

parser.add_argument('--quiet', metavar='quiet', type=str, nargs='+',
                    help='y to log to console, n to only log to log file.', default="n")


def create_test_folder(args):
    folder_path = os.path.join(os.getcwd(), f"miniProject_{str(args.name[0]).replace(' ', '_')}")

    if os.path.exists(folder_path):
        print("Folder name already exits. Please run cleaner.py")
    else:
        os.mkdir(folder_path)
        return folder_path


args = parser.parse_args()
folder_path = create_test_folder(args)
logger = Logger(folder_path, args.quiet)
# get_input_files(logger, folder_path)
retrieve_genbank(logger, folder_path)

