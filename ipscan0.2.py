import re
import requests
import csv

def extract_ips(text):
    # Regular expression to find IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(ip_pattern, text)

def aggregate_ips(ip_list):
    ip_counts = {}
    for ip in ip_list:
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
    return ip_counts

def is_local_ip(ip):
    # Check if IP is in local range
    parts = ip.split('.')
    if parts[0] == '10':
        return True
    elif parts[0] == '192' and parts[1] == '168':
        return True
    elif parts[0] == '172' and 16 <= int(parts[1]) <= 31:
        return True
    elif parts[0] == '127':
        return True
    elif parts[0] == '169' and parts[1] == '254':
        return True
    return False

def get_ip_ownership(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('org', 'Organization information not available')
    else:
        return f"Failed to fetch data for IP: {ip}"

def main():
    file_path = 'sample.txt'  # Update this with your file path
    output_file = 'ipscan.csv'
    
    with open(file_path, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
    
    ip_list = extract_ips(content)
    aggregated_ips = aggregate_ips(ip_list)
    
    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(["IP Address", "Times Seen", "Ownership"])
        for ip, count in aggregated_ips.items():
            if not is_local_ip(ip):
                ownership = get_ip_ownership(ip)
                writer.writerow([ip, count, ownership])
                print(f"IP Address: {ip}, Times Seen: {count}, Ownership: {ownership}")

if __name__ == "__main__":
    main()
