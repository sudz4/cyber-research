import socket
import ipaddress

def get_network_range():
    # Get the hostname
    hostname = socket.gethostname()

    # Get the IP
    ip_address = socket.gethostbyname(hostname)

    # Get subnet mask
    subnet_mask = socket.inet_ntoa(socket.inet_aton('255.255.255.0'))  # replace this with your actual subnet mask

    # Calculate network range
    ip_interface = ipaddress.ip_interface(f'{ip_address}/{subnet_mask}')
    network = ip_interface.network

    return str(network.network_address), str(network.broadcast_address)


if __name__ == "__main__":
    network_start, network_end = get_network_range()
    print(f"Network range is: {network_start} - {network_end}")

