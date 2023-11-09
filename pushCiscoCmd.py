from netmiko import ConnectHandler
import argparse
import getpass

# Setting up the argument parser to read host list
parser = argparse.ArgumentParser(description='Apply commands to a list of hosts.')
parser.add_argument('hostfile', type=str, help='The file containing the list of host IPs.')
parser.add_argument('commandfile', type=str, help='The file containing the list of commands.')

# Parsing the arguments
args = parser.parse_args()

# Reading the host list from the file provided
with open(args.hostfile, 'r') as file:
    host_ips = file.read().splitlines()

# Reading the command list from the file provided
with open(args.commandfile, 'r') as file:
    commands = file.read().splitlines()

# Prompting for username and password
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# Function to log in and apply commands to a device
def apply_commands_to_device(device_ip, commands, username, password):
    device_info = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': username,
        'password': password
    }
    # Establishing a connection to the device
    with ConnectHandler(**device_info) as net_connect:
        # Sending configuration commands to the device
        output = net_connect.send_config_set(commands)
        print(output)  # Printing the output

# Applying the commands to each host IP
for host_ip in host_ips:
    apply_commands_to_device(host_ip, commands, username, password)
