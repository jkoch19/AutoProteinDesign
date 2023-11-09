import os
import re

# Define the base directory path
apd=""

# Define the folder containing the PDB files and the output file
folder_path = os.path.join(apd, "1-rfdiffusion")
output_file = os.path.join(apd, "2-proteinmpnn", "seqs", "fixed_residues.txt")

# Function to extract numerical values from a file
def extract_numerical_values_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        pattern = r"REMARK PDBinfo-LABEL:\s+(\d+)\s+FIXED"
        matches = re.findall(pattern, data)
        return matches

# Get a list of PDB files in the folder and sort them
pdb_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.pdb')]
pdb_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

# Extract numerical values and write them to the output file
with open(output_file, 'w') as output:
    for filename in pdb_files:
        file_path = os.path.join(folder_path, filename)
        numerical_values = extract_numerical_values_from_file(file_path)
        if numerical_values:
            output.write(' '.join(numerical_values) + '\n')

print(f"Fixed residue values have been written to {output_file}")

