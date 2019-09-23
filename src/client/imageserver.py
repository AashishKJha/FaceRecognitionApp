import socket
import sys
import os

class iserver:
    def __init__(self,course,stream,sem,email,caller):
        self.course=course
        self.sem=sem
        self.stream=stream
        self.new(self.course,self.sem,self.stream,email,caller)
    def new(self,course,stream,sem,email,caller):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = "192.168.43.67"
        port = 5000
        s.connect( (host, port) )
        print(course)
        print(stream)
        print(sem)
        flag=0
        name="Image/0"
        client_data=name.encode("utf-8")
        s.send(client_data)
        server_data = s.recv(128)
        server_data_s = server_data.decode("utf-8")
        if(int(server_data_s)==1):
            sb="input.jpg"
            f=open(sb, "rb")
            while True:
                if(s.send(f.read(512))):
                    flag=1
                else:
                    break
            f.close()
            s.close()
##        new_name="Please/0"
##        client_data=new_name.encode("utf-8")
##        if(s.send(client_data)):
##            client_d=s.recv(1024)
##            x=client_d.decode("utf-8")
##            print(x)
            from Soc import Sock
            Sock(caller,course,stream,sem)
        
            
            
          
            
            
            
        
