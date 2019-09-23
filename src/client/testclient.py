import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object # Get local machine name
 # Reserve a port for your service.
host = "192.168.43.67"
port = 5000
s.connect((host, port))
print (s.recv(1024))
s.close
