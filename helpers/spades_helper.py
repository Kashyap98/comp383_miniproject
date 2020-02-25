import os
# TODO assemble 4 transcriptomes into 1 assembly using spades, output the command to log file. (Step 5)

data_names = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]


def convert_sam_files_to_fastq(logger, folder_path):
    for name in data_names:
        sam_path = os.path.join(folder_path, f"{name}_map.sam")
        paired_ouput = os.path.join(folder_path, f"{name}_paired.fastq")
        samtools_command = f"samtools fastq {sam_path} > {paired_ouput}"
        logger.log(f"Running samtools command = {samtools_command}")
        os.system(samtools_command)


def assemble_transcriptomes_into_assembly(logger, folder_path):
    convert_sam_files_to_fastq(logger, folder_path)
    spades_output = os.path.join(folder_path, "spades_assembly")
    spades_command = f"spades -k 55,77,99,127 -t 2 --only-assembler --pe1-12 {data_names[0]}_paired.fastq" \
                     f" --pe2-12 {data_names[1]}_paired.fastq --pe3-12 {data_names[2]}_paired.fastq" \
                     f" --pe4-12 {data_names[3]}_paired.fastq -o {spades_output}"
    logger.log(f"Running spades command = {spades_command}")
    os.system(spades_command)
