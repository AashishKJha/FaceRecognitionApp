import socket
class Myclient:
    def __init__(self,email,pwd,caller):
        self.email=email
        self.caller=caller
        self.pwd=pwd
        self.server()
        
    def server(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = "192.168.43.67"
            port = 5000
            server.connect( (host, port) )
            name=str("Login")+"/"+str(self.email)+"/"+str(self.pwd)

            client_data = name.encode("utf-8")
            ##Send Data To Server in String Formet

            server.send(client_data)

            server_data = server.recv(128)

            ##Receive Data From Server as String

            server_data_s = server_data.decode("utf-8")
            
            if(int(server_data_s)==1):
                
                from main import mainwindow
                mainwindow(self.caller,self.email)
            else:
                import tkMessageBox
                tkMessageBox.showwarning("Warning","Incorrect Email or Password")
            server.close()
            
        except Exception as e:
            import tkMessageBox
            tkMessageBox.showwarning("Warning",str(type(e)))




