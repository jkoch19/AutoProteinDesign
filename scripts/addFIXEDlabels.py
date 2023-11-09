#!/usr/bin/env python

import numpy as np
import os
import argparse

apd=""

# Automatically set pdbdir and trbdir to apd/1-rfdiffusion/
pdbdir = os.path.join(apd, "1-rfdiffusion/")
trbdir = pdbdir  # Set trbdir to the same directory as pdbdir

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true", default=False)
args = parser.parse_args()

pdb_list = os.listdir(pdbdir)

for pdb in pdb_list:

    if not pdb.endswith(".pdb"):
        if args.verbose:
            print(f"Skipping {pdb} as it is not a PDB file")
        continue

    pdb_path = os.path.join(pdbdir, pdb)

    trb_path = os.path.join(trbdir, f'{pdb.split(".")[0]}.trb')

    if not os.path.exists(trb_path):
        print(f"Error: TRB file not found for PDB {pdb}")
        continue

    data = np.load(trb_path, allow_pickle=True)

    if 'receptor_con_hal_pdb_idx' in data:
        # Identify the last residue number in A chain
        last_res_id = int(data['receptor_con_hal_pdb_idx'][0][1]) - 1

        # Identify where inpaint seq is True, i.e., kept fixed
        indices = np.where(data['inpaint_seq'][:last_res_id])[0]
    else:
        # Identify where inpaint seq is True in the only chain
        indices = np.where(data['inpaint_seq'])[0]

    if args.verbose:
        print(f"Adding FIXED labels to {pdb} at positions {indices}")

    remarks = []
    for position in indices:
        remark = f"REMARK PDBinfo-LABEL:{position+1: >5} FIXED"
        remarks.append(remark)

    # Read the existing content of the PDB file
    with open(pdb_path, 'r') as f:
        lines = f.readlines()

    # Remove previous instances of the remarks
    new_lines = [line for line in lines if not line.startswith("REMARK PDBinfo-LABEL:")]

    # Uncomment below to add hotspots
    remarks_str = '\n'.join(remarks)
    with open(pdb_path, 'w') as f:
        f.writelines(new_lines)
        f.write('\n')
        f.write(remarks_str)

