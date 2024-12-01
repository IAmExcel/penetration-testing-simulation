import os
import nmap_scan

def generate_report(target, results):
    """Save the scan results to a file."""
    report_path = f"report/{target}_nmap_report.txt"
    with open(report_path, "w") as file:
        file.write(f"Penetration Testing Report for {target}\n")
        file.write("=" * 40 + "\n")
        for port, service in results.items():
            file.write(f"Port {port}: {service}\n")
    print(f"Report saved to {report_path}")

def main():
    print("Penetration Testing Simulation")
    
    # Create a folder for reports if it doesn't exist
    if not os.path.exists("report"):
        os.makedirs("report")
    
    # Get the target host from the user
    target = input("Enter the target host (IP or hostname): ")
    
    # Perform the scan
    results = nmap_scan.scan_network(target)
    
    if results:
        print("\nOpen Ports Found:")
        for port, service in results.items():
            print(f"Port {port}: {service}")
        
        # Generate the report
        generate_report(target, results)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
