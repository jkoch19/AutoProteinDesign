import os
import shutil

apd=""

# Define the parent directory containing all subdirectories
parent_directory = os.path.join(apd, "3-alphafold", "output")

# Define the destination directory
destination_directory = os.path.join(apd, "3-alphafold", "output_relaxed")

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Iterate over all subdirectories in the parent directory
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        if file.endswith('.pdb') and 'ranked' in file:
            source_file = os.path.join(root, file)
            subdirectory_name = os.path.basename(root)  # Get the name of the subdirectory
            destination_file = os.path.join(destination_directory, f"{subdirectory_name}_{file}")
            shutil.copy(source_file, destination_file)

print(f"All '.pdb' files with 'ranked' in their names copied to {destination_directory}")

