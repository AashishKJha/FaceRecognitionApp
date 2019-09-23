import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
import ttk
class LoginAccepted:
    def __init__(self,masterr,email):
        masterr=Toplevel(masterr)
        masterr.title("DATA INPUT")
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
                from steachercredit import STcredit
                STcredit(course__name1,sem__no1,stream_no1,caller,email)
            else:
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," (*) Feild Required")
##            def capt():
##                from pccap import UpperBody
##                UpperBody(course__name1,sem__no1,stream_no1)
##            if(course__name1!="" and sem__no1!="" and stream_no1!=""):
##                cap=Button(frm1,width=10,text="Capture",bg="blue",fg="white",command=capt)
##                cap.grid(row=3,column=2,sticky=W,padx=30,pady=20)

                
        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm1=Frame(caller,height=650,width=900,bg="#990066")
        frm1.grid(row=1,column=1,sticky= N+W+E+S,padx=200,pady=150)
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
        submit=Button(frm1,width=10,text="Save Details",bg="gray",fg="#990066",command=save2)
        submit.grid(row=2,column=4,sticky=W,padx=30,pady=20)
        
