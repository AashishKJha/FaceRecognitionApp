import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
class Login:
    def __init__(self):
        masterr=Tk()
        masterr.title("FACULTY LOGIN")
        masterr.configure(height=650,width=900,bg="#990066")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)
        self.menu=Menu(masterr)
        masterr['menu']=self.menu
        self.menu1=Menu(self.menu,activebackground="#990066",tearoff=0)
        self.menu.add_cascade(menu=self.menu1,label="User")
        self.menu1.add_command(label="System Guide")
        self.menu1.add_command(label="System Close")
        self.new1(masterr)
        self.help=Menu(self.menu,activebackground="#990066",tearoff=0)
        self.menu.add_cascade(menu=self.help,label="Help")
        self.help.add_command(label="About Us")
        masterr.mainloop()
        
    def new1(self,caller):
        email=StringVar();
        pwd=StringVar();
        def save1():
            e_mail=email.get()
            p_wd=pwd.get()
            if(e_mail=="" or p_wd==""):
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," (*) Feild Required")
            else:
                caller.state(newstate="iconic")
                from sclient import Myclient
                Myclient(e_mail,p_wd,caller)
                
                
                

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm1=Frame(caller,height=650,width=900,bg="#990066")
        frm1.grid(row=1,column=1,padx=330,pady=200,sticky= N+W+E+S)
        lblid=Label(frm1,text="Enter Email",fg="gray",bg="#990066",font=f)
        lblid.grid(row=1,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entid=Entry(frm1,width=35,textvariable=email)
        Entid.grid(row=2,column=1,padx=2,pady=2,sticky= N+W+E+S)
        lblpass=Label(frm1,text="Enter Password",fg="gray",bg="#990066",font=f)
        lblpass.grid(row=3,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entpass=Entry(frm1,width=35,show="*",textvariable=pwd)
        Entpass.grid(row=4,column=1,padx=2,pady=2,sticky= N+W+E+S)
        submit=Button(frm1,width=3,text="Save Details",bg="gray",fg="#990066",command=save1)
        submit.grid(row=5,column=1,padx=30,pady=20,sticky= N+W+E+S)
        forget=Button(frm1,width=20,text="Forgot Password",bg="gray",fg="#990066")
        forget.grid(row=6,column=1,sticky=N+W+E+S,padx=2,pady=20)
        
Login()

        
        
        
