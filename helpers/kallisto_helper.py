import os
from Bio import Entrez, SeqIO
import platform
import glob
# TODO using Biopython get the genbank file by accession, build the index using CDS features, write the number of
#  features Use Kallisto to quantify the TPM and input into sleuth. Log based on assignment (Steps 2 & 3)

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


def get_kallisto_path():
    if platform.system() == "Windows":
        kallisto_path = "C:\\Users\\Kashyap\\Desktop\\kallisto\\kallisto.exe"
    else:
        kallisto_path = "kallisto"
    return kallisto_path


def get_r_path():
    if platform.system() == "Windows":
        r_path = 'C:\\"Program Files"\\R\\R-3.6.1\\bin\\Rscript.exe'
    else:
        r_path = "Rscript"
    return r_path


def get_condition(name):
    if name == data_names[0] or name == data_names[2]:
        condition = "HCMV2"
    else:
        condition = "HCMV6"
    return condition


def retrieve_genbank(logger, folder_path):
    cdna_path = os.path.join(folder_path, "cdna.fasta")
    logger.log("Downloading cDNA")
    Entrez.email = "k.patel1098@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=" EF999921.1", rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    cdna_count = 0
    logger.log("Downloaded cDNA. Extracting CDS features")
    with open(cdna_path, "w") as cdna_file:
        for feature in record.features:
            if feature.type == "CDS":
                cdna_count += 1
                cdna_file.write(f">{feature.qualifiers['protein_id'][0]}\n")
                cdna_file.write(f"{feature.location.extract(record).seq}\n")
    logger.log(f"Finished Extracting CDS features. The HCMV genome (EF99921) has {cdna_count} CDS.")
    build_index(logger, folder_path, cdna_path)


def build_index(logger, folder_path, cdna_path):
    index_path = os.path.join(folder_path, 'index.idx')
    logger.log("Building index using Kallisto")
    kallisto_command = f"{get_kallisto_path()} index -i {index_path} {cdna_path} --make-unique"
    logger.log(f"Running Kallisto command = {kallisto_command}")
    os.system(kallisto_command)
    logger.log("Finished building index")
    quantify_data(logger, folder_path, index_path)


def quantify_data(logger, folder_path, index_path):
    logger.log("Quantifying data")
    table_path = os.path.join(folder_path, "quant_table.txt")
    with open(table_path, "w") as quant_table:
        quant_table.write("sample condition path\n")
        for name in data_names:
            name_path = os.path.join(folder_path, name)
            results_path = os.path.join(folder_path, f"results_{name}")
            quantify_kallisto_command = f"{get_kallisto_path()} quant -i {index_path} -o {results_path} -b 30 -t 4 {name_path}.1_1.fastq {name_path}.1_2.fastq"
            logger.log(f"Running Kallisto command = {quantify_kallisto_command}")
            os.system(quantify_kallisto_command)
            quant_table.write(f"{name} {get_condition(name)} {results_path}\n")
    run_sleuth(logger, folder_path, table_path)


def run_sleuth(logger, folder_path, table_path):
    logger.log("Running Sleuth")
    output_path = os.path.join(folder_path, f"sleuth_output.txt")
    sleuth_command = f"{get_r_path()} mini_sleuth.R {table_path} {output_path}"
    logger.log(f"Running R (Sleuth) script = {sleuth_command}")
    os.system(sleuth_command)

    with open(output_path, "r") as sleuth_output:
        lines = sleuth_output.readlines()
        header = lines[0].split(" ")
        logger.log(f"{header[0]} {header[3]} {header[1]} {header[2]}\n")
        for line in lines[1:11]:
            line_info = line.split(" ")
            logger.log(f"{line_info[0]} {line_info[3]} {line_info[1]} {line_info[2]}\n")






