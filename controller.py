import argparse
import os

from helpers.blast_helper import blast_filtered_contigs
from helpers.get_contig_info import count_filtered_contig_bp_and_append
from helpers.log_handler import Logger
from helpers.get_input_data import get_input_files
from helpers.kallisto_helper import retrieve_genbank
from helpers.bowtie_mapping import generate_bowtie_index

# This will be the script that is called first and will call all the other python helpers / handle outputs.
from helpers.spades_helper import assemble_transcriptomes_into_assembly

# define arguments for the script.
parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument('--name', metavar='name', type=str, nargs='+',
                    help='a name for your test run')
parser.add_argument('--quiet', metavar='quiet', type=str, nargs='+',
                    help='y to only log to log file, n (default) to log to log file and print to console.', default="n")
parser.add_argument('--test_data', metavar='test_data', type=str, nargs='+',
                    help='y to download new files, n (default) to use sample data.', default="n")


def create_test_folder(args):
    folder_name = str(args.name[0]).replace(' ', '_')
    # make sure the folder name is valid
    if folder_name is None or folder_name == "":
        print("Invalid folder name")
        return None
    folder_path = os.path.join(os.getcwd(), f"miniProject_{folder_name}")

    # check if folder exists, if not make it.
    if os.path.exists(folder_path):
        print("Folder name already exits. Please run cleaner.py")
    else:
        os.mkdir(folder_path)
        return folder_path


def arg_get_files(input_arg):
    # Determine if downloading files using wget
    if input_arg == "y":
        return True
    else:
        return False


args = parser.parse_args()
folder_path = create_test_folder(args)
# folder_path = os.path.join(os.getcwd(), "miniProject_kashyap")
# exit if folder is not made.
if not folder_path:
    exit()
# run the scripts according to the instructions.
logger = Logger(folder_path, args.quiet[0])
get_files = arg_get_files(args.test_data[0])
get_input_files(logger, folder_path, get_files)
retrieve_genbank(logger, folder_path)
generate_bowtie_index(logger, folder_path)
assemble_transcriptomes_into_assembly(logger, folder_path)
count_filtered_contig_bp_and_append(logger, folder_path)
blast_filtered_contigs(logger, folder_path)
