import argparse
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
from getpass import getpass

# Function to read IP addresses from a file
def read_ip_addresses(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Set up argument parser
parser = argparse.ArgumentParser(description='SSH into Cisco devices using IP addresses from a file.')
parser.add_argument('file_path', help='Path to the file containing IP addresses')
args = parser.parse_args()

# Reading IP addresses
ip_addresses = read_ip_addresses(args.file_path)

# User credentials
username = input("Enter your SSH username: ")
password = getpass("Enter your SSH password: ")

# File to log failed connections
failed_logins_file = 'failed_logins.txt'

# Looping through each IP address
for ip in ip_addresses:
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
    }

    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('show version')  # Example command
        print(f"--- Login Success to {ip} ---")
        #print(output)
        net_connect.disconnect()
    except (NetmikoAuthenticationException, NetmikoTimeoutException) as e:
        print(f"Failed to connect to {ip}: {e}")
        with open(failed_logins_file, 'a') as file:
            file.write(f"{ip}\n")

print(f"Failed logins have been recorded in {failed_logins_file}.")