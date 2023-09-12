from netmiko import ConnectHandler
import getpass
import datetime
import os

# Read from a list of hostnames to connect to
hosts = open('hosts.txt', 'r')
hosts = hosts.read()
hosts = hosts.strip().splitlines()

# Get UserName and password from input

userName = input('Username: ')
passWord = getpass.getpass()

current_date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder_name = current_date_str + "_output"
os.makedirs(folder_name)  # Create a new directory with the folder name

# Loop to process hosts in hosts.txt file
for host in hosts:
    # Define device type and connection attributes
    devices = {
        'device_type': 'cisco_ios',
        'ip': host,
        'username': userName,
        'password': passWord
    }

    # Netmiko SSH Connection Handler
    net_connect = ConnectHandler(**devices)

    #open file to write command output
    # Get the current date and time
    current_date = datetime.datetime.now()

    # Convert the current date to a string
    current_date_str = str(current_date)
    current_date_str = current_date_str.replace(" ", "")
    current_date_str = current_date_str.replace("/", "-")
    current_date_str = current_date_str.replace(":", "-") 

    #current_date = datetime.datetime.now().strftime("_%Y-%m-%d_%H:%M:%S")
    #file = open(host + "_" + current_date_str + '_output.txt', 'w')

    

    file_path = os.path.join(folder_name, host + "_output.txt")
    file = open(file_path, 'w')


    # Execute commands
    output = net_connect.send_command('term len 0')
    output_1 = net_connect.send_command('show run aaa')
    output_2 = net_connect.send_command('show ver')
    output_final = output_1 + output_2


    # Print output to console screen
    print(host)

    #print(output)
    #print()
    #print()

    # Write output to file above
    file.write(output_final)
    file.close()