import nmap
import pandas as pd

def scan_network(segment):
    nm = nmap.PortScanner()
    res = nm.scan(hosts=segment, arguments='-sS -O -sV')

    host_data = []

    for host in res['scan'].keys():
        if res['scan'][host]['status']['state'] == 'up':
            osmatch = res['scan'][host].get('osmatch', [])
            os_name = osmatch[0]['name'] if osmatch else ''

            data = {
                'Host': host,
                'Hostname': res['scan'][host]['hostnames'][0]['name'],
                'OS': os_name,
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
with pd.ExcelWriter('var_network_inventory.xlsx', engine='xlsxwriter') as writer:
    web_services_df.to_excel(writer, sheet_name='Web Services', index=False)
    business_services_df.to_excel(writer, sheet_name='Business Services', index=False)

# Print DataFrames to terminal
print("Web Services DataFrame:")
print(web_services_df)

print("Business Services DataFrame:")
print(business_services_df)
