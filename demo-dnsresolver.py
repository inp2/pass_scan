import sys
import dns.resolver

# Domain Name
arg = sys.argv[1]

def resolve(domain):
  resolveList = []
  resol = dns.resolver.Resolver() #create a new instance named Resolver
  answer = resol.query(domain,"A")
  y=0
  for rData in answer: 
    resolveList.append(rData)
    ++y        
  return resolveList

domainName = arg
queryResult = resolve(domainName)

for result in queryResult:
    print(queryResult[0])
    answers = dns.resolver.resolve(arg, "MX")
