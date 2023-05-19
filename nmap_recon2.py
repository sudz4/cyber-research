import nmap
import pandas as pd

def scan_network(segment):
    nm = nmap.PortScanner()
    res = nm.scan(hosts=segment, arguments='-sS -O -sV') # DONT use -sn here because it blocks port scans and will throw an ERROR

    host_data = []

    for host in res['scan'].keys():
        if res['scan'][host]['status']['state'] == 'up':
            data = {
                'Host': host,
                'Hostname': res['scan'][host]['hostnames'][0]['name'],
                'OS': ' '.join(map(str, res['scan'][host].get('osmatch', []))),
                'TCP Ports': ', '.join([str(port) for port in res['scan'][host].get('tcp', [])]),
            }
            host_data.append(data)

    return host_data

web_services_segment = '172.16.10.0/24'
business_services_segment = '172.16.1.0/24'

web_services_data = scan_network(web_services_segment)
business_services_data = scan_network(business_services_segment)

web_services_df = pd.DataFrame(web_services_data)
business_services_df = pd.DataFrame(business_services_data)

print(web_services_df)
print(business_services_df)
