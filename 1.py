import socket
s=socket.socket()
host=socket.gethostname()
host='172.16.127.41'
port=12345
s.connect((host,port))
print(s.recv(1024))
s.close