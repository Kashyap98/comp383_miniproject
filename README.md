# COMP 383 MiniProject
### By: Kashyap Patel

## Requirements
These requirements are needed to run the project. You will need to run a Unix based environment such as Linux/MacOS.

**Python 3.6.x (For example 3.6.3)** 
https://www.python.org/downloads/release/python-363/

**BioPython**
https://biopython.org/wiki/Download

**R**
https://www.r-project.org/

**Kallisto**
https://pachterlab.github.io/kallisto/download.html

**Bowtie2**
http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#obtaining-bowtie-2

**Spades**
http://cab.spbu.ru/files/release3.14.0/manual.html

**Fastq-dump**
https://ncbi.github.io/sra-tools/fastq-dump.html

## Usage
### Get the repo
Run the following command in the directory you would like the project to reside in.

`git clone https://github.com/Kashyap98/comp383_miniproject.git`

Enter the project directory 
`cd comp383_miniproject/`

### Run controller.py
controller.py is the center of the entire operation. 

NOTE: If you have multiple versions of python installed on your system replace the `python` part of the commands with `python3`.

Identify the args necessary for the smooth operation of this miniproject pipeline.

`python controller.py -h`

Run the sample data set with this command. Will not run in quiet mode.

`python controller.py --name sample_test`

#### Args:
`--name [name]`: (Required) The name of your test folder and log file inside the folder. miniProject_[name]

`--test_data [y\n]`: (Default: y) Determine if you should download the full sra files or use the sample test data provided. y uses sample test data while n downloads new sra files. 

`--quiet [y\n]`: (Default: n) Determine if logger should also output to terminal in addition to the log file generated in the test folder. y does not output to terminal while n outputs to both log file and terminal.

### Run cleaner.py

If you have too many test folders created you can run `python cleaner.py` to remove the test folders. It will prompt you with a 'y' or 'n' confirmation of folder deletion (this is irreversible).

 
