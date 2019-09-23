import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
import socket

class inputdata:
    def __init__(self,win,cid):
        self.win=win
        self.cid=cid
        self.new1()
    def new1(self):
        c_id=self.cid
    
        if(c_id==""):
            import tkMessageBox
            tkMessageBox.showwarning("Warning"," (*) Feild Required")
        elif(len(str(c_id))!=6):
            import tkMessageBox
            tkMessageBox.showwarning("Warning","Not College Id")
        else:
            
            self.win.state(newstate="iconic")
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = "192.168.43.67"
            port = 5000
            server.connect( (host, port) )
            name=str("Profile")+"/"+str(c_id)
            print(name)

            client_data = name.encode("utf-8")
            print(client_data)
            ##Send Data To Server in String Formet

            server.send(client_data)

            server_data = server.recv(2048)
            data=server_data.decode("utf-8")
            if(data==""):
                import tkMessageBox
                tkMessageBox.showwarning("Warning","No Data Received From Server")
            else:
                data=data.split("/")
                print(data)
                f=open("Photo/Spic/"+data[2]+".jpg" , 'wb')
                while True:
                    data1=server.recv(1024)
                    print("ok")
                    if not data1:
                        print("Null")
                        break
                    f.write(data1)
                f.close()
            server.close()
            from details import Detailsstudent
            Detailsstudent(self.win,data)

