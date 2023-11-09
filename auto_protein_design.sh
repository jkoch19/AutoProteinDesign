#!/bin/bash

#Folder directory of auto_protein-design
apd=""
	#Program directories
#RFDiffusion folder
run_inference_path="path/to/RFdiffusion"	

conda deactivate
#1 RF Diffusion
conda activate SE3nv

cd $run_inference_path

./scripts/run_inference.py 'contigmap.contigs=[20-50/A347-350/0-50/A403-403/0-50/A411-411/0-50/A450-452/0-50/A537-537/0-50/A568-568/20-50/A569-572/0-50/A593-593/20-50]' contigmap.length=150-250 inference.output_prefix=$apd/1-rfdiffusion/pdb inference.input_pdb=$apd/1-rfdiffusion/input/model3x2_ph52.pdb inference.num_designs=10 inference.ckpt_override_path=models/ActiveSite_ckpt.pt

cd $apd/scripts/

#Adds lines that describe which amino acids are fixed
python addFIXEDlabels.py

python rfdiffusion_movefiles.py

conda deactivate

#2 ProteinMPNN
conda activate mlfold

python iterative_fixedres.py # Generates bash scripts for ProteinMPNN for all fastas with the fixed residues included

python modify_mpnnbash.py

cd $apd/2-proteinmpnn/seqs
chmod +x master.sh
chmod a+x *.sh
./master.sh #Runs ProteinMPNN

cd $apd/scripts
chmod a+x extract_fastas.py
python extract_fastas.py

conda deactivate

#3 AlphaFold

conda activate
python af2_allfasta.py

python copy_relaxedfiles.py # Copies all of the relaxed alphafold files to the same folder

cd $apd/3-alphafold/output_relaxed/
ls
conda deactivate

