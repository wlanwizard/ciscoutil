import argparse
from netmiko import ConnectHandler
from getpass import getpass
import csv

# Assuming the CSV file has columns: device, mac_address, ip_address
csv_file = 'ip_reservations.csv'  # Replace with the path to your CSV file


# Run the script from the command line, providing the device's IP or hostname, the MAC address,
# and the IP address for the reservation. For example:
# python script.py 192.168.1.1 00:1A:2B:3C:4D:5E 192.168.1.100
# You will be prompted to enter the SSH username and password for the Cisco device.
    
    
def format_mac(mac_address):
    """
    Format the MAC address by removing colons and prepending '01'.
    """
    return '01' + mac_address.replace(':', '.')

def push_dhcp_reservation(device, username, password, mac_address, ip_address):
    """
    Push DHCP reservation configuration to a Cisco IOS device.
    """
    # Format MAC address
    formatted_mac = format_mac(mac_address)

    # Define device connection parameters
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': "10.21.0.1",
        'username': username,
        'password': password,
    }

    # DHCP reservation command
    command = f"ip dhcp pool {device}\n" \
              f"host {ip_address} 255.255.255.0\n" \
              f"client-identifier {convert_mac_format(mac_address)}\n"
    print(command)
    try:
        # Establishing connection to the device
        with ConnectHandler(**cisco_device) as net_connect:
            output = net_connect.send_config_set(command)
            print(output)
            print("DHCP reservation configured successfully.")
    except Exception as e:
        print(f"")
        
# Establish a connection to the device
    # with ConnectHandler(**cisco_device) as net_connect:
    #     # Send the command
    #     output = net_connect.send_config_set(command)

    #     # Check if the specific message is in the command output
    #     if "% A binding for this client already exists." in output:
    #         print("Reservation exists")
    #     else:
    #         # Handle other outputs or show the command output
    #         print(output)

def convert_mac_format(mac_str):
    """
    Convert MAC address format from 2222.3333.4444 to 0122.2233.3344.44
    """
    # Prepend '01' to the string
    mac_str = mac_str.replace(".", "")
    mac_str = mac_str.replace(":", "")
    new_str = '01' + mac_str

    # Insert a dot after every fourth character
    formatted_str = '.'.join(new_str[i:i+4] for i in range(0, len(new_str), 4))

    return formatted_str

def main():
    password = getpass("Enter your SSH password: ")
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            device = row[0]
            mac_address = row[1]
            ip_address = row[2]

            # Use the variables as needed for further processing
            # For example, you can pass them to a function or perform operations with them

            # Get username and password
            #username = input("Enter your SSH username: ")
            

            # Push DHCP reservation configuration
            push_dhcp_reservation(device, "admin", password, mac_address, ip_address )

if __name__ == "__main__":
    main()
