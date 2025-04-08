import socket
import thread

BUFF = 1024 # buffer size
HOST = '127.0.0.1'
PORT = 1234 # Port number for client & server to recieve data
def response(key):
    return 'Sent by client'


def logger(string, file_=open('logfile.txt', 'a'), lock=thread.allocate_lock()):
    with lock:
        file_.write(string)
        file_.flush() # optional, makes data show up in the logfile more quickly, but is slower


def handler(clientsock, addr):
    while 1:
        data = clientsock.recv(BUFF) # receive data(buffer).
        logger('data:' + repr(data) + '\n') #Server to recieve data sent by client.
        if not data:
            break           #If connection is closed by client, server will break and stop recieving data.
        logger('sent:' + repr(response('')) + '\n') # respond by saying "Sent By Client".
if __name__=='__main__':
    ADDR = (HOST, PORT) #Define Addr
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind(ADDR) #Binds the ServerSocket to a specific address (IP address and port number)
    serversock.listen(0)
    while True:
        logger('waiting for connection...\n')
        clientsock, addr = serversock.accept()
        logger('...connected from: ' + str(addr) + '\n') #show its connected to which addr
        thread.start_new_thread(handler, (clientsock, addr))