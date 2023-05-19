import nmap
import pandas as pd
#ddd
def scan_network(segment):
    nm = nmap.PortScanner()
    res = nm.scan(hosts=segment, arguments='-sS -O -sV')

    host_data = []

    for host in res['scan'].keys():
        if res['scan'][host]['status']['state'] == 'up':
            data = {
                'Host': host,
                'Hostname': res['scan'][host]['hostnames'][0]['name'],
                'OS': ' '.join(map(str, res['scan'][host].get('osmatch', []))),
                'TCP Ports': ', '.join([str(port) for port in res['scan'][host].get('tcp', [])]),
                'MAC Address': res['scan'][host]['addresses'].get('mac', 'N/A')
            }
            host_data.append(data)

    return host_data

web_services_segment = '172.16.10.0/24'
business_services_segment = '172.16.1.0/24'

web_services_data = scan_network(web_services_segment)
business_services_data = scan_network(business_services_segment)

web_services_df = pd.DataFrame(web_services_data)
business_services_df = pd.DataFrame(business_services_data)

# Now, we create an ExcelWriter object and write the dataframes to excel sheets
with pd.ExcelWriter('network_inventory_44.xlsx', engine='xlsxwriter') as writer:
    web_services_df.to_excel(writer, sheet_name='Web Services', index=False)
    business_services_df.to_excel(writer, sheet_name='Business Services', index=False)
