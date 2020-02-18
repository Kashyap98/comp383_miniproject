import urllib.request as request
from scripts.log_handler import Logger
import shutil

# TODO using wget, download all the files designated by the input file. (step 1)
# Also convert these files to paired-end fastq format

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


def download_file(name, file_name, logger):
    logger.log(f"Downloading {name}_1")
    url = f"ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR566/000/{name}/{file_name}.fastq.gz"
    with request.urlopen(url) as file_1:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(file_1, f)
            logger.log(f"Downloaded {name}_1")


def get_input_files(logger, folder_path):

    for i in range(0, len(data_names)):
        name = data_names[i]
        file_name_1 = f"{name}_1"
        file_name_2 = f"{name}_2"
        download_file(name, file_name_1, logger)
        download_file(name, file_name_2, logger)

