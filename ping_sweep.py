from scapy.all import ICMP, IP, sr, TCP

# Specify the target hosts range
target_ip = "192.168.1.1/24"

# Send ICMP echo requests (ping) to the target hosts
answered, unanswered = sr(IP(dst=target_ip) / ICMP(), timeout=2, verbose=0)

print("The following hosts are alive:")
for response in answered:
    print(response[1].src)
