import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
class TLogin:
    def __init__(self,mwindow):
        global masterr
        masterr =Toplevel(mwindow)   
        
        masterr.title("FACULTY LOGIN")
        masterr.configure(height=650,width=900,bg="#FF33FF")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)
        self.menu=Menu(masterr)
        masterr['menu']=self.menu
        self.menu1=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.menu1,label="Admin")
        self.menu1.add_command(label="System Guide")
        self.new(masterr)
        self.help=Menu(self.menu,activebackground="pink",tearoff=0)
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
                import mysql.connector 
                cnx = mysql.connector.connect(user='root', password='aashishgolu', host='127.0.0.1', database='project')
                if(cnx):
                    cursor=cnx.cursor()
                    try:
                        q= "select password from t_register where email=%s "
                        data= (e_mail,)
                        cursor.execute(q,data)
                        
                        row_pass=str(cursor.fetchone()[0])
                        print(str(row_pass))
                        if(pass_word==str(row_pass)):
                            from Attendance_sheet import attendance
                            attendance(masterr,e_mail,row_pass)
                        else:
                            import tkMessageBox
                            tkMessageBox.showwarning("Warning","Incorrect Psaaword")
                        
                        cnx.commit()
        
                    except Exception as e:
                        import tkMessageBox
                        tkMessageBox.showwarning("Warning",str(e))
                    cursor.close
                cnx.close() 
            
        

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm1=Frame(masterr,height=650,width=900,bg="#FF33FF")
        frm1.grid(row=1,column=1,sticky= N+W+E+S,padx=350,pady=200)
        lblid=Label(frm1,text="Email",fg="blue",bg="#FF33FF",anchor=CENTER,font=f)
        lblid.grid(row=1,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entid=Entry(frm1,width=35,textvariable=email)
        Entid.grid(row=2,column=1,padx=2,pady=2,sticky= N+W+E+S)
        lblpass=Label(frm1,text="Password",fg="blue",bg="#FF33FF",font=f)
        lblpass.grid(row=3,column=1,padx=2,pady=2,sticky= N+W+E+S)
        Entpass=Entry(frm1,width=35,show="*",textvariable=password)
        Entpass.grid(row=4,column=1,padx=2,pady=2,sticky= N+W+E+S)
        submit=Button(frm1,width=15,text="Submit Details",bg="blue",fg="white",command=submit)
        submit.grid(row=5,column=1,padx=2,pady=20)
        forget=Button(frm1,width=20,text="Forgot Password",bg="blue",fg="white")
        forget.grid(row=6,column=1,sticky=N+W+E+S,padx=2,pady=20)
        
        
        
        
