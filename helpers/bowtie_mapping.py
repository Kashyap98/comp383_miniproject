import os
import platform
# TODO Create and index using bowtie2 and save the reads that map for assembly later on. Write the output. (step 4)
from Bio import Entrez, SeqIO

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


def get_bowtie_path():
    if platform.system() == "Windows":
        bowtie_path = "C:\\Users\\Kashyap\\Desktop\\bowtie2-2.3.5.1\\bowtie2"
    else:
        bowtie_path = "bowtie2"
    return bowtie_path


def get_bowtie_build_path():
    if platform.system() == "Windows":
        bowtie_build_path = "C:\\Users\\Kashyap\\Desktop\\bowtie2-2.3.5.1\\bowtie2-build"
    else:
        bowtie_build_path = "bowtie2-build"
    return bowtie_build_path


def generate_bowtie_index(logger, folder_path):
    logger.log("Downloading EF999921.fasta")
    fasta_path = os.path.join(folder_path, "EF999921.fasta")
    index_path = os.path.join(folder_path, 'EF999921')
    Entrez.email = "k.patel1098@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=" EF999921.1", rettype="fasta")
    record = SeqIO.read(handle, "fasta")
    SeqIO.write(record, fasta_path, "fasta")
    logger.log("Building index using bowtie2")
    bowtie_build_command = f"{get_bowtie_build_path()} {fasta_path} {index_path}"
    logger.log(f"bowtie index build command = {bowtie_build_command}")
    os.system(bowtie_build_command)
    logger.log("Finished building EF999921 index using bowtie2")
    bowtie_map_to_index(logger, folder_path, index_path)


def bowtie_map_to_index(logger, folder_path, index_path):
    for name in data_names:
        logger.log("Starting to map reads to bowtie index")
        one_pair_path = os.path.join(folder_path, f"{name}.1_1.fastq")
        two_pair_path = os.path.join(folder_path, f"{name}.1_2.fastq")
        name_output_path = os.path.join(folder_path, f"{name}_map.sam")
        bowtie_command = f"{get_bowtie_path()} --no-unal --quiet -x {index_path} -1 {one_pair_path}" \
                         f" -2 {two_pair_path} -S {name_output_path}"
        logger.log(f"bowtie map command = {bowtie_command}")
        os.system(bowtie_command)




