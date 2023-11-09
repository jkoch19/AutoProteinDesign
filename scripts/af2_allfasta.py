import os
import subprocess

# Set the paths and folders
apd=""
input_folder = os.path.join(apd, "2-proteinmpnn","extracted_seqs")
output_folder = os.path.join(apd, "3-alphafold","output")
alphafold_script = "/path/to/run_docker.py"

# List all .fasta files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".fasta"):
        fasta_path = os.path.join(input_folder, filename)
        # Create the full output path by replacing the file extension with an empty string
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0])

        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Build the AlphaFold command
        command = (
            f"python3 {alphafold_script} "
            f"--fasta_paths={fasta_path} "
            "--max_template_date=2020-05-14 "
            "--model_preset=monomer "
            "--db_preset=full_dbs "
            "--data_dir=/mnt/database "
            f"--output_dir={output_path}"
        )

        try:
            print(f"Running: {command}")
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while running command: {command}")
            print(f"Error message: {e}")

