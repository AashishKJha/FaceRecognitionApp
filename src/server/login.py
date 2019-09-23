import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
class Login:
    def __init__(self,mwindow):
        global masterr
        masterr =Toplevel(mwindow)   
        
        masterr.title("STUDENT LOGIN")
        masterr.configure(height=650,width=900,bg="#FF33FF")
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
        self.new(masterr)
        self.help=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.help,label="help")
        self.help.add_command(label="About Us")
        
        masterr.mainloop()
    def new(self,caller):
        
        listvar=StringVar()
        

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm1=Frame(masterr,height=650,width=900,bg="#FF33FF")
        frm1.grid(row=1,column=1,sticky= N+W+E+S,padx=350,pady=200)
        lblid=Label(frm1,text="Enrollment ID",fg="blue",bg="#FF33FF",anchor=CENTER,font=f)
        lblid.grid(row=1,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entid=Entry(frm1,width=35)
        Entid.grid(row=2,column=1,padx=2,pady=2,sticky= N+W+E+S)
        lblpass=Label(frm1,text="Password",fg="blue",bg="#FF33FF",font=f)
        lblpass.grid(row=3,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entpass=Entry(frm1,width=35)
        Entpass.grid(row=4,column=1,padx=2,pady=2,sticky= N+W+E+S)
        submit=Button(frm1,width=15,text="Submit Details",bg="blue",fg="white")
        submit.grid(row=5,column=1,padx=2,pady=20)
        forget=Button(frm1,width=20,text="Forgot Password",bg="blue",fg="white")
        forget.grid(row=6,column=1,sticky=N+W+E+S,padx=2,pady=20)
        
        
        
        
