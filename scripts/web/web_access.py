import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a doorway, not connected yet to any server
mysock.connect(('data.pr4e.org', 80)) #dpecifying host name #finds the server, connects tp port 80. could fail if server doesn't exist
#rule - client sends first, server receives first

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #specifying document #prepare for sending
mysock.send(cmd) #sending

while True:
    data = mysock.recv(512)
    if (len(data)) < 1:
        break
    print(data.decode()) #decodes the data till it doesn't reach end
mysock.close() #closes all resources used for connection

