import dns.resolver

def get_name_servers(domain):
    try:
        # Query for NS records
        answers = dns.resolver.resolve(domain, 'NS')
        print(f"Name servers for {domain}:")
        for server in answers:
            print(server.to_text())
    except Exception as e:
        print(f"Error: {e}")

# Replace 'example.com' with the domain you want to check
domain = 'example.com'
get_name_servers(domain)