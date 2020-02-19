import os
from Bio import Entrez, SeqIO
# TODO using Biopython get the genbank file by accession, build the index using CDS features, write the number of
#  features Use Kallisto to quantify the TPM and input into sleuth. Log based on assignment (Steps 2 & 3)


def retrieve_genbank(logger, folder_path):
    logger.log("Downloading cDNA")
    Entrez.email = "k.patel1098@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=" EF999921.1", rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    cdna_count = 0
    logger.log("Downloaded cDNA. Extracting CDS features")
    with open(os.path.join(folder_path, "cdna.fasta"), "w") as cdna_file:
        for feature in record.features:
            if feature.type == "CDS":
                cdna_count += 1
                cdna_file.write(f"> {feature.qualifiers['protein_id']}\n")
                cdna_file.write(f"{feature.location.extract(record).seq}\n")
    logger.log(f"Finished Extracting CDS features. The HCMV genome (EF99921) has {cdna_count} CDS.")
