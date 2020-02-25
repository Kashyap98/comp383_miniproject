import argparse
import os

from helpers.get_contig_info import count_filtered_contig_bp_and_append
from helpers.log_handler import Logger
from helpers.get_input_data import get_input_files
from helpers.kallisto_helper import retrieve_genbank
from helpers.bowtie_mapping import generate_bowtie_index

# This will be the script that is called first and will call all the other python helpers / handle outputs.
# TODO Handle input of data, create output directory and log files, call the helpers in order of tasks needed to
# complete the task.
from helpers.spades_helper import assemble_transcriptomes_into_assembly

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--name', metavar='name', type=str, nargs='+',
                    help='a name for your test run')
parser.add_argument('--quiet', metavar='quiet', type=str, nargs='+',
                    help='y to log to console, n to only log to log file.', default="n")
parser.add_argument('--get_files', metavar='get_files', type=str, nargs='+',
                    help='y to download new files, n to use sample data.', default="n")


def create_test_folder(args):
    folder_name = str(args.name[0]).replace(' ', '_')
    if folder_name is None or folder_name == "":
        print("Invalid folder name")
        return None
    folder_path = os.path.join(os.getcwd(), f"miniProject_{folder_name}")

    if os.path.exists(folder_path):
        print("Folder name already exits. Please run cleaner.py")
    else:
        os.mkdir(folder_path)
        return folder_path


def arg_get_files(input_arg):
    if input_arg == "y":
        return True
    else:
        return False


args = parser.parse_args()
# folder_path = create_test_folder(args)
folder_path = os.path.join(os.getcwd(), "miniProject_kashyap")
if not folder_path:
    exit()
logger = Logger(folder_path, args.quiet[0])
# get_files = arg_get_files(args.get_files[0])
# get_input_files(logger, folder_path, get_files)
# retrieve_genbank(logger, folder_path)
generate_bowtie_index(logger, folder_path)
assemble_transcriptomes_into_assembly(logger, folder_path)
count_filtered_contig_bp_and_append(logger, folder_path)
