from scapy.all import ICMP, IP, sr1, TCP

# Specify the target hosts range
target_ip = "192.168.1.1/24"
# Send ICMP echo requests (ping) to the target hosts
alive, dead = sr1(IP(dst=target_ip) / ICMP(), timeout=2, verbose=0)
print("The following hosts are alive:")
for i in range(len(alive)):
    print(alive[i][1].src)
