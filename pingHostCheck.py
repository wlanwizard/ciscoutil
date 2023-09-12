import ping3

# Read the IP addresses from the file
with open('hosts.txt', 'r') as file:
    ip_addresses = file.read().splitlines()

# Ping each IP address and write the results to the output file
with open('ping_results.txt', 'w') as output_file:
    for ip in ip_addresses:
        result = ping3.ping(ip)
        if result is not None:
            output_file.write(f'{ip}: Ping successful\n')
            print(f'{ip}: Ping successful')
        else:
            output_file.write(f'{ip}: Ping failed\n')
            print(f'{ip}: Ping failed')
