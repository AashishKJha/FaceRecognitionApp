import socket
class STcredit:
    def __init__(self,course,sem,stream,caller,email):
        self.course=course
        self.sem=sem
        self.stream=stream
        self.caller=caller
        self.email=email
        self.server_send()
        
    def server_send(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = "192.168.43.67"
            port = 5000
            server.connect( (host, port) )
            name=str("LoginSuccessful")+"/"+str(self.course)+"/"+str(self.sem)+"/"+str(self.stream)

            client_data = name.encode("utf-8")

            server.send(client_data)

            server_data = server.recv(128)

            server_data_s = server_data.decode("utf-8")
            if(int(server_data_s)==1):
                server.close()              
                from pccap import UpperBody
                UpperBody(self.course,self.sem,self.stream,self.caller,self.email)
            else:
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," Data Not Exist")
            
            
        except Exception as e:
            import tkMessageBox
            tkMessageBox.showwarning("Warning",str(e))
