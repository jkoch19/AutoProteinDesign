# AutoProteinDesign
A script made as a part of my master thesis. This script automates the process of protein design by combining RFDiffusion, ProteinMPNN and Alphafold.

This script is written by someone who had almost zero python programming experience before starting and heavily used ChatGPT to create the script. Therefore you have to make some small adjustments yourself to make it run (Everything you need to do is mentioned below).

This script combines the powers of RFDiffussion, Protein-MPNN and Alphafold and removes the use of manual work once everything is set up. It does NOT install anything or relies on a single conda environment, so you need to have all conda environments  beforehand and define the executables for RFDiffusion, ProteinMPNN and Alphafold.

### Need to know before running the script ###

1) RFDiffusion
You need to insert your input pdb files in the "/apd/1-rfdiffusion/input" folder.
You also need to change the RFDiffusion command in the auto_protein_design.sh script

2) ProteinMPNN
If you keep residues fixed in RFDiffusion, the addFIXEDlabels.py and iterative_fixedres.py will automatically define them for ProteinMPNN and run a bash script for each individual structure

3) Alphafold
You need to change the Alphafold command in the auto_protein_design.sh script

### Change directories! ###

Before you can run the script, you need to change directories in the following scripts:

In the "2-proteinmpnn" folder: Define the ProteinMPNN software folder for all pdb_{i}.sh bash scripts

In the "3-alphafold" folder: Define path to the alphafold script "run_docker.py" for the af2_allfasta.py python script

## Run APD
### Now you can run the script!! ###
Before you can run the auto_protein_design.sh script you have to run the change_apd.py script with:
	"python change_apd.py"
Then you can run auto_protein_design by:
	source auto_protein_design


### A bit about all the scripts ###

* addFIXEDlabels.py - A script taken from dl_binder_design which writes the fixed amino acids (from RFDiffusion) into the pdb file itself.

* rfdiffusion_movefiles.py - Moves the output pdbs into their specified folder

* iterative_fixedres.py - This reads the information that addFIXEDlabels.py wrote into the pdb file and makes executable ProteinMPNN bash scripts for each .pdb file from RFDiffusion.

* modify_mpnnbash.py - Inserts the fixed amino acids into the pdb_{i}.sh scripts

* master.sh - This runs all the executable ProteinMPNN scripts.

* extract_fastas.py - This takes the output from ProteinMPNN and gives each fasta code its own individual file (Because Alphafold does not like when you have more than one fasta code in a file).

* af2_allfasta.py - Instead of manually inserting the name of ALL fastas in the alphafold command, this script takes ALL .fasta files it can find from the PorteinMPNN output and begins to fold them.

* copy_relaxedfiles.py - Copies all ranked files from the alphafold output
