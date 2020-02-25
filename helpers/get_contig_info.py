import os
from Bio import SeqIO
# TODO Output number of contigs with more than 1000 bp, from now on only consider these, and output the total number
# of base pairs in the assembly. Concat all of these contigs into 1 fasta sequence separated by 50 N's(STEP 6 & 7 & 8)

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]
N_string = ''
for _ in range(0, 50):
    N_string = N_string + 'N'


def count_filtered_contig_bp_and_append(logger, folder_path):
    contigs_path = os.path.join(folder_path, "spades_assembly", "contigs.fasta")
    filtered_contigs_count = 0
    filtered_total_length = 0
    logger.log("Filtering assembled contigs (bp > 1000)")
    with open(os.path.join(folder_path, "filtered_assembly_contigs.fasta"), "w") as filtered_contigs:
        filtered_contigs.write("> filtered assembled contigs\n")
        all_contigs = SeqIO.parse(contigs_path, "fasta")
        for contig in all_contigs:
            contig_length = len(contig.seq)
            if contig_length > 1000:
                filtered_total_length += contig_length
                filtered_contigs_count += 1
                filtered_contigs.write(f"{contig.seq}{N_string}")
    logger.log(f"There are {filtered_contigs_count} > 1000 bp in the assembly.")
    logger.log(f"There are {filtered_total_length} in the assembly.")





