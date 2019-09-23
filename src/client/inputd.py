import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
import socket

class inputdata:
    def __init__(self,win):
        masterr=Toplevel(win)
        masterr.title("STUDENT Profile")
        masterr.configure(height=350,width=450,bg="#990066")
        masterr.minsize(height=350,width=450)
        masterr.maxsize(height=350,width=450)
        self.menu=Menu(masterr)
        masterr['menu']=self.menu
        self.menu1=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.menu1,label="Admin")
        self.menu1.add_command(label="System Guide")
        self.menu1.add_command(label="System Close")
        self.menu1.add_command(label="Change Password")
        self.menu.add_command(label="System Guide")
        self.menu.add_command(label="System Close")
        self.menu.add_command(label="Change Password")
        self.new1(masterr)
        self.help=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.help,label="help")
        self.help.add_command(label="About Us")
        masterr.mainloop()
        
    def new1(self,caller):
        cid=StringVar();
        def save1():
            c_id=cid.get()
            if(c_id==""):
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," (*) Feild Required")
            elif(len(str(c_id))!=6):
                import tkMessageBox
                tkMessageBox.showwarning("Warning","Not College Id")
            else:
                
                caller.state(newstate="iconic")
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = "192.168.43.67"
                port = 5000
                server.connect( (host, port) )
                name=str("Profile")+"/"+str(c_id)

                client_data = name.encode("utf-8")
                ##Send Data To Server in String Formet

                server.send(client_data)

                server_data = server.recv(2048)
                data=server_data.decode("utf-8")
                if(data==""):
                    import tkMessageBox
                    tkMessageBox.showwarning("Warning","No Data Received From Server")
                else:
                    data=data.split("/")
                    f=open("Photo/Spic/"+data[2]+".jpg" , 'wb')
                    while True:
                        data1=server.recv(1024)
                        if not data1:
                            break
                        f.write(data1)
                    f.close()
                server.close()
                from details import Detailsstudent
                Detailsstudent(caller,data)
                    
                    
                    
                
                

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm1=Frame(caller,height=350,width=450,bg="#990066")
        frm1.grid(row=1,column=1,padx=160,pady=100,sticky= N+W+E+S)
        lblid=Label(frm1,text="Enter Collge ID",fg="gray",bg="#990066",font=f)
        lblid.grid(row=1,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entid=Entry(frm1,width=35,textvariable=cid)
        Entid.grid(row=2,column=1,padx=2,pady=2,sticky= N+W+E+S)
        
        submit=Button(frm1,width=3,text="Save Details",bg="gray",fg="#990066",command=save1)
        submit.grid(row=5,column=1,padx=30,pady=20,sticky= N+W+E+S)
