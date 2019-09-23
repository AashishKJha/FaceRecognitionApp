import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
class TLogin:
    def __init__(self,mwindow):
        global masterr
        masterr = mwindow 
        
        masterr.title("ADMIN LOGIN")
        masterr.configure(height=650,width=900,bg="#990066")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)
        self.menu=Menu(masterr)
        masterr['menu']=self.menu
        self.menu1=Menu(self.menu,activebackground="#990066",tearoff=0)
        self.menu.add_cascade(menu=self.menu1,label="Admin")
        self.menu1.add_command(label="System Guide")
        self.new(masterr)
        self.help=Menu(self.menu,activebackground="#990066",tearoff=0)
        self.menu.add_cascade(menu=self.help,label="help")
        self.help.add_command(label="About Us")
        
        masterr.mainloop()
    def new(self,caller):
        email=StringVar()
        password=StringVar()
        def submit():
            e_mail=str(email.get())
            pass_word=str(password.get())
            if(e_mail=="" or pass_word==""):
                import tkMessageBox
                tkMessageBox.showwarning("Warning","(*) Feild Required")
            else:
                if(str(e_mail)=="aashishjha.1994@gmail.com" and str(pass_word)=="891994"):
                    from main import mainwindow
                    mainwindow(caller,e_mail)
                else:
                    print("Incorrect Email Or Password")
        def forget():
            import tkMessageBox
            tkMessageBox.showwarning("Information","Contact system admin for further assistance.")
            
            
        

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm1=Frame(masterr,height=650,width=900,bg="#990066")
        frm1.grid(row=1,column=1,sticky= N+W+E+S,padx=350,pady=200)
        lblid=Label(frm1,text="Email",fg="gray",bg="#990066",anchor=CENTER,font=f)
        lblid.grid(row=1,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entid=Entry(frm1,width=35,textvariable=email)
        Entid.grid(row=2,column=1,padx=2,pady=2,sticky= N+W+E+S)
        lblpass=Label(frm1,text="Password",fg="gray",bg="#990066",font=f)
        lblpass.grid(row=3,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entpass=Entry(frm1,width=35,show="*",textvariable=password)
        Entpass.grid(row=4,column=1,padx=2,pady=2,sticky= N+W+E+S)
        submit=Button(frm1,width=15,text="Submit Details",bg="gray",fg="#990066",command=submit)
        submit.grid(row=5,column=1,padx=2,pady=20)
        forget=Button(frm1,width=20,text="Forgot Password",bg="gray",fg="#990066",command=forget)
        forget.grid(row=6,column=1,sticky=N+W+E+S,padx=2,pady=20)
win=Tk()
TLogin(win)
        
        
        
        
