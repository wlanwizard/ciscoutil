from netmiko import ConnectHandler
import getpass
import datetime

# Read from a list of hostnames to connect to
hosts = open('hosts.txt', 'r')
hosts = hosts.read()
hosts = hosts.strip().splitlines()

# Get UserName and password from input

userName = input('Username: ')
passWord = getpass.getpass()

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
    file = open(host + "_" + current_date_str + '_output.txt', 'w')


    # Execute commands
    output = net_connect.send_command('term len 0')
    output = net_connect.send_command('show run aaa')


    # Print output to console screen
    print(host)

    #print(output)
    #print()
    #print()

    # Write output to file above
    file.write(output)
    file.close()