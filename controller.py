import argparse
import os

# This will be the script that is called first and will call all the other python scripts / handle outputs.
# TODO Handle input of data, create output directory and log files, call the scripts in order of tasks needed to
# complete the task.


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--name', metavar='--name', type=str, nargs='+',
                    help='a name for your test run')


def create_test_folder():
    args = parser.parse_args()
    folder_name = os.path.join(os.getcwd(), f"miniProject_{str(args.name[0]).replace(' ', '_')}")

    if os.path.exists(folder_name):
        print("Folder name already exits. Please run cleaner.py")
    else:
        os.mkdir(folder_name)


create_test_folder()



