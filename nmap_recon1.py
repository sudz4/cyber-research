import nmap
import pandas as pd

def scan_network(segment): #scans the network segment(s)
    nm = nmap.PortScanner()
    res = nm.scan(hosts=segment, arguments='-sn')

    host_list = []

    for host in res['scan'].keys():
        if res['scan'][host]['status']['state'] == 'up':
            host_list.append(host)

    return host_list

web_services_segment = '172.16.10.0/24'
business_services_segment = '172.16.1.0/24'

web_services_hosts = scan_network(web_services_segment) #segment 1
business_services_hosts = scan_network(business_services_segment) #segment 2

web_services_df = pd.DataFrame(web_services_hosts, columns=["Web Services"])
business_services_df = pd.DataFrame(business_services_hosts, columns=["Business Services"])

print(web_services_df)
print(business_services_df)
