import os
#  assemble 4 transcriptomes into 1 assembly using spades, output the command to log file. (Step 5)

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


# helper function to generalize the creation of the spades command
def generate_spades_fastq_path(folder_name, name, number):
    return os.path.join(folder_name, f"{name}_paired.{number}.fastq")


def assemble_transcriptomes_into_assembly(logger, folder_path):
    # run spades on all the mapped paired output from bowtie in order to generate assembly
    spades_output = os.path.join(folder_path, "spades_assembly")
    spades_command = f"spades -k 55,77,99,127 -t 4 --only-assembler" \
                     f" --pe1-1 {generate_spades_fastq_path(folder_path, data_names[0], 1)}" \
                     f" --pe1-2 {generate_spades_fastq_path(folder_path, data_names[0], 2)}" \
                     f" --pe2-1 {generate_spades_fastq_path(folder_path, data_names[1], 1)}" \
                     f" --pe2-2 {generate_spades_fastq_path(folder_path, data_names[1], 2)}" \
                     f" --pe3-1 {generate_spades_fastq_path(folder_path, data_names[2], 1)}" \
                     f" --pe3-2 {generate_spades_fastq_path(folder_path, data_names[2], 2)}" \
                     f" --pe4-1 {generate_spades_fastq_path(folder_path, data_names[3], 1)}" \
                     f" --pe4-2 {generate_spades_fastq_path(folder_path, data_names[3], 2)}" \
                     f" -o {spades_output}"
    logger.log(f"Running spades command = {spades_command}")
    os.system(spades_command)
