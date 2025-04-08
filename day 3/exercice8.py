import telnetlib3 as Telnet
def test_telnet(host, port=23, timeout=10):
    try:
        connection = Telnet.Telnet(host, port, timeout)
        print('telnet is available on port 23 ')
        connection.close()
    except Exception as e:
        print('telnet is not available on port 23')
        print(e)
test_telnet('192.168.0.100') # change this to your host