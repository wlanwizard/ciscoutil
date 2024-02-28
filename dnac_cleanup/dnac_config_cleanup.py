import argparse
import re

def process_text(input_text):
    """
    Process the input text to:
    1. Remove starting patterns matching '^\s*\d+\s*\|' from lines.
    2. Remove lines containing "attach".
    3. Remove lines containing "dna".
    4. Remove blocks of text starting with a line containing "crypto" until a line containing "end".
    5. Remove blocks of text starting with "flow record " and ending with "!".
    """
    # Split the input into lines
    lines = input_text.split('\n')

    # Rule 1: Process for removing starting pattern
    lines = [re.sub(r'^\s*\d+\s*\|', '', line) for line in lines]

    processed_lines = []
    skip_block = False
    skip_block2 = False

    for line in lines:
        # Check for the start of a block to skip
        if "crypto" in line:
            skip_block = True
            continue

        # Check for the end of a block to skip
        if skip_block and (line.strip() == "!" in line):
            skip_block = False
            continue

        # Skip lines if in a block to skip
        if skip_block:
            continue

        # Check for the start of a block2 to skip
        if "telemetry" in line:
            skip_block2 = True
            continue

        # Check for the end of a block to skip
        if skip_block2 and (line.strip() == "!" in line):
            skip_block2 = False
            continue

        # Skip lines if in a block to skip
        if skip_block2:
            continue

        # Rule 2: Remove lines containing "attach"
        if "attach" in line:
            continue
        
        # Rule 3: Remove lines containing "errdisable"
        if "errdisable" in line:
            continue

        # Rule 4: Remove lines containing "snmp-server enable traps"
        if "snmp-server enable traps" in line:
            continue

        # Rule 5: Remove lines containing "flow monitor "
        if "flow monitor" in line:
            continue

        # Rule 6: Remove lines containing "snmp-server host"
        if "snmp-server host" in line:
            continue

        # Rule 7: Remove lines containing "device-tracking"
        if "device-tracking" in line:
            continue

        processed_lines.append(line)

    return '\n'.join(processed_lines)

def main():
    parser = argparse.ArgumentParser(description='Process a file according to specified rules.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file path')
    
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as infile:
        input_text = infile.read()

    processed_text = process_text(input_text)

    with open(args.output, 'w', encoding='utf-8') as outfile:
        outfile.write(processed_text)

    print("Processing completed. Check the output file for results.")

if __name__ == "__main__":
    main()
