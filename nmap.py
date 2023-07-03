import nmap3

scan = nmap3.NmapScanTechniques()

target_ip = input("Enter the host IP: ")

port_range = input("Enter the range of ports to scan (for example, 1-5000): ")

result =  scan.nmap_tcp_scan(target_ip, args=f"-sV -p{port_range}")

for port in result[target_ip]['ports']:
    port_number = port['portid']
    protocol = port['protocol']
    state = port['state']
    service_name = port['service']['name']

    # Проверяем, существует ли ключ 'version' в словаре 'service'
    if 'version' in port['service']:
        service_version = port['service']['version']
    else:
        service_version = 'N/A'

    print(f"Port: {port_number}\tService: {service_name}\tProtocol: {protocol}\tState: {state}\tVersion: {service_version}")
