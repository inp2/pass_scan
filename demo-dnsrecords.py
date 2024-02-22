import dns.resolver
import nmap
import sys

def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain: 
    :return: 
    """
    ids = [
        'NONE',
        'A',
        'NS',
        'CNAME',
        'SOA',
        'MX',
        'TXT',
        'AAAA',
        'SRV',
        'CERT'
    ]

    ip_list = []
    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                if a == 'A':
                    ip_list.append(rdata.to_text())
                #print(a, ':', rdata.to_text()) 
        except Exception as e:
            print(e)  # or pass
    print(ip_list)
    nm = nmap.PortScanner()
    for ip in ip_list:
        nm.scan(ip, '22-443')
        print(nm.csv())

if __name__ == '__main__':
    arg = sys.argv[1]
    get_records(arg)
