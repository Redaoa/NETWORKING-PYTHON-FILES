ports_numbers = {'http':80, 'https':443, 'ftp':21, 'smtp':25, 'dns':53} 
for port in ports_numbers:
    if ports_numbers[port] <= 65535:
        print (f'the port {port} is valid')
    else:
        print (f'the port {port} is not valid')