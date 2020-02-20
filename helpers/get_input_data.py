import urllib.request as request
from helpers.log_handler import Logger
import shutil
import os
import platform

# TODO using wget, download all the files designated by the input file. (step 1)
# Also convert these files to paired-end fastq format

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


def get_fastq_path():
    if platform.system() == "Windows":
        fastq_path = "C:\\Users\\Kashyap\\ncbi\\public\\sratoolkit.2.9.6-1-win64\\bin\\fastq-dump.exe"
    else:
        fastq_path = "fastq-dump"
    return fastq_path


def download_file(name, file_name, logger):
    logger.log(f"Downloading {name}")
    url = f"https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos2/sra-pub-run-11/{name}/{name}.1"
    with request.urlopen(url) as file_1:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(file_1, f)
            logger.log(f"Downloaded {name}")


def get_input_files(logger, folder_path, get_files):
    current_dir = os.getcwd()
    for i in range(0, len(data_names)):
        name = data_names[i]
        file_name = os.path.join(folder_path, name)
        if get_files:
            download_file(name, file_name, logger)
        else:
            shutil.copyfile(os.path.join(current_dir, "sample_data", f"{name}.1"),
                            os.path.join(folder_path, f"{name}.1"))
        logger.log(f"Running fastq-dump on {name}")
        os.chdir(folder_path)
        os.system(f"{get_fastq_path()} -I --split-files {name}.1")
    os.chdir(current_dir)




