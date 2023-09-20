import subprocess

def call_tcping(ip):
    command = f"tcping.exe -n 2 {ip} 22"
    subprocess.call(command, shell=True)

def main():
    network = input("Enter the network in CIDR notation (e.g. 192.168.0.0/24): ")
    ip, subnet = network.split("/")
    subnet_mask = 32 - int(subnet)
    base_ip_parts = list(map(int, ip.split(".")))
    
    for i in range(2 ** subnet_mask):
        ip_parts = base_ip_parts.copy()
        for j in range(4):
            ip_parts[j] += (i >> (3-j)) & 0x1
        
        call_tcping(".".join(map(str, ip_parts)))

if __name__ == "__main__":
    main()
