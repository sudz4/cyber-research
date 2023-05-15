import nmap
import pandas as pd

def scan_network(subnet):
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn -Pn')
    host_list = [item for item in nm.all_hosts() if nm[item].state() == 'up']
    os_list = []
    for host in host_list:
        try:
            nm.scan(host, arguments='-O')
            if 'osmatch' in nm[host] and nm[host]['osmatch']:
                os_list.append(nm[host]['osmatch'][0]['name'])
            else:
                os_list.append('Unknown')
        except KeyError:
            os_list.append('Scan failed')
    return host_list, os_list


# List of subnets to scan
subnets = ['172.16.10.0/24', '172.16.1.0/24']

# Create an empty DataFrame
df = pd.DataFrame()

# Scan each subnet and store the results in the DataFrame
for subnet in subnets:
    live_hosts, os_list = scan_network(subnet)
    df_temp = pd.DataFrame({subnet: live_hosts, subnet+'_OS': os_list})
    df = pd.concat([df, df_temp], axis=1)

print(df)
