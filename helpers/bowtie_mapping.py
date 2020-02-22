import os
import platform
# TODO Create and index using bowtie2 and save the reads that map for assembly later on. Write the output. (step 4)
from Bio import Entrez, SeqIO


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
    Entrez.email = "k.patel1098@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=" EF999921.1", rettype="fasta")
    record = SeqIO.read(handle, "fasta")
    SeqIO.write(record, fasta_path, "fasta")
    logger.log("Building index using bowtie2")
    bowtie_build_command = f"{get_bowtie_build_path()} {fasta_path} EF999921"
    logger.log(f"bowtie index build command = {bowtie_build_command}")
    os.system(bowtie_build_command)






