import socket

def brute_force_subdomains(domain, subdomains):
    found_subdomains = []

    for subdomain in subdomains:
        try:
            full_domain = f"{subdomain}.{domain}"
            ip = socket.gethostbyname(full_domain)
            found_subdomains.append((full_domain, ip))
            print(f"Found: {full_domain} -> {ip}")
        except socket.gaierror:
            pass  # Ignore subdomains that can't be resolved

    return found_subdomains

if __name__ == "__main__":
    domain = "example.com"
    subdomains = [
        "www", "mail", "ftp", "test", "dev", "staging", "blog", "shop"
    ]

    found = brute_force_subdomains(domain, subdomains)
    print("\nSummary of found subdomains:")
    for subdomain, ip in found:
        print(f"{subdomain} -> {ip}")