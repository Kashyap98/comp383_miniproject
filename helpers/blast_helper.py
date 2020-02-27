from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
import os
from helpers import log_handler
# TODO For the top 10 hits, write the following to your log file: sequence title,
# alignment length, number of HSPs, and for the top HSP: HSP identities, HSP gaps, HSP bits, and HSP expect scores.
# Include the following header row and tab-delimit each item (Step 9)


def blast_filtered_contigs(logger, folder_path):
    logger.log("Blasting generated fasta file using blastn")
    fasta_seq = SeqIO.read(os.path.join(folder_path, "filtered_assembly_contigs.fasta"), format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nr", fasta_seq.seq, megablast=True, entrez_query="Herpesviridae[family]")
    blast_records = list(NCBIXML.parse(result_handle))
    alignment_count = 1
    logger.log("seq_title align_len number_HSPS topHSP_ident topHSP_gaps topHSP_bits topHSP_expect\n")
    for alignment in blast_records[0].alignments:
        number_HSPS = len(alignment.hsps)
        top_hsp = alignment.hsps.pop(0)
        logger.log(f"{alignment.title} {alignment.length} {number_HSPS} {top_hsp.identities} {top_hsp.gaps} "
                   f"{top_hsp.bits} {top_hsp.expect}")
        alignment_count += 1
        if alignment_count == 10:
            break

# logger = log_handler.Logger("C:\\Users\\Kashyap\\PycharmProjects\\comp383_miniproject\\miniProject_kashyap", quiet_arg=False)
# blast_filtered_contigs(logger, "C:\\Users\\Kashyap\\PycharmProjects\\comp383_miniproject\\miniProject_kashyap")



