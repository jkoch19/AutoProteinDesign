import os
import re

# Define the paths and filenames
apd=""
template_script_folder = os.path.join(apd, "2-proteinmpnn/seqs")  # Replace with the actual path
output_file_path = os.path.join(apd, "2-proteinmpnn/seqs/fixed_residues.txt")

# Read the values from the output file
with open(output_file_path, "r") as output_file:
    lines = output_file.read().splitlines()

# Iterate over the nomenclature of the template scripts
for i, line in enumerate(lines):
    # Create the filename for the new script
    script_filename = f"pdb{i}.sh"
    script_path = os.path.join(template_script_folder, script_filename)

    # Read the template script
    with open(script_path, "r") as template_file:
        template = template_file.readlines()

    # Find and replace values inside double quotes in line 16
    line_number_to_replace = 14
    current_line = template[line_number_to_replace]
    modified_line = re.sub(r'fixed_positions="[^"]+"', f'fixed_positions="{line}"', current_line)

    # Update the line in the template script
    template[line_number_to_replace] = modified_line

    # Create the new script with the modified values
    new_script_path = os.path.join(template_script_folder, script_filename)
    with open(new_script_path, "w") as new_script:
        new_script.writelines(template)

