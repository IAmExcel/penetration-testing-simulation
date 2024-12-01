import nmap

def scan_network(target, ports="1-1024"):
    """
    Perform an Nmap scan on the specified target.
    Args:
        target (str): The IP or hostname to scan.
        ports (str): The range of ports to scan (default: "1-1024").
    Returns:
        dict: A dictionary of open ports and their services.
    """
    nm = nmap.PortScanner()
    print(f"Scanning {target} for open ports...")
    nm.scan(hosts=target, ports=ports, arguments="-sV")
    
    results = {}
    for host in nm.all_hosts():
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                state = nm[host]['tcp'][port]['state']
                service = nm[host]['tcp'][port].get('name', 'unknown')
                if state == "open":
                    results[port] = service
    return results
