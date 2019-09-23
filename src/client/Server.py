import socket
address = ("192.168.43.67", 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(1000)


client, addr = s.accept()
print 'got connected from', addr

filename = open('input.jpg', 'wb')
while True:
    strng = client.recv(1024)
    if not strng:
        break
    filename.write(strng)
filename.close()
print 'received, yay!'

client.close()
