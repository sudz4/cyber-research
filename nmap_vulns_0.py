import nmap

def scan_network(ip_range):
    nm = nmap.PortScanner()

    # Use '-O' for OS detection. Note: this requires root privileges
    nm.scan(hosts=ip_range, arguments='-O')

    for host in nm.all_hosts():
        print(f"Host : {host}")

        # Hostname
        if nm[host].hostname():
            print(f"Hostname : {nm[host].hostname()}")

        # Vendor information
        for mac in nm[host]['addresses']:
            if nm[host]['addresses'][mac] != host:
                print(f"MAC Address : {nm[host]['addresses'][mac]}")
                print(f"Vendor : {nm[host]['vendor'][nm[host]['addresses'][mac]] if nm[host]['addresses'][mac] in nm[host]['vendor'] else 'Unknown'}")

        # Operating System information
        if 'osmatch' in nm[host]:
            for osmatch in nm[host]['osmatch']:
                print(f"OS Match : {osmatch['name']}")
                print(f"OS Accuracy : {osmatch['accuracy']}")
                print('-------------')

if __name__ == "__main__":
    # replace with your actual IP range, e.g. '192.168.1.0/24'
    ip_range = '192.168.1.0/24'
    scan_network(ip_range)

