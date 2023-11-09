import os
import shutil

apd=""

# Specify the source folder where the files are located
source_folder = os.path.join(apd, "1-rfdiffusion")  # Replace with your source folder path

# List all files in the source folder
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Iterate over each file and copy it to a new folder with the same name
for file in files:
    # Create a new folder with the same name as the file (without extension)
    file_name, file_extension = os.path.splitext(file)
    new_folder_path = os.path.join(source_folder, file_name)

    # Ensure the new folder exists or create it
    os.makedirs(new_folder_path, exist_ok=True)

    # Copy the file to the new folder
    source_file_path = os.path.join(source_folder, file)
    destination_file_path = os.path.join(new_folder_path, file)
    shutil.copy(source_file_path, destination_file_path)

