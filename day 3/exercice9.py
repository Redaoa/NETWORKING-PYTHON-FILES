import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']
domain = "google.com"
response = resolver.resolve(domain, "A")
for i in response:
    print(i)