from Tkinter import *
import tkFont
import PIL
from PIL import Image
import ttk
import socket




class ATT_LIST:
    def __init__(self,win,email):
        masterr=win
        masterr.title("STUDENT LIST")
        masterr.configure(height=650,width=900,bg="#990066")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)
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
        self.new2(masterr,email)
        self.help=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.help,label="help")
        self.help.add_command(label="About Us")
        masterr.mainloop()
    def new2(self,caller,email):
        course_name1=StringVar();
        sem_name1=StringVar();
        stream_name1=StringVar();
        def save2():
            course__name1=course_name1.get()
            sem__no1=sem_name1.get()
            stream_no1=stream_name1.get()
            if(course__name1!="" and sem__no1!="" and stream_no1!=""):
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = "192.168.43.67"
                port = 5000
                server.connect( (host, port) )
                name="Status"+"/"+str(course__name1)+"/"+str(sem__no1)+"/"+str(stream_no1)
                name=name.encode("utf-8")
                server.send(name)

                s_data=server.recv(2048)
                s_data=s_data.decode("utf-8")
                



                
                server.close()
                
            else:
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," (*) Feild Required")

                
        f=tkFont.Font(size=15,weight="bold",family="Helvetica")

        frm1=Frame(caller,height=630,width=200,bg="#990066")
        frm1.grid(row=1,column=1,padx=10,pady=58,sticky= N)

        frm2=Frame(caller,height=630,width=660,bg="#990066")
        frm2.grid(row=1,column=2,padx=10,sticky= W+N+S+E)


        
        course=Label(frm1,text="Courses(*)",fg="gray",bg="#990066",font=f)
        course.grid(row=1,column=1,sticky=W,padx=2,pady=2)
        courses = ttk.Combobox(frm1,state="readonly",textvariable=course_name1,
        values = ('BTech', 'MTech'))
        courses.grid(row=2,column=1,sticky=W,padx=2,pady=2)
        lblsem=Label(frm1,text="Semester(*)",fg="gray",bg="#990066",font=f)
        lblsem.grid(row=3,column=1,sticky=W,padx=2,pady=2)
        sem= ttk.Combobox(frm1,state="readonly",textvariable=sem_name1,
        values = ('SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4','SEMESTER 5','SEMESTER 6','SEMESTER 7','SEMESTER 8'))
        sem.grid(row=4,column=1,sticky=W,padx=2,pady=2)
        stream=Label(frm1,text="Stream(*)",fg="gray",bg="#990066",font=f)
        stream.grid(row=5,column=1,sticky=W,padx=2,pady=2)
        sub = ttk.Combobox(frm1,state="readonly",textvariable=stream_name1,
        values = ('CS','CIVIL', 'IT', 'ECE','EIC','EE', 'ME'))
        sub.grid(row=6,column=1,sticky=W,padx=2,pady=2)
        submit=Button(frm1,width=10,text="View Status",bg="gray",fg="#990066",command=save2)
        submit.grid(row=7,column=1,sticky=W,padx=30,pady=20)

        frm4=Frame(frm2,width=660,bg="#990066")
        frm4.grid(row=1,column=1,sticky= W+N+S+E)

        id_lbl=Label(frm4,text="Name",width=15,fg="gray",bg="#990066")
        id_lbl.grid(row=1,column=1,sticky=W,padx=10)

        n_lbl=Label(frm4,text="College ID",width=15,fg="gray",bg="#990066")
        n_lbl.grid(row=1,column=2,sticky=W,padx=10)

        mark_lbl=Label(frm4,text="Enrollment ID",width=15,fg="gray",bg="#990066")
        mark_lbl.grid(row=1,column=3,sticky=W,padx=10)


        details=Label(frm4,text="Details",width=15,fg="gray",bg="#990066")
        details.grid(row=1,column=5,sticky=W,padx=10)


        
