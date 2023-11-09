import os
import fileinput

# Define the parent directory where you want to search for Python and Bash scripts
parent_directory = os.path.abspath(os.curdir)

# Define the variable name you want to change
variable_name = "apd"

# Get the new value for the variable from the user
new_value = f'"{parent_directory}"'

# Function to search and replace a variable in Python and Bash scripts
def replace_variable(file_path, variable_name, new_value):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            if line.strip().startswith(f"{variable_name}="):
                print(f"{variable_name}={new_value}", end="\n")
            else:
                print(line, end="")

# Iterate over all subdirectories in the parent directory
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        if file.endswith('.py') or file.endswith('.sh'):
            file_path = os.path.join(root, file)
            replace_variable(file_path, variable_name, new_value)

print(f"Variable '{variable_name}' updated in all Python and Bash scripts.")

