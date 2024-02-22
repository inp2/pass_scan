import nmap

nm = nmap.PortScanner()

results = nm.nmap_dns_brute_script("example.com")

print(results)
