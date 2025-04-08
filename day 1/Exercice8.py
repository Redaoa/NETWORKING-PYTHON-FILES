import ipaddress
addr = ipaddress.ip_address('::abc:7:def')
extended = addr.exploded
compressed = addr.compressed
print(f'Extended: {extended}')
print(f'Compressed: {compressed}')