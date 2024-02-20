import re

# File paths
input_file_path = 'sw_config.txt'
output_file_path = 'output4.txt'

# Flags to track whether we're between "crypto" and "quit"
inside_crypto_block = False

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Iterate over each line in the input file
    for line in input_file:
        # Check if the line contains "crypto"
        if "crypto" in line:
            inside_crypto_block = True
            continue  # Skip adding the line to the output
        # Check if we are exiting a crypto block
        if "quit" in line:
            inside_crypto_block = False
            continue  # Skip adding the line to the output
        
        # If not inside a crypto block, process the line
        if not inside_crypto_block:
            # Use regular expression to remove all characters up to and including the first pipe on the line
            modified_line = re.sub(r'^.*?\|', '', line, 1)
            # Write the modified line to the output file
            output_file.write(modified_line)

print(f"Process completed. Check {output_file_path} for the result.")