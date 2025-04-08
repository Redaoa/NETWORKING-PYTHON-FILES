port_number = int(input("Enter the port number: "))
if port_number < 1024 :
    print("Port number is less than 1024")
else:
    print("Port number is greater than 1024")