import urllib.request as request
import shutil
import os
import platform

# using wget, download all the files designated by the input file. (step 1)
# Also convert these files to paired-end fastq format

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


# used for testing on local machine
def get_fastq_path():
    if platform.system() == "Windows":
        fastq_path = "C:\\Users\\Kashyap\\ncbi\\public\\sratoolkit.2.9.6-1-win64\\bin\\fastq-dump.exe"
    else:
        fastq_path = "fastq-dump"
    return fastq_path


# download the sra file and place it in the test folder
def download_file(name, file_name, logger):
    logger.log(f"Downloading {name}")
    url = f"https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos2/sra-pub-run-11/{name}/{name}.1"
    with request.urlopen(url) as file_1:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(file_1, f)
            logger.log(f"Downloaded {name}")


def get_input_files(logger, folder_path, test_data):
    current_dir = os.getcwd()
    for name in data_names:
        file_name = os.path.join(folder_path, name)
        # determine if you are running the test or not
        if not test_data:
            # download the sra file and split into fastq using fastq-dump
            download_file(name, file_name, logger)
            logger.log(f"Running fastq-dump on {name}")
            os.chdir(folder_path)
            os.system(f"{get_fastq_path()} -I --split-files {name}")
        else:
            # copy test data from the sample data folder into test folder
            shutil.copyfile(os.path.join(current_dir, "sample_data", f"{name}_1.fastq"),
                            os.path.join(folder_path, f"{name}_1.fastq"))
            shutil.copyfile(os.path.join(current_dir, "sample_data", f"{name}_2.fastq"),
                            os.path.join(folder_path, f"{name}_2.fastq"))

    os.chdir(current_dir)




