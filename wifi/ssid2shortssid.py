import argparse
import binascii

def calculate_crc32(input_data):
    # Ensure the input is bytes
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif isinstance(input_data, int):
        input_data = input_data.to_bytes((input_data.bit_length() + 7) // 8, 'big')
    
    # Calculate CRC32 using binascii
    crc_value = binascii.crc32(input_data) & 0xffffffff
    return crc_value

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Calculate CRC-32 of input data.')
    
    # Add an argument to the parser
    parser.add_argument('data', type=str, help='Input data for CRC-32 calculation')
    
    # Parse the command line arguments
    args = parser.parse_args()
    
    # Calculate CRC32 of the provided data
    crc32_value = calculate_crc32(args.data)
    
    # Print the result
    print(f"CRC-32: {crc32_value:08x}")

if __name__ == '__main__':
    main()
