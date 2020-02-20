import os
from Bio import Entrez, SeqIO
import platform
# TODO using Biopython get the genbank file by accession, build the index using CDS features, write the number of
#  features Use Kallisto to quantify the TPM and input into sleuth. Log based on assignment (Steps 2 & 3)


def get_kallisto_path():
    if platform.system() == "Windows":
        kallisto_path = "C:\\Users\\Kashyap\\Desktop\\kallisto\\kallisto.exe"
    else:
        kallisto_path = "kallisto"
    return kallisto_path


def retrieve_genbank(logger, folder_path):
    cdna_path = os.path.join(folder_path, "cdna.fasta")
    if False:
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
                    cdna_file.write(f"> {feature.qualifiers['protein_id'][0]}\n")
                    cdna_file.write(f"{feature.location.extract(record).seq}\n")
        logger.log(f"Finished Extracting CDS features. The HCMV genome (EF99921) has {cdna_count} CDS.")
    build_index(logger, folder_path, cdna_path)


def build_index(logger, folder_path, cdna_path):
    logger.log("Building index using Kallisto")
    kallisto_command = f"{get_kallisto_path()} index -i {os.path.join(folder_path, 'index.idx')} {cdna_path} --make-unique"
    logger.log(f"Running Kallisto command: {kallisto_command}")
    os.system(kallisto_command)
    logger.log("Finished building index")


