import os
import platform
# TODO Create and index using bowtie2 and save the reads that map for assembly later on. Write the output. (step 4)
from Bio import Entrez, SeqIO

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]
donors = ['Donor 1 (2dpi)', 'Donor 1 (6dpi)', 'Donor 3 (2dpi)', 'Donor 3 (6dpi)']


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


def get_number_of_fastq_genes(fastq_path):
    count = 0
    with open(fastq_path, "r") as sam_file:
        lines = sam_file.readlines()
        for line in lines:
            if line.startswith("@"):
                count += 1
    return count


def get_number_of_sam_genes(sam_path):
    with open(sam_path, "r") as sam_file:
        lines = sam_file.readlines()
        return len(lines[3:])


def generate_bowtie_index(logger, folder_path):
    logger.log("Downloading EF999921.fasta")
    fasta_path = os.path.join(folder_path, "cdna.fasta")
    index_path = os.path.join(folder_path, 'EF999921')
    logger.log("Building index using bowtie2")
    bowtie_build_command = f"{get_bowtie_build_path()} {fasta_path} {index_path}"
    logger.log(f"bowtie index build command = {bowtie_build_command}")
    os.system(bowtie_build_command)
    logger.log("Finished building EF999921 index using bowtie2")
    bowtie_map_to_index(logger, folder_path, index_path)


def bowtie_map_to_index(logger, folder_path, index_path):
    logger.log("Starting to map reads to bowtie index")
    current_name = 0
    for name in data_names:
        one_pair_path = os.path.join(folder_path, f"{name}_1.fastq")
        two_pair_path = os.path.join(folder_path, f"{name}_2.fastq")
        paired_output = os.path.join(folder_path, f"{name}_paired.fastq")
        # init_count = len(list(SeqIO.parse(one_pair_path, "fastq"))) + len(list(SeqIO.parse(two_pair_path, "fastq")))
        init_count = get_number_of_fastq_genes(one_pair_path) + get_number_of_fastq_genes(two_pair_path)
        name_output_path = os.path.join(folder_path, f"{name}_map.sam")
        if not platform.system() == "Windows":
            bowtie_command = f"{get_bowtie_path()} --no-unal --quiet -x {index_path} -1 {one_pair_path}" \
                             f" -2 {two_pair_path} -S {name_output_path} --al-conc {paired_output}"
            logger.log(f"bowtie map command = {bowtie_command}")
            os.system(bowtie_command)
        new_count = get_number_of_sam_genes(name_output_path)
        logger.log(f"{donors[current_name]} had {init_count} read pairs before Bowtie2 filtering and {new_count} read pairs after.")
        current_name += 1




