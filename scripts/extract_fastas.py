import os

apd=""

# Input and output folders
input_base_folder = os.path.join(apd, "2-proteinmpnn", "seqs")
output_folder = os.path.join(apd, "2-proteinmpnn", "extracted_seqs")

try:
    # Ensure the output folder exists; create it if it doesn't
    os.makedirs(output_folder, exist_ok=True)

    for i in range(10):  # Process folders from 0 to 9
        input_folder = os.path.join(input_base_folder, str(i))

        # Iterate over input files in the current folder
        for (root, dirs, files) in os.walk(input_folder, topdown=True):
            for input_filename in files:
                if input_filename.endswith('.fa'):
                    input_file_path = os.path.join(root, input_filename)

                    with open(input_file_path, 'r') as input_file:
                        lines = input_file.readlines()

                        # Check if there are at least 12 lines in the input file
                        if len(lines) >= 12:
                            # Create the output file names starting from 0
                            output_file_name_1 = f"pdb-{i}_1.fasta"
                            output_file_name_2 = f"pdb-{i}_2.fasta"
                            output_file_name_3 = f"pdb-{i}_3.fasta"
                            output_file_name_4 = f"pdb-{i}_4.fasta"
                            output_file_name_5 = f"pdb-{i}_5.fasta"
                            output_file_path_1 = os.path.join(output_folder, output_file_name_1)
                            output_file_path_2 = os.path.join(output_folder, output_file_name_2)
                            output_file_path_3 = os.path.join(output_folder, output_file_name_3)
                            output_file_path_4 = os.path.join(output_folder, output_file_name_4)
                            output_file_path_5 = os.path.join(output_folder, output_file_name_5)

                            # Write lines 4 and 6 to separate output files
                            with open(output_file_path_1, 'w') as output_file_1:
                                output_file_1.write("> pdb\n" + lines[3])
                            with open(output_file_path_2, 'w') as output_file_2:
                                output_file_2.write("> pdb\n" + lines[5])
                            with open(output_file_path_3, 'w') as output_file_3:
                                output_file_3.write("> pdb\n" + lines[7])
                            with open(output_file_path_4, 'w') as output_file_4:
                                output_file_4.write("> pdb\n" + lines[9])
                            with open(output_file_path_5, 'w') as output_file_5:
                                output_file_5.write("> pdb\n" + lines[11])
    print(f"Lines from rows 4, 6, 8, 10 and 12 in text files in folders '{input_base_folder}/0' to '{input_base_folder}/9' have been written to separate output files in '{output_folder}' starting from 0.")
except FileNotFoundError:
    print(f"Folder '{input_base_folder}' not found.")