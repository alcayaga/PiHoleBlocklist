import dns.resolver
import time

def check_domains(filename):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']  # Google's public DNS server
    
    with open(filename, 'r') as file:
        domains = file.readlines()
    
    active_domains = []
    inactive_domains = []
    
    for domain in domains:
        domain = domain.strip()
        if domain.startswith('||'):
            domain = domain[2:].rstrip('^')
        try:
            answers = resolver.resolve(domain, 'A')  # 'A' record for IPv4 addresses
            active_domains.append(domain)
            print(f"Domain {domain} is active.")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            inactive_domains.append(domain)
            print(f"Domain {domain} is inactive.")
        
        time.sleep(1)
    
    return active_domains, inactive_domains

# Example usage
active, inactive = check_domains('Chile-Phishing.txt')
print("Active domains:", active)
print("Inactive domains:", inactive)
