from scapy.all import ARP, Ether, srp

def scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients = []
    for sent, received in answered_list:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

def print_result(results_list):
    print("IP" + " "*18+"MAC")
    for client in results_list:
        print("{:20}{}".format(client['ip'], client['mac']))

# Replace '192.168.1.1/24' with the network you want to scan
network = '192.168.1.1/24'
print_result(scan(network))
