import subprocess
import ipaddress

def call_tcping(ip):
    command = f"tcping.exe -n 2 {ip} 22"
    subprocess.call(command, shell=True)



# def main():
#     network = input("Enter the network in CIDR notation (e.g. 192.168.0.0/24): ")
#     ip, subnet = network.split("/")
#     subnet_mask = 32 - int(subnet)
#     base_ip_parts = list(map(int, ip.split(".")))
    
#     for i in range(2 ** subnet_mask):
#         ip_parts = base_ip_parts.copy()
#         for j in range(4):
#             ip_parts[j] += (i >> (3-j)) & 0x1
        
#         call_tcping(".".join(map(str, ip_parts)))


def get_usable_ip_addresses(network):
    # Create an IPv4Network object from the CIDR notation
    subnet = ipaddress.IPv4Network(network)

    # Get the list of all usable IP addresses in the subnet
    usable_ips = [str(ip) for ip in subnet.hosts()]

    # Print out each usable IP address
    for ip in usable_ips:
        #print(ip)
        call_tcping(ip)

# Test the function
get_usable_ip_addresses("192.168.0.0/24")


# if __name__ == "__main__":
#     main()
